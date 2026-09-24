#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
圖表同步：wiki 投資筆記的本機圖片 → Astro public/charts/ ＋ 連結改寫。

為什麼需要這一步（踩雷紀錄）：
  wiki 筆記裡的圖片連結是「相對檔名」（例：![](1999_xxx_chart1.png)），
  但 Astro 只有 public/ 會被原樣複製到網站根目錄；直接搬進文章 → 圖片 404。
  本步驟把圖檔複製到 public/charts/，並把連結改寫成 /charts/<檔名>。

設計原則（與 import_wiki.py 一致的 wipe-and-rebuild）：
  - 以 manifest 記錄本次寫入的檔案；下次執行時刪除不在清單內的舊檔（避免殘留孤兒圖）。
  - 內容相同（md5）不重寫，避免 git 無謂變動。

對外介面：
  sync(dry_run=False) -> dict[來源絕對路徑, "/charts/<檔名>"]
  rewrite(body, md_path, chart_map) -> 改寫後的 body
用法：
  python3 scripts/sync_charts.py            # 同步並報告
  python3 scripts/sync_charts.py --dry-run  # 只報告
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.expanduser("~/.hermes/wiki/投資")
PUB = os.path.join(ROOT, "public", "charts")
# manifest 放在 scripts/（不進 public/，避免被部署到公開網站）
MANIFEST = os.path.join(ROOT, "scripts", ".charts_manifest.json")

# 只處理本機相對連結；外部 http(s) 連結一律不動
IMG_RE = re.compile(r"!\[([^\]]*)\]\((?!https?://)([^)\s]+\.(?:png|jpg|jpeg|webp|gif|svg))\)", re.I)
SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__"}


def md5(path: str) -> str:
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_wiki_md():
    for dp, dn, fns in os.walk(WIKI):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for fn in sorted(fns):
            if fn.endswith(".md"):
                yield os.path.join(dp, fn)


def find_links(md_path: str):
    """回傳 [(alt, 相對連結, 解析後絕對路徑)]"""
    try:
        text = open(md_path, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError):
        return []
    base = os.path.dirname(md_path)
    out = []
    for alt, link in IMG_RE.findall(text):
        out.append((alt, link, os.path.normpath(os.path.join(base, link))))
    return out


def sync(dry_run: bool = False, verbose: bool = True):
    """複製 wiki 圖片到 public/charts/；回傳 {來源絕對路徑: "/charts/檔名"}"""
    os.makedirs(PUB, exist_ok=True)
    prev = {}
    if os.path.exists(MANIFEST):
        try:
            prev = json.load(open(MANIFEST, encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            prev = {}

    chart_map, wanted, missing, copied, reused = {}, {}, [], 0, 0
    for md_path in iter_wiki_md():
        for _alt, link, abs_src in find_links(md_path):
            if not os.path.isfile(abs_src):
                missing.append((os.path.relpath(md_path, WIKI), link))
                continue
            name = os.path.basename(abs_src)
            # 檔名衝突且來源不同 → 加短雜湊前綴（可重現、不覆蓋他人圖）
            if name in wanted and wanted[name] != abs_src:
                name = f"{hashlib.md5(abs_src.encode()).hexdigest()[:8]}_{name}"
            wanted[name] = abs_src
            chart_map[abs_src] = f"/charts/{name}"
            dst = os.path.join(PUB, name)
            if os.path.exists(dst) and md5(dst) == md5(abs_src):
                reused += 1
                continue
            if not dry_run:
                shutil.copy2(abs_src, dst)
            copied += 1

    # 清掉不再被引用的孤兒圖（含上一個 manifest 留下、但已無人引用的）
    orphans = []
    for name in prev:
        if name not in wanted:
            orphans.append(name)
            if not dry_run and os.path.exists(os.path.join(PUB, name)):
                os.remove(os.path.join(PUB, name))

    if not dry_run:
        json.dump(wanted, open(MANIFEST, "w", encoding="utf-8"), ensure_ascii=False, indent=0, sort_keys=True)

    if verbose:
        print(f"CHARTS：同步 {len(wanted)} 張圖（新寫 {copied}、沿用 {reused}、清孤兒 {len(orphans)}）"
              f"｜引用筆記 {len({os.path.dirname(p) for p in chart_map})} 篇", file=sys.stderr)
        for rel, link in missing[:10]:
            print(f"  ⚠️ 連結指向不存在的圖：{rel} → {link}", file=sys.stderr)
    return chart_map


def rewrite(body: str, md_path: str, chart_map: dict) -> str:
    """把 body 內的本機圖片連結改寫成 /charts/<檔名>（找不到來源者保持原樣並回報）"""
    base = os.path.dirname(md_path)

    def sub(m):
        alt, link = m.group(1), m.group(2)
        abs_src = os.path.normpath(os.path.join(base, link))
        url = chart_map.get(abs_src)
        return f"![{alt}]({url})" if url else m.group(0)

    return IMG_RE.sub(sub, body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    cm = sync(dry_run=args.dry_run)
    if args.dry_run:
        print(f"（dry-run，未寫入任何檔案）共 {len(cm)} 張")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
