#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日自動更新：wiki/投資 → 網站 → GitHub Pages（排程 10:00）

流程（fail-closed）：
  0. 前置檢查（Ollama 可用）
  1. classify_wiki.py  只分類新增檔案（斷點續傳）
  2. import_wiki.py    重建文章（來源已刪除者自動移除）
  3. nda_check.py      ★ 機密閘門：BLOCK → 中止，絕不推送
  4. pnpm build
  5. git commit + push（無變更則跳過）
  6. 等 workflow → 實查線上 200

stdout 即為交付報告（cron no_agent 模式原樣發送）。
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

R = {}          # 報告欄位
ERR = []        # 失敗訊息


def run(cmd, timeout=3600, check=True):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    if check and r.returncode != 0:
        raise RuntimeError(f"指令失敗（exit {r.returncode}）：{' '.join(cmd)}\n"
                           f"{r.stdout[-800:]}\n{r.stderr[-800:]}")
    return r


def count_md():
    n = 0
    for dp, dn, fns in os.walk(WIKI):
        dn[:] = [d for d in dn if d not in {".git", "node_modules"}]
        n += sum(1 for f in fns if f.endswith(".md"))
    return n


def report(status, note=""):
    head = "📦 網站每日更新" if status == "ok" else "🚨 網站每日更新失敗"
    out = [f"{head}（{time.strftime('%Y-%m-%d %H:%M')}）", ""]
    if status == "ok":
        out += [
            "✅ 結果：成功",
            f"· wiki 檔案：{R.get('wiki', '?')} 個 .md",
            f"· 新增分類：{R.get('newly', 0)} 檔",
            f"· 文章總數：{R.get('posts', '?')} 篇（排除 {R.get('excluded', '?')} 檔）",
            "· 機密閘門：通過（BLOCK = 0）",
            f"· 建置：{R.get('pages', '?')}",
            f"· 推送：{R.get('push', '?')}",
            f"· 線上實查：{R.get('live', '?')}",
            f"· 耗時：{R.get('secs', '?')} 秒",
        ]
        if note:
            out += ["", note]
        out += ["", f"🔗 {BASE_URL}/"]
    else:
        out += [f"❌ 結果：{note}", "", "⛔ 已中止，**網站未更新**（fail-closed）", ""]
        out += ["── 失敗詳情 ──"] + ERR[:25]
    return "\n".join(out)


def main():
    t0 = time.time()
    try:
        # 0. 前置檢查
        try:
            run(["curl", "-s", "--max-time", "8", "http://127.0.0.1:11434/api/tags"], timeout=30)
        except Exception as e:
            ERR.append(f"Ollama 無法連線（分類需要它）：{e}")
            return 2
        R["wiki"] = count_md()

        # 1. 分類（只處理新檔）
        before = len(json.load(open(os.path.join(ROOT, "scripts", "wiki_index.json"), encoding="utf-8"))) \
            if os.path.exists(os.path.join(ROOT, "scripts", "wiki_index.json")) else 0
        r = run([sys.executable, "scripts/classify_wiki.py", "--workers", "3"], timeout=10800)
        after = len(json.load(open(os.path.join(ROOT, "scripts", "wiki_index.json"), encoding="utf-8")))
        R["newly"] = max(0, after - before)

        # 2. 匯入
        r = run([sys.executable, "scripts/import_wiki.py"], timeout=1800)
        for l in r.stdout.splitlines():
            if "可匯入" in l:
                R["posts"] = l.split("可匯入")[1].split("檔")[0].strip()
                R["excluded"] = l.split("排除")[1].split("檔")[0].strip()

        # 3. 機密閘門（fail-closed）
        g = subprocess.run([sys.executable, "scripts/nda_check.py"], cwd=ROOT,
                           capture_output=True, text=True, timeout=1800)
        if g.returncode != 0:
            ERR.append("機密閘門攔阻（未推送任何內容）：")
            ERR += [l.strip() for l in g.stdout.splitlines() if "BLOCK" in l or "命中" in l][:20]
            return 3

        # 4. 建置
        b = run(["pnpm", "build"], timeout=1800)
        for l in b.stdout.splitlines():
            if "page(s) built" in l:
                R["pages"] = l.strip().split("]")[-1].strip()

        # 5. 推送
        run(["git", "add", "-A"])
        st = run(["git", "status", "--porcelain"])
        if not st.stdout.strip():
            R["push"] = "無變更（跳過）"
            R["live"] = "未部署（無變更）"
            R["secs"] = f"{time.time()-t0:.0f}"
            print(report("ok", "ℹ️ wiki 無新增內容，本次未變更。"))
            return 0
        changed = len(st.stdout.strip().splitlines())
        run(["git", "commit", "-q", "-m",
             f"chore(auto): 每日 wiki 同步（{time.strftime('%Y-%m-%d')}，{changed} 檔變更）"])
        run(["git", "push", "origin", "main"], timeout=600)
        R["push"] = f"{changed} 檔變更"

        # 6. 等部署 + 線上實查
        deployed = False
        for _ in range(15):
            time.sleep(8)
            try:
                r = run(["gh", "run", "list", "--limit", "1",
                         "--json", "status,conclusion"], timeout=120)
                j = json.loads(r.stdout)[0]
                if j.get("status") == "completed":
                    if j.get("conclusion") != "success":
                        ERR.append(f"GitHub Actions 部署失敗：{j.get('conclusion')}")
                        return 4
                    deployed = True
                    break
            except Exception:
                continue
        if not deployed:
            ERR.append("等待部署逾時（15 次輪詢未完成）")
            return 4

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
            ERR.append("線上實查失敗：" + ", ".join(bad))
            return 5
        R["live"] = "5 條關鍵路由全 200"
        R["secs"] = f"{time.time()-t0:.0f}"
        print(report("ok"))
        return 0

    except Exception as e:
        ERR.append(str(e))
        return 1
    finally:
        if ERR:
            print(report("fail", ERR[0] if len(ERR) == 1 else ERR[0]))


if __name__ == "__main__":
    code = main()
    sys.exit(code)
