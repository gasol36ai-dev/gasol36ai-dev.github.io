#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
從 wiki 投資筆記抽出「黃金關鍵價位」（給圖表用）。

支援兩種格式（前者為機器可讀、建議未來日報採用）：
  A. 機器區塊（優先）
     <!-- levels:gold -->
     current: 4710.57
     entry: 4680-4700
     addon: 4760-4780
     stop: 4620
     <!-- /levels -->
  B. 既有 markdown 粗體欄位（fallback）
     **Current Price**: $4,710.57
     - **Entry**: $4,680 - $4,700
     - **Add-on**: $4,760 - $4,780
     - **Stop-loss**: $4,620

設計原則：寧可少抓、不可抓錯。抓不到完整欄位（current + entry 或 stop）的檔案一律略過，
並在報告中列出「有部分欄位但不完整」的檔案，避免圖表出現假的價位。

CLI：python3 scripts/extract_levels.py
"""
import json
import os
import re
import sys

WIKI = os.path.expanduser("~/.hermes/wiki/投資")
INDEX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wiki_index.json")

BLOCK_RE = re.compile(r"<!--\s*levels:gold\s*-->(.*?)<!--\s*/levels\s*-->", re.S | re.I)
NUM = r"([\d]{1,3}(?:,\d{3})*(?:\.\d+)?)"
PAIR = rf"\$?{NUM}\s*(?:[-–~到]|to)\s*\$?{NUM}"

MD_PATTERNS = {
    "current": re.compile(rf"(?:Current Price|Current price|現價|Spot)\**\s*[:：]\s*\**\s*\$?{NUM}"),
    "entry": re.compile(rf"\*\*(?:Entry|進場[^:*]*)\*\*\s*[:：]\s*\$?{PAIR}", re.I),
    "addon": re.compile(rf"\*\*(?:Add-?on|加碼[^:*]*)\*\*\s*[:：]\s*\$?{PAIR}", re.I),
    "stop": re.compile(rf"\*\*(?:Stop-?loss|停損[^:*]*)\*\*\s*[:：]\s*\$?{NUM}", re.I),
}


def _f(s: str) -> float:
    return float(s.replace(",", ""))


def _pair_from(text: str):
    m = re.search(PAIR, text, re.I)
    if not m:
        one = re.search(rf"\$?{NUM}", text)
        if not one:
            return None
        v = _f(one.group(1))
        return (v, v)
    a, b = _f(m.group(1)), _f(m.group(2))
    return (min(a, b), max(a, b))


def parse_block(text: str):
    """格式 A：<!-- levels:gold --> 區塊"""
    m = BLOCK_RE.search(text)
    if not m:
        return None
    kv = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            kv[k.strip().lower()] = v.strip()
    rec = {}
    if "current" in kv:
        mm = re.search(rf"{NUM}", kv["current"])
        rec["current"] = _f(mm.group(1)) if mm else None
    if "entry" in kv:
        rec["entry"] = _pair_from(kv["entry"])
    if "addon" in kv:
        rec["addon"] = _pair_from(kv["addon"])
    if "stop" in kv:
        mm = re.search(rf"{NUM}", kv["stop"])
        rec["stop"] = _f(mm.group(1)) if mm else None
    return rec or None


def parse_markdown(text: str):
    """格式 B：既有粗體欄位"""
    rec = {}
    for key, pat in MD_PATTERNS.items():
        m = pat.search(text)
        if not m:
            continue
        if key in ("entry", "addon"):
            rec[key] = (_f(m.group(1)), _f(m.group(2)))
        else:
            rec[key] = _f(m.group(1))
    return rec or None


def usable(rec) -> bool:
    """至少要能畫出階梯：現價 +（進場區 或 停損）"""
    if not rec or rec.get("current") is None:
        return False
    return rec.get("entry") is not None or rec.get("stop") is not None


def extract_all(verbose: bool = True):
    """回傳 (完整紀錄 list, 不完整清單 list)"""
    if not os.path.exists(INDEX):
        if verbose:
            print("LEVELS：找不到 wiki_index.json，跳過", file=sys.stderr)
        return [], []
    idx = json.load(open(INDEX, encoding="utf-8"))
    good, partial = [], []
    for rel, info in sorted(idx.items()):
        if info.get("excluded"):
            continue
        path = os.path.join(WIKI, rel)
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        rec = parse_block(text) or parse_markdown(text)
        if not rec:
            continue
        # 只收黃金相關（避免把其他標的的價位畫成黃金圖）
        blob = rel + text[:4000]
        if not re.search(r"gold|黃金|XAU", blob, re.I):
            continue
        rec.update({
            "rel": rel,
            "date": info.get("date") or "",
            "title": info.get("title") or os.path.basename(rel),
            "source_kind": "block" if parse_block(text) else "markdown",
        })
        (good if usable(rec) else partial).append(rec)
    if verbose:
        print(f"LEVELS：可繪圖 {len(good)} 篇、欄位不完整 {len(partial)} 篇", file=sys.stderr)
        for r in partial[:8]:
            have = [k for k in ("current", "entry", "addon", "stop") if r.get(k) is not None]
            print(f"  ⚠️ {os.path.basename(r['rel'])}：僅有 {','.join(have) or '無'}", file=sys.stderr)
    return good, partial


if __name__ == "__main__":
    g, p = extract_all()
    for r in g:
        print(f"{r['date'] or '----------'}  {os.path.basename(r['rel'])[:40]:42s} "
              f"cur={r.get('current')} entry={r.get('entry')} addon={r.get('addon')} stop={r.get('stop')} [{r['source_kind']}]")
    sys.exit(0)
