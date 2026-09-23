#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 1：wiki/投資 → NDA 過濾 + 8 類內容分類
產出 wiki_index.json（含每檔的分類、標題、日期、NDA 判定）
支援斷點續傳（重跑會跳過已完成的檔案）。
用法：python3 scripts/classify_wiki.py [--workers 3]
"""
import argparse, json, os, re, sys, time, threading, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import nda_check

WIKI = os.path.expanduser("~/.hermes/wiki/投資")
OUT = os.path.join(ROOT, "scripts", "wiki_index.json")
MODEL = "ornith-1.5:9b"

CATS = ["每日戰情室", "能源追蹤", "AI與機器人", "黃金分析",
        "台股IPO", "顯示驅動市場", "AI眼鏡", "研究筆記"]

SYS = """你是財經文件分類器。讀完文件後，只輸出一個數字（1-8），代表最合適的類別：
1=每日戰情室（市場日報/戰情/WarRoom）
2=能源追蹤（電力、核能、鈾、清潔能源、太陽能）
3=AI與機器人（機器人、具身智能、空間智能、自動化）
4=黃金分析（黃金、貴金屬）
5=台股IPO（新股申購、抽籤）
6=顯示驅動市場（面板、顯示驅動IC、DDIC、OLED）
7=AI眼鏡（AR/VR/MR 眼鏡、頭戴裝置）
8=研究筆記（以上皆非：量子金融、宏觀、主權、技術分析、量化指標、生醫、市場微結構）
只輸出數字，不要任何其他文字或解釋。"""

PRE = [(r"WarRoom", 1), (r"申購|抽籤|_IPO|IPO_", 5), (r"DNlite", 8)]

_lock = threading.Lock()


def pre_rule(rel):
    for pat, idx in PRE:
        if re.search(pat, rel, re.IGNORECASE):
            return idx
    return None


def ask(text):
    body = json.dumps({
        "model": MODEL, "stream": False, "think": False,
        "messages": [{"role": "system", "content": SYS},
                     {"role": "user", "content": "文件內容：\n" + text[:1200]}],
        "options": {"temperature": 0, "num_predict": 8},
    }).encode()
    req = urllib.request.Request("http://127.0.0.1:11434/api/chat", data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.load(r)["message"].get("content", "").strip()


def extract_meta(rel, text):
    """標題：首個 H1；若無則用檔名。日期：檔名前綴 YYYY-MM-DD，否則 mtime。"""
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = m.group(1).strip() if m else os.path.splitext(os.path.basename(rel))[0]
    title = re.sub(r"[#*_`]+", "", title).strip()
    dm = re.search(r"(\d{4})-(\d{2})-(\d{2})", os.path.basename(rel))
    if dm:
        date = f"{dm.group(1)}-{dm.group(2)}-{dm.group(3)}"
    else:
        date = time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(os.path.join(WIKI, rel))))
    return title[:120], date


def process(rel):
    path = os.path.join(WIKI, rel)
    try:
        text = open(path, encoding="utf-8").read()
    except (UnicodeDecodeError, OSError) as e:
        return rel, {"error": f"read: {e}"}

    # NDA 過濾（重用專案檢查器規則）
    findings = []
    nda_check.scan_text(rel, text, findings)
    if any(f[0] == "BLOCK" for f in findings):
        labels = sorted({f[3] for f in findings if f[0] == "BLOCK"})
        return rel, {"excluded": True, "reason": "; ".join(labels)}

    idx = pre_rule(rel)
    src = "pre"
    if idx is None:
        try:
            out = ask(text)
            m = re.search(r"[1-8]", out)
            idx = int(m.group(0)) if m else None
        except Exception:
            idx = None
        src = "llm"
    cat = CATS[idx - 1] if idx else "研究筆記"
    title, date = extract_meta(rel, text)
    return rel, {"category": cat, "src": src, "title": title, "date": date,
                 "bytes": len(text.encode("utf-8"))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=3)
    args = ap.parse_args()

    rels = []
    for dirpath, _, files in os.walk(WIKI):
        for fn in files:
            if fn.endswith(".md"):
                rels.append(os.path.relpath(os.path.join(dirpath, fn), WIKI))
    rels.sort()

    result = {}
    if os.path.exists(OUT):
        result = json.load(open(OUT, encoding="utf-8"))
        print(f"續傳：已有 {len(result)} 筆")

    todo = [r for r in rels if r not in result]
    print(f"總計 {len(rels)} 檔，待處理 {len(todo)} 檔，workers={args.workers}", flush=True)

    done = 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(process, r): r for r in todo}
        for fut in as_completed(futs):
            rel = futs[fut]
            try:
                r, info = fut.result()
            except Exception as e:
                r, info = rel, {"error": str(e)}
            with _lock:
                result[r] = info
                done += 1
                if done % 25 == 0:
                    json.dump(result, open(OUT, "w", encoding="utf-8"),
                              ensure_ascii=False, indent=1)
                    el = time.time() - t0
                    rate = done / el if el else 0
                    eta = (len(todo) - done) / rate / 60 if rate else 0
                    print(f"  {done}/{len(todo)}  速率 {rate:.2f}/s  ETA {eta:.0f} 分", flush=True)

    json.dump(result, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    c = Counter(v.get("category", "EXCLUDED") for v in result.values())
    print("\n═══ 分類結果 ═══")
    for k, v in c.most_common():
        print(f"  {v:>5}  {k}")
    print(f"\n總耗時 {(time.time()-t0)/60:.1f} 分；輸出 {OUT}")


if __name__ == "__main__":
    main()
