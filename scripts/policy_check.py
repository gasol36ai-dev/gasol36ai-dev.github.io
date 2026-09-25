#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
policy_check.py — 部落格「編輯政策」閘門（fail-closed，管線第三道）

與 nda_check.py 的分工
----------------------
- nda_check.py ：公司機密（客戶名、未公開專案、競爭對手代號…）
- policy_check.py：**編輯政策**——README 明訂
  「投資類文章為個人紀錄，不構成投資建議，不推薦特定標的、不揭露具體持倉」

2026-09-25 實測：日報含完整交易參數（進場／加碼／停損／T1-T3／均價／
實際成交狀態）可零命中通過 nda_check，並被 import_wiki.py 自動 draft:false
推上公開網站，造成實際公開洩漏。本閘門即為補上這個缺口。

管線位置：import_wiki → policy_redact → nda_check → **policy_check** → build → push
本檢查器與 policy_redact.py **刻意不共用程式碼**：改寫器的 bug 不應能
靜默通過驗證器。

用法
----
    python3 policy_check.py                     # 掃描 src/content/posts
    python3 policy_check.py <file.md> ...
退出碼：0 = 通過；1 = 攔阻（呼叫端必須中止，不得推送）
"""
from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIR = os.path.join(ROOT, "src", "content", "posts")

# 負向後顧：排除產品售價／毛利情境（「內部目標 $1,000」、「產品目標價」）。
# 皆為固定寬度 2 字，Python 的 lookbehind 要求等寬才合法。
_PRICE_KW = r"(?<!內部)(?<!產品)(?<!定價)(?<!售價)(?<!毛利)(?<!目標)"

# 關鍵字與數值之間可能夾著 markdown 強調符：`- **加碼**：4,200`。
# 只允許空白是錯的（2026-09-25 實際漏檢，且 redactor 同步漏檢）。
_MD = r"[\s*_`]*"
_GAP = _MD + r"價?" + _MD
_CUR = r"(?:\$|NT\$|US\$)?"
_NUM = r"\d[\d,]*(?:\.\d+)?"

BLOCK_RULES: list[tuple[str, str]] = [
    # ── 交易價位指令（核心政策：不構成投資建議）──
    # 負向後顧：產品售價與毛利情境（「內部目標 $1,000」「產品目標價」）
    # 不是投資價位。實測誤報：Ray-Ban Meta $449、Phoenix ASP $2,000。
    (_PRICE_KW + r"(進場|加碼|停損|停利|目標|買點|賣點)" + _GAP + r"[:：]"
     + _MD + _CUR + _MD + _NUM, "交易價位指令"),
    # 裸寫價位：無冒號、無幣別。實測洩漏的「進場 4,240／加碼 4,200／
    # 停損 4,150」正是繞過冒號版的寫法。關鍵字與數字之間只允許空白與
    # 「價」，因此「停損率 44.4%」這類統計敘述不會誤判。
    (_PRICE_KW + r"(進場|加碼|停損|停利|均價|買點|賣點|建倉|出場)" + _GAP
     + _CUR + _MD + _NUM, "交易價位指令（裸寫）"),
    (r"\bT[123]\b\s*[:：]?\s*\$?\d", "目標階梯價位"),
    (r"(支撐|壓力|頸線)\s*(?:\$|NT\$)?\s*\d[\d,]*(?:\.\d+)?\s*(?:元|美元|USD|TWD)?\s*(?:為|即|進場|出場)",
     "以價位作為進出場依據"),
    # ── 倉位與風險預算建議 ──
    (r"倉位上限|部位上限|單一資產.{0,6}上限|單日新增風險|最大回撤容忍|風險預算",
     "倉位／風險預算建議"),
    (r"(減碼|加碼|減倉|加倉|出清|部位)\s*\d+\s*%", "倉位比例指令"),
    (r"(減|加)\s*\d+/\d+", "部位分數指令"),
    (r"停損(上移|下移|設在|移至)", "停損操作指令"),
    (r"(月內|連續)\s*停損\s*\d+\s*次", "停損紀律規則"),
    # ── 第一人稱持倉揭露 ──
    (r"我的持倉|我的部位|目前持有|目前已進場|已進場|持有中|成本價|未實現損益|帳面損益",
     "個人持倉揭露"),
    (r"(進場單|加碼單|停損單)[^。\n]{0,12}(成交|觸及|掛|取消)", "實際下單揭露"),
    # ── 投資建議語氣 ──
    (r"建議買進|建議賣出|建議加碼|建議減碼|應買入|應賣出|應加碼|可買進|可放空",
     "投資建議語氣"),
    (r"建議[^。\n]{0,12}(部位|倉位|曝險|配置|比重)", "部位配置建議"),
    (r"(不宜|宜|應)[^。\n]{0,8}(加碼|減碼|買進|賣出)", "操作指令語氣"),
    # ── 家族基金（紅線，與 nda_check 獨立重複檢查）──
    (r"家族基金|基富通|StockQ|基金代碼|基金持股|參考市值|帳面報酬|持有基金|全部基金|低檔加碼",
     "家族基金內容"),
    # ── 任職公司名稱（獨立於 nda_check 的重複防線）──
    (r"奕力|Ilitek|ILITEK", "任職公司名稱"),
    # ── 內部方法論代號 ──
    # 詞邊界陷阱：Python 3 的 \w 涵蓋 CJK，`\bTJB\b` 在「宏觀TJB與微觀TJB」
    # 這種中英相鄰處沒有邊界 → 檢查失效。改用只排除 ASCII 字母數字。
    (r"(?<![A-Za-z0-9])(?:TJB|MJB)(?![A-Za-z0-9])", "內部方法論代號"),
]

WARN_RULES: list[tuple[str, str]] = [
    # 注意：這條**必須大小寫敏感**。用 re.I 會讓 "and"、"the" 之類
    # 全小寫單字也被當成股票代號，實測產生 200+ 筆噪音，
    # 反而訓練人忽略警告。
    (r"\b[A-Z]{2,5}\b(?=\s*(?:收|漲|跌|—|：))", "個股／ETF 代號（請確認非推薦）"),
    (r"台積電|2330|TSMC", "個股名稱（請確認非推薦）"),
    (r"\b\d{4}\.TW\b|\b\d{4}\.TWO\b", "台股代號"),
]
WARN_CASE_SENSITIVE = {0}   # WARN_RULES 中需大小寫敏感的索引


def check_text(path: str, text: str) -> tuple[list[str], list[str]]:
    blocks, warns = [], []
    for i, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("#") and not re.search(r"\d", line):
            continue
        for pat, label in BLOCK_RULES:
            m = re.search(pat, line, re.I)
            if m:
                blocks.append(f"{path}:{i}\n    規則：{label}\n"
                              f"    命中：{m.group(0)[:40]!r}\n"
                              f"    內容：{line.strip()[:120]}")
                break
        else:
            for idx, (pat, label) in enumerate(WARN_RULES):
                flags = 0 if idx in WARN_CASE_SENSITIVE else re.I
                m = re.search(pat, line, flags)
                if m:
                    warns.append(f"{path}:{i}  [WARN] {label} → {m.group(0)}")
                    break
    return blocks, warns


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    targets: list[str] = list(args)
    if not targets:
        for dp, dn, fns in os.walk(DEFAULT_DIR):
            dn[:] = [d for d in dn if d not in {"node_modules", ".git"}]
            targets += [os.path.join(dp, f) for f in fns if f.endswith(".md")]
        targets.sort()
    if not targets:
        print("❌ 找不到任何 .md 可檢查")
        return 1

    all_blocks, all_warns = [], []
    for p in targets:
        try:
            text = open(p, encoding="utf-8", errors="ignore").read()
        except OSError as e:
            all_blocks.append(f"{p}: 讀取失敗 {e}")
            continue
        b, w = check_text(p, text)
        all_blocks += b
        all_warns += w

    print(f"POLICY_CHECK：掃描 {len(targets)} 篇")
    if all_warns:
        print(f"── 提醒（不攔阻）{len(all_warns)} 筆 ──")
        for w in all_warns[:10]:
            print(f"  {w}")
    if all_blocks:
        print(f"\n❌ 編輯政策攔阻 {len(all_blocks)} 筆 —— 不得發布：\n")
        for b in all_blocks[:25]:
            print(f"  [BLOCK] {b}")
        print("\n本部落格投資類文章為個人紀錄，不構成投資建議，"
              "不推薦特定標的、不揭露具體持倉。")
        print("請先跑 scripts/policy_redact.py 改寫後重試。")
        return 1
    print("✅ 通過：符合編輯政策（無交易價位、無倉位建議、無持倉揭露）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
