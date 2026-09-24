#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日自動更新：wiki/投資 → 網站 → GitHub Pages

流程（fail-closed）：
  0. 前置檢查（Ollama／pnpm／gh）
  1. classify_wiki.py  只分類新增檔案（斷點續傳）
  2. import_wiki.py    重建文章（來源已刪除者自動移除）
  3. nda_check.py      ★ 機密閘門：BLOCK → 中止，絕不推送
  4. pnpm build
  5. git commit + push（無變更則跳過）
  6. 等 workflow → 實查線上 200

任何一步失敗都會中止並以非零退出碼回報。
"""
import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://gasol36ai-dev.github.io"
WIKI = os.path.expanduser("~/.hermes/wiki/投資")
INDEX = os.path.join(ROOT, "scripts", "wiki_index.json")


def run(cmd, timeout=3600, check=True):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    if check and r.returncode != 0:
        raise RuntimeError(f"指令失敗（{r.returncode}）：{' '.join(cmd)}\n{r.stdout[-1500:]}\n{r.stderr[-1500:]}")
    return r


def log(msg):
    print(msg, flush=True)


def count_md():
    n = 0
    for dp, dn, fns in os.walk(WIKI):
        dn[:] = [d for d in dn if d not in {".git", "node_modules"}]
        n += sum(1 for f in fns if f.endswith(".md"))
    return n


def main():
    t0 = time.time()
    log("=" * 60)
    log("每日網站更新開始")
    log("=" * 60)

    # ── 0. 前置檢查 ──────────────────────────────────────────
    try:
        run(["curl", "-s", "--max-time", "8", "http://127.0.0.1:11434/api/tags"], timeout=30)
    except Exception as e:
        log(f"❌ Ollama 無法連線，中止（不發佈未分類內容）：{e}")
        return 2
    log("✅ 前置檢查：Ollama 可用")

    wiki_total = count_md()
    log(f"wiki/投資 目前 {wiki_total} 個 .md")

    # ── 1. 分類（只處理新檔）────────────────────────────────
    log("\n[1/6] 分類新增檔案…")
    r = run([sys.executable, "scripts/classify_wiki.py", "--workers", "3"], timeout=10800)
    tail = [l for l in r.stdout.strip().splitlines() if l.strip()][-3:]
    for l in tail:
        log("   " + l)

    # ── 2. 匯入 ─────────────────────────────────────────────
    log("\n[2/6] 產生文章…")
    r = run([sys.executable, "scripts/import_wiki.py"], timeout=1800)
    line = [l for l in r.stdout.splitlines() if "已寫入" in l or "可匯入" in l]
    for l in line:
        log("   " + l)
    imported = 0
    for l in r.stdout.splitlines():
        if "已寫入" in l:
            imported = int(l.split("已寫入")[1].split("篇")[0].strip())
    log(f"   文章總數：{imported}")

    # ── 3. 機密閘門（fail-closed）───────────────────────────
    log("\n[3/6] 機密閘門掃描…")
    g = subprocess.run([sys.executable, "scripts/nda_check.py"], cwd=ROOT,
                       capture_output=True, text=True, timeout=1800)
    if g.returncode != 0:
        log("❌ 機密閘門攔阻 —— 已中止，**未推送任何內容**")
        for l in g.stdout.splitlines()[:40]:
            if "BLOCK" in l or "規則" in l or "命中" in l:
                log("   " + l.strip())
        return 3
    log("✅ 閘門通過（BLOCK = 0）")

    # ── 4. 建置 ─────────────────────────────────────────────
    log("\n[4/6] 建置…")
    b = run(["pnpm", "build"], timeout=1800)
    pages = ""
    for l in b.stdout.splitlines():
        if "page(s) built" in l:
            pages = l.strip()
    log(f"   {pages or '建置完成'}")

    # ── 5. 推送（無變更則跳過）──────────────────────────────
    log("\n[5/6] 檢查變更並推送…")
    run(["git", "add", "-A"])
    st = run(["git", "status", "--porcelain"])
    if not st.stdout.strip():
        log("   ℹ️ 無變更，跳過推送")
        log(f"\n完成（無更新），耗時 {time.time()-t0:.0f}s")
        return 0

    changed = len(st.stdout.strip().splitlines())
    run(["git", "commit", "-q", "-m",
         f"chore(auto): 每日 wiki 同步（{time.strftime('%Y-%m-%d')}，{changed} 檔變更）"])
    run(["git", "push", "origin", "main"], timeout=600)
    log(f"   已推送（{changed} 檔變更）")

    # ── 6. 等部署並實查 ─────────────────────────────────────
    log("\n[6/6] 等待部署並實查線上…")
    run_id = ""
    for _ in range(12):
        time.sleep(8)
        try:
            r = run(["gh", "run", "list", "--limit", "1", "--json", "databaseId,status,conclusion"], timeout=120)
            j = json.loads(r.stdout)[0]
            if j.get("status") == "completed":
                run_id = j.get("databaseId", "")
                if j.get("conclusion") != "success":
                    log(f"❌ 部署失敗：{j.get('conclusion')}")
                    return 4
                break
        except Exception:
            continue

    bad = []
    for p in ["/", "/invest/", "/about/", "/invest/research/", "/rss.xml"]:
        try:
            c = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                                BASE_URL + p], capture_output=True, text=True, timeout=30).stdout.strip()
        except Exception:
            c = "ERR"
        if c != "200":
            bad.append(f"{p}={c}")
    if bad:
        log(f"❌ 線上實查失敗：{', '.join(bad)}")
        return 5

    log("✅ 線上實查：5 條關鍵路由全 200")
    log(f"\n完成：{imported} 篇文章已上線，耗時 {time.time()-t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
