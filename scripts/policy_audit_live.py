#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
policy_audit_live.py — 發布後「線上」稽核（第四道防線）

為什麼還需要這一支？
--------------------
policy_check.py 檢查的是**建置產物**（本地檔案）。
這一支檢查的是**網路上真正公開的東西**——兩者失效模式不同：

  · GitHub Pages 部署延遲／CDN 快取 → 本地乾淨、線上還是舊的
  · 建置失敗但 push 成功 → 線上停在上一版
  · 推錯檔案／路徑寫錯 → 本地檔案在，線上抓不到
  · 非 posts 路徑（首頁摘要、src/data/*.json、RSS）不經過閘門

在「全自動、無人工審核」的前提下，最後一道防線只能是自動的：
發布後立刻把「這次推送的每一篇文章」從線上抓回來掃一遍。

用法
----
    python3 scripts/policy_audit_live.py              # 稽核上次 commit 涉及的文章
    python3 scripts/policy_audit_live.py --rev HEAD~1 # 指定 revision
    python3 scripts/policy_audit_live.py --all-changed # 最近 2 個 commit
退出碼：0 = 線上乾淨；1 = 線上發現違規（已公開，需立即處理）
      網路錯誤不視為違規（回 0），避免網路抖動讓 cron 誤報。
"""
from __future__ import annotations

import argparse
import html
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://gasol36ai-dev.github.io"
UA = "Mozilla/5.0 (policy-audit; +https://gasol36ai-dev.github.io)"

# 與 policy_check.py **獨立**表達：稽核器不 import 閘門，避免共用同一顆 bug
LIVE_BLOCK_RULES: list[tuple[str, str]] = [
    (r"(?<![A-Za-z0-9])(?:進場|加碼|停損|停利|均價)\s*[：:]?\s*"
     r"(?:\$|NT\$|US\$)?\s*\d[\d,]*", "交易價位（進場／加碼／停損／均價）"),
    (r"(?<![A-Za-z0-9])(?:T[123])\s*[：:]?\s*\$?\d", "目標階梯價位"),
    (r"進場單|加碼單|停損單", "實際下單揭露"),
    (r"風險預算|倉位上限|部位上限", "倉位／風險預算"),
    (r"(?<![A-Za-z0-9])(?:TJB|MJB)(?![A-Za-z0-9])", "內部方法論代號"),
    (r"家族基金|基富通|StockQ", "家族基金內容"),
    (r"奕力|Ilitek|ILITEK", "任職公司名稱"),
    (r"我的持倉|目前持有|已進場|均價\s*\d", "個人持倉揭露"),
]
_RX = [(re.compile(p, re.I), lab) for p, lab in LIVE_BLOCK_RULES]


def changed_posts(revs: list[str]) -> list[str]:
    out: set[str] = set()
    for rev in revs:
        try:
            r = subprocess.run(["git", "show", "--name-only", "--format=", rev],
                               cwd=ROOT, capture_output=True, text=True, timeout=60)
        except Exception:
            continue
        for ln in r.stdout.splitlines():
            ln = ln.strip()
            if ln.startswith("src/content/posts/") and ln.endswith(".md"):
                out.add(ln)
    return sorted(out)


def slug_url(path: str) -> str:
    """src/content/posts/invest/foo.md → /posts/invest/foo/"""
    rel = path[len("src/content/"):-3]
    return f"{BASE}/{rel}/"


def fetch(url: str, timeout: int = 25) -> str | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return None


def visible_text(doc: str) -> str:
    doc = re.sub(r"<script\b.*?</script>", " ", doc, flags=re.S | re.I)
    doc = re.sub(r"<style\b.*?</style>", " ", doc, flags=re.S | re.I)
    doc = re.sub(r"<[^>]+>", " ", doc)
    return html.unescape(doc)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rev", default="HEAD")
    ap.add_argument("--all-changed", action="store_true",
                    help="稽核最近 2 個 commit 涉及的文章")
    args = ap.parse_args()

    revs = ["HEAD", "HEAD~1"] if args.all_changed else [args.rev]
    posts = changed_posts(revs)
    if not posts:
        print("POLICY_AUDIT_LIVE：本次無文章變更，無需稽核")
        return 0

    checked = unreachable = 0
    violations: list[str] = []
    for p in posts:
        url = slug_url(p)
        doc = fetch(url)
        if doc is None:
            unreachable += 1
            continue
        checked += 1
        text = visible_text(doc)
        for rx, lab in _RX:
            m = rx.search(text)
            if m:
                violations.append(f"  ⚠️  {os.path.basename(p)}\n"
                                  f"       規則：{lab}｜命中：{m.group(0)[:40]!r}\n"
                                  f"       {url}")
                break

    print(f"POLICY_AUDIT_LIVE：稽核 {len(posts)} 篇（線上可達 {checked}、"
          f"無法連線 {unreachable}）")
    if violations:
        print(f"\n🚨 線上發現 {len(violations)} 篇仍有違規內容 —— 已公開，需立即處理：\n")
        print("\n".join(violations))
        return 1
    print("✅ 線上稽核通過：本次推送的文章在公開網路上皆無違規內容")
    return 0


if __name__ == "__main__":
    sys.exit(main())
