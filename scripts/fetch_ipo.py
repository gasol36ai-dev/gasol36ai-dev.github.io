#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抓取「今日台股公開申購（IPO 抽籤）截止」資訊 → src/data/ipo.json

設計：
  1. 重用 CFO 既有腳本 `ipo_subscription_today.py` 的抓取函式（單一真相來源，
     避免把 TWSE／HiStock 的踩雷知識複製成第二份而分歧）。
  2. 與該腳本差異：這裡**不做 30% 篩選**，輸出「今日截止」全部標的 ＋ 是否達門檻，
     讓網站呈現完整畫面；門檻仍標示為 30%。
  3. **非致命**：抓取失敗時寫入 source_ok=false，不讓網站更新流程中斷
     （前端有日期閘門，過期資料不會顯示）。

輸出契約：永遠 exit 0（除非寫檔失敗），狀態記在 JSON 內。
"""
import importlib.util
import json
import os
import sys
import traceback
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "src", "data", "ipo.json")
CFO_SCRIPT = os.path.expanduser("~/.hermes/profiles/cfo/scripts/ipo_subscription_today.py")
THRESHOLD = 30.0


def load_cfo_module():
    """載入 CFO 的 IPO 腳本為模組（不執行其 main）。"""
    spec = importlib.util.spec_from_file_location("ipo_cfo", CFO_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組（檔案不存在或非 Python）：{CFO_SCRIPT}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mmdd(iso):
    return iso[5:].replace("-", "/") if iso else "?"


def main():
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    weekday = now.weekday()

    doc = {
        "date": today,
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%S+08:00"),
        "trading_day": weekday < 5,
        "source_ok": False,
        "threshold": THRESHOLD,
        "items": [],
        "error": None,
    }

    if weekday >= 5:
        doc["source_ok"] = True          # 週末：確定無申購截止，非失敗
        doc["note"] = "週末無申購截止作業"
        _write(doc)
        return 0

    try:
        m = load_cfo_module()
        twse = m.load_twse()
        hs = m.load_histock()
        try:
            shares = m.load_shares()
        except Exception:
            shares = {}
    except Exception as e:
        doc["error"] = f"{type(e).__name__}: {e}"
        _write(doc)
        print(f"⚠️ IPO 抓取失敗（非致命）：{doc['error']}", file=sys.stderr)
        return 0

    # 今日截止 ＋ 排除已取消抽籤
    ends = [v for v in twse.values() if v["end"] == today]
    ends = [v for v in ends
            if not v["cancel_raw"] or v["cancel_raw"] in ("0", "-", "N", "否")]

    for t in sorted(ends, key=lambda x: x["code"]):
        h = hs.get(t["code"], {})
        rate = h.get("rate")
        mkt = h.get("market_price")
        spread = None
        if rate is not None:
            spread = round(rate, 2)
        elif mkt is not None and t.get("underwrite_price"):
            spread = round((mkt - t["underwrite_price"]) / t["underwrite_price"] * 100, 2)

        issued = shares.get(t["code"])
        dilution = None
        if t.get("underwrite_shares") and issued:
            dilution = round(t["underwrite_shares"] / issued * 100, 3)

        doc["items"].append({
            "code": t["code"],
            "name": t["name"],
            "market": t["market"],
            "start": t["start"],
            "end": t["end"],
            "period": f"{mmdd(t['start'])}~{mmdd(t['end'])}",
            "underwrite_price": t["underwrite_price"],
            "market_price": mkt,
            "spread": spread,
            "dilution": dilution,
            "lottery_date": t["lottery_date"],
            "qualified": (spread is not None and spread >= THRESHOLD),
            "histock_matched": bool(h),
        })

    doc["source_ok"] = True
    _write(doc)
    q = sum(1 for i in doc["items"] if i["qualified"])
    print(f"IPO：今日截止 {len(doc['items'])} 檔（達 {THRESHOLD:.0f}% 門檻 {q} 檔）", file=sys.stderr)
    return 0


def _write(doc):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
        f.write("\n")


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(1)
