#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
policy_redact.py — 部落格「編輯政策」自動改寫器（第三道防線）

為什麼需要？
------------
README 的編輯政策：投資類文章為個人紀錄，不構成投資建議，
不推薦特定標的、不揭露具體持倉。

2026-09-25 實測發現：wiki 日報含完整交易參數（進場／加碼／停損／T1-T3、
均價、實際成交狀態），經 import_wiki.py 自動 draft:false 直接推上公開網站，
而 nda_check.py 只擋公司機密、攔不到這些。已實際造成公開洩漏。

本腳本在「匯入之後、閘門之前」把違規內容改寫掉：
  import_wiki.py → 【policy_redact.py】→ nda_check.py → policy_check.py → build

策略（依序）
------------
1. INLINE：可保留脈絡者就地改寫（內部方法論代號 TJB/MJB → 技術面/總經面）
2. DROP  ：整行為交易指令／持倉揭露者，整行刪除
3. 清掉因刪行而變空的段落標題，避免留下空殼

設計原則
--------
- **不動 frontmatter**：只在第二個 `---` 之後的內文作用。
- **確定性**：同一份輸入永遠得到同一份輸出（可重跑、可審計）。
- **獨立表達**：規則不 import policy_check，改寫器的 bug 不該能靜默通過閘門。
- **冪等**：重複執行結果相同。

用法
----
    python3 policy_redact.py                # 改寫 src/content/posts 下所有 .md
    python3 policy_redact.py --dry-run      # 只報告，不寫檔
    python3 policy_redact.py --dir <path>
退出碼：0 = 完成（含「無需改寫」）
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from collections.abc import Callable

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIR = os.path.join(ROOT, "src", "content", "posts")

# ── 1. 就地改寫：保留分析價值，只拿掉不該公開的識別 ──────────────
# 順序重要：先處理「英文全名（代號）」形式，再處理裸用代號。
#
# 詞邊界陷阱：Python 3 的 `\w` 涵蓋 CJK，所以 `\bTJB\b` 在
# 「宏觀TJB與微觀TJB」這種中英相鄰處**沒有邊界**，改寫與檢查都會失效
# （2026-09-25 實際殘留於線上）。改用只排除 ASCII 字母數字的 lookaround。
_B_L = r"(?<![A-Za-z0-9])"
_B_R = r"(?![A-Za-z0-9])"


def _cjk_adjacent(s: str, a: int, b: int) -> bool:
    """TJB/MJB 前後是否緊貼中文字。"""
    def is_cjk(i: int) -> bool:
        return 0 <= i < len(s) and "\u4e00" <= s[i] <= "\u9fff"
    return is_cjk(a - 1) or is_cjk(b)


def _code_repl(zh: str, en: str):
    """依語境決定替換字：中文句子裡用中文詞，英文句子裡用英文詞。"""
    def fn(m):
        return zh if _cjk_adjacent(m.string, m.start(), m.end()) else en
    return fn


_PRICE_KW = r"(?<!內部)(?<!產品)(?<!定價)(?<!售價)(?<!毛利)(?<!目標)"

INLINE_RULES: list[tuple[str, str | Callable[[re.Match[str]], str]]] = [
    (r"(Technical Judgment Base)\s*[（(]\s*TJB\s*[）)]", r"\1"),
    (r"(Macro Judgment Base)\s*[（(]\s*MJB\s*[）)]", r"\1"),
    (_B_L + r"TJB" + _B_R, _code_repl("技術基準", "technical base")),
    (_B_L + r"MJB" + _B_R, _code_repl("總經基準", "macro base")),
    # 引用內部證據編號（WIKI-01、FLOW-03a…）
    (r"\b(?:WIKI|FLOW|MACRO|PRICE|TECH|FX|GOLD)-\d{1,2}[a-z]?\b", "[內部編號]"),
    # 內部知識庫實體路徑
    (r"~?/Users/ai/\.hermes/[^\s）),]*", "[內部路徑]"),
]

# ── 2. 整行刪除：交易指令與持倉揭露 ──────────────────────────────
# 註：關鍵字與數字之間只允許空白與「價」，故「停損率 44.4%」這類
#     統計敘述不會被誤刪。
DROP_LINE_RULES: list[tuple[str, str]] = [
    (_PRICE_KW + r"(進場|加碼|停損|停利|目標|買點|賣點)\s*價?\s*[:：]\s*"
     r"(?:\$|NT\$|US\$)?\s*\d", "交易價位（帶冒號）"),
    (_PRICE_KW + r"(進場|加碼|停損|停利|目標)\s*價?\s*(?:\$|NT\$|US\$)\s*\d",
     "交易價位（帶幣別）"),
    (_PRICE_KW + r"(進場|加碼|停損|停利|均價|買點|賣點|建倉|出場)\s*價?\s*[:：]?\s*"
     r"(?:\$|NT\$|US\$)?\s*\d[\d,]*(?:\.\d+)?", "交易價位（裸寫）"),
    (r"\bT[123]\b\s*[:：]?\s*\$?\d", "目標階梯價位"),
    (r"倉位上限|部位上限|單一資產.{0,6}上限|單日新增風險|最大回撤容忍|風險預算",
     "倉位／風險預算"),
    (r"(減碼|加碼|減倉|加倉|出清|部位)\s*\d+\s*%", "倉位比例指令"),
    (r"(減|加)\s*\d+/\d+", "部位分數指令"),
    (r"停損(上移|下移|設在|移至)", "停損操作指令"),
    (r"(月內|連續)\s*停損\s*\d+\s*次", "停損紀律規則"),
    (r"我的持倉|我的部位|目前持有|目前已進場|已進場|持有中|成本價|未實現損益|帳面損益",
     "個人持倉揭露"),
    (r"(進場單|加碼單|停損單)[^。\n]{0,12}(成交|觸及|掛|取消)", "實際下單揭露"),
    (r"建議買進|建議賣出|建議加碼|建議減碼|應買入|應賣出|應加碼|可買進|可放空",
     "投資建議語氣"),
    (r"建議[^。\n]{0,12}(部位|倉位|曝險|配置|比重)", "部位配置建議"),
    # 家族基金（紅線）
    (r"家族基金|基富通|StockQ|基金代碼|基金持股|參考市值|帳面報酬|持有基金|全部基金|低檔加碼",
     "家族基金內容"),
    # 任職公司名稱
    (r"奕力|Ilitek|ILITEK", "任職公司名稱"),
    # 風控紀律（屬投資建議範疇）
    (r"(無進場觸發|不建倉|停止加碼|持續加碼|左側觀察區)", "操作紀律"),
]

_DROP_RES = [(re.compile(p, re.I), lab) for p, lab in DROP_LINE_RULES]
_HEADING_RE = re.compile(r"^(#{1,6})\s")
_BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")


def _level(line: str) -> int:
    m = _HEADING_RE.match(line)
    return len(m.group(1)) if m else 0


def split_frontmatter(text: str) -> tuple[str, str]:
    """回傳 (frontmatter, body)。沒有 frontmatter 時前者為空字串。"""
    if not text.startswith("---"):
        return "", text
    m = re.match(r"^---\r?\n.*?\r?\n---\r?\n?", text, re.S)
    if not m:
        return "", text
    return text[:m.end()], text[m.end():]


def redact_body(body: str) -> tuple[str, list[tuple[int, str, str]], int]:
    """改寫內文。回傳 (新內文, [(行號, 規則, 原文)], 就地改寫行數)。

    注意：INLINE 改寫也必須計入「有變更」，否則只有 TJB→技術面 這種
    純就地改寫的檔案不會被寫回，閘門將永遠攔阻同一批檔案。
    """
    hits: list[tuple[int, str, str]] = []
    inline_n = 0
    lines = body.splitlines()
    out: list[str] = []

    for i, line in enumerate(lines, 1):
        # 1. 就地改寫
        new = line
        for pat, repl in INLINE_RULES:
            new = re.sub(pat, repl, new)
        if new != line:
            inline_n += 1

        # 2. 整行刪除
        dropped = None
        for rx, label in _DROP_RES:
            if rx.search(new):
                dropped = label
                break
        if dropped:
            hits.append((i, dropped, line.strip()))
            continue

        out.append(new)

    # 3. 清掉變空的段落標題。
    # 只有當下一個非空行是「同級或更上級」標題（代表本段落沒有內容）才刪。
    # 誤刪案例：`## Market Segmentation` 緊接 `### By Type` 是合法的父子
    # 標題結構，子標題層級更深（3 > 2），必須保留。
    cleaned: list[str] = []
    for idx, ln in enumerate(out):
        lv = _level(ln)
        if lv:
            j = idx + 1
            while j < len(out) and not out[j].strip():
                j += 1
            if j >= len(out):
                continue                      # 文末空標題
            nlv = _level(out[j])
            if 0 < nlv <= lv:
                continue                      # 緊接下一個同級／上級標題 → 空段落
        cleaned.append(ln)

    # 4. 收斂連續空行
    final: list[str] = []
    for ln in cleaned:
        if not ln.strip() and final and not final[-1].strip():
            continue
        final.append(ln)

    return "\n".join(final).rstrip() + "\n", hits, inline_n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=DEFAULT_DIR)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(args.dir):
        print(f"❌ 目錄不存在：{args.dir}")
        return 1

    targets = []
    for dp, dn, fns in os.walk(args.dir):
        dn[:] = [d for d in dn if d not in {"node_modules", ".git"}]
        targets += [os.path.join(dp, f) for f in fns if f.endswith(".md")]
    targets.sort()

    changed = 0
    total_hits = 0
    total_inline = 0
    detail: list[str] = []
    for p in targets:
        text = open(p, encoding="utf-8", errors="ignore").read()
        head, body = split_frontmatter(text)
        new_body, hits, inline_n = redact_body(body)
        if not hits and not inline_n:
            continue
        changed += 1
        total_hits += len(hits)
        total_inline += inline_n
        rel = os.path.relpath(p, os.path.dirname(args.dir))
        detail.append(f"  {rel}：刪除 {len(hits)} 行、就地改寫 {inline_n} 行")
        for ln, label, snippet in hits[:6]:
            detail.append(f"      L{ln} [{label}] {snippet[:72]}")
        if not args.dry_run:
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(head + new_body)

    mode = "（試跑，未寫檔）" if args.dry_run else ""
    print(f"POLICY_REDACT：掃描 {len(targets)} 篇，改寫 {changed} 篇，"
          f"刪除 {total_hits} 行、就地改寫 {total_inline} 行 {mode}")
    if detail:
        print("\n".join(detail[:60]))
    if changed == 0:
        print("  （無違規內容）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
