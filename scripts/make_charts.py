#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
網站圖表產生器：把 wiki 語料變成圖表（VIP 指示：blog 不能只有文字）。

輸出 → public/charts/（Astro 會原樣複製到網站根目錄）
  - blog-content-mix.png   主題分佈（各 topic 篇數＋佔比）
  - blog-timeline.png      語料時間軸（每月新增篇數）

執行（專案自帶 .venv，見 agent-output-policy）：
  .venv/bin/python scripts/make_charts.py

失敗不致命：daily_update.py 以「非致命步驟」呼叫，圖表壞掉不影響文章同步。
"""
import collections
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public", "charts")
INDEX = os.path.join(ROOT, "scripts", "wiki_index.json")
# 逐篇圖表對照（wiki rel path → [{url, alt}]）：由本腳本產生，import_wiki.py 讀取後注入文章
POST_CHARTS = os.path.join(ROOT, "scripts", ".post_charts.json")

# 分類標籤 → 網站 topic slug（與 import_wiki.LABEL2SLUG 同源；此處只為排序／配色）
TOPIC_ORDER = ["每日戰情室", "黃金分析", "能源追蹤", "AI與機器人", "AI眼鏡", "研究筆記"]
TOPIC_SLUG = {
    "每日戰情室": "warroom", "能源追蹤": "energy", "AI與機器人": "ai-robotics",
    "黃金分析": "gold", "台股IPO": "ipo", "顯示驅動市場": "display",
    "AI眼鏡": "ai-glasses", "研究筆記": "research",
}

# 配色（沿用網站 accent 色系；深淺色模式都不刺眼）
C_BAR = "#c8a24a"      # gold
C_BAR_2 = "#3f7fb3"    # blue
C_GRID = "#d8d8d8"
C_TXT = "#2b2b2b"
C_MUTED = "#6b6b6b"


def setup_font():
    """CJK 字型：PingFang SC（有 weight 600 半粗體面；Arial Unicode MS 無粗體面會靜默降級）"""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.font_manager as fm
    import matplotlib.pyplot as plt
    avail = {f.name for f in fm.fontManager.ttflist}
    font = next((c for c in ["PingFang SC", "Heiti TC", "Hiragino Sans GB", "Arial Unicode MS"]
                 if c in avail), "DejaVu Sans")
    plt.rcParams["font.sans-serif"] = [font, "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False   # 不設 → 負號變方框
    plt.rcParams["figure.dpi"] = 160
    plt.rcParams["savefig.dpi"] = 160
    plt.rcParams["savefig.bbox"] = "tight"
    return plt, font


def load_counts():
    idx = json.load(open(INDEX, encoding="utf-8"))
    per_cat, per_month = collections.Counter(), collections.Counter()
    for rel, info in idx.items():
        if info.get("excluded") or info.get("error"):
            continue
        per_cat[info.get("category") or "研究筆記"] += 1
        d = info.get("date") or ""
        if len(d) >= 7:
            per_month[d[:7]] += 1
    return per_cat, per_month


def chart_mix(plt, per_cat, total):
    labels = [t for t in TOPIC_ORDER if per_cat.get(t)]
    labels += [t for t, _ in per_cat.most_common() if t not in TOPIC_ORDER]
    vals = [per_cat[t] for t in labels]

    fig, ax = plt.subplots(figsize=(9, 4.2))
    ypos = range(len(labels))[::-1]
    colors = [C_BAR if t in ("黃金分析", "每日戰情室") else C_BAR_2 for t in labels]
    bars = ax.barh(list(ypos), vals, color=colors, height=0.62, zorder=3)
    ax.legend([bars[0], bars[-1]], ["重點追蹤主題（戰情室／黃金）", "其他主題"],
              loc="upper right", fontsize=10, framealpha=0.95)
    for y, v, t in zip(ypos, vals, labels):
        ax.text(v + max(vals) * 0.012, y, f"{v} 篇（{v / total * 100:.1f}%）",
                va="center", fontsize=10.5, color=C_TXT, fontweight=600)
    ax.set_yticks(list(ypos))
    ax.set_yticklabels([f"{t}（{TOPIC_SLUG.get(t, 'research')}）" for t in labels], fontsize=11)
    ax.set_xlim(0, max(vals) * 1.42)
    ax.set_xlabel("文章篇數", fontsize=11)
    ax.set_title(f"語料主題分佈　共 {total} 篇", fontsize=15, fontweight=600, color=C_TXT, pad=12)
    ax.grid(axis="x", color=C_GRID, lw=0.7, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="both", length=0, labelsize=10.5)
    p = os.path.join(OUT, "blog-content-mix.png")
    fig.savefig(p, facecolor="white")
    plt.close(fig)
    return p


def chart_timeline(plt, per_month):
    months = sorted(per_month)
    vals = [per_month[m] for m in months]
    xs = [datetime.date(int(m[:4]), int(m[5:7]), 1) for m in months]

    fig, ax = plt.subplots(figsize=(9, 3.6))
    ax.bar(xs, vals, width=22, color=C_BAR, zorder=3)
    ax.plot(xs, vals, color=C_BAR_2, lw=1.8, zorder=4)
    ax.set_ylim(0, max(vals) * 1.22)
    peak = max(range(len(vals)), key=lambda i: vals[i])
    ax.annotate(f"高峰 {months[peak]}　{vals[peak]} 篇", xy=(xs[peak], vals[peak]),
                xytext=(xs[max(0, peak - 3)], vals[peak] * 1.10), fontsize=10.5,
                color=C_TXT, fontweight=600,
                arrowprops=dict(arrowstyle="->", color=C_MUTED, lw=1.2))
    ax.set_ylabel("每月新增篇數", fontsize=11)
    ax.set_title(f"語料時間軸　{months[0]} – {months[-1]}（合計 {sum(vals)} 篇）",
                 fontsize=15, fontweight=600, color=C_TXT, pad=12)
    ax.grid(axis="y", color=C_GRID, lw=0.7, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=10.5, length=0)
    import matplotlib.dates as mdates
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    p = os.path.join(OUT, "blog-timeline.png")
    fig.savefig(p, facecolor="white")
    plt.close(fig)
    return p


def chart_level_ladder(plt, rec):
    """價格階梯圖：把單篇日報的關鍵價位畫成「停損／進場／現價／加碼」階梯。"""
    cur = rec.get("current")
    entry = rec.get("entry")
    addon = rec.get("addon")
    stop = rec.get("stop")
    levels = [v for v in [cur, stop] if v] + [x for pair in (entry, addon) if pair for x in pair]
    lo, hi = min(levels), max(levels)
    pad = max((hi - lo) * 0.18, hi * 0.004)

    fig, ax = plt.subplots(figsize=(8.6, 4.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(lo - pad, hi + pad)
    ax.set_xticks([])
    for s in ("top", "right", "bottom"):
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0, labelsize=10.5)
    ax.set_ylabel("黃金價格（USD/oz）", fontsize=11)

    if entry:
        ax.axhspan(entry[0], entry[1], color="#2e7d32", alpha=0.22, zorder=2)
        ax.text(0.02, (entry[0] + entry[1]) / 2, f"進場區 {entry[0]:,.0f}–{entry[1]:,.0f}",
                va="center", fontsize=11, fontweight=600, color="#1b5e20", zorder=5)
    if addon:
        ax.axhspan(addon[0], addon[1], color="#1565c0", alpha=0.20, zorder=2)
        ax.text(0.02, (addon[0] + addon[1]) / 2, f"加碼區 {addon[0]:,.0f}–{addon[1]:,.0f}",
                va="center", fontsize=11, fontweight=600, color="#0d47a1", zorder=5)
    if stop:
        ax.axhline(stop, color="#c62828", lw=2.0, ls="--", zorder=4)
        ax.annotate(f"停損 {stop:,.0f}", xy=(0.965, stop), xytext=(0, 5), textcoords="offset points",
                    ha="right", va="bottom", fontsize=11, fontweight=600, color="#c62828", zorder=7,
                    bbox=dict(facecolor="white", edgecolor="none", pad=1.5, alpha=0.92))
    if cur:
        ax.axhline(cur, color=C_BAR, lw=3.0, zorder=6)
        ax.annotate(f"現價 {cur:,.2f}", xy=(0.965, cur), xytext=(0, 6), textcoords="offset points",
                    ha="right", va="bottom", fontsize=12, fontweight=600, color="#8a6a0f", zorder=7,
                    bbox=dict(facecolor="white", edgecolor="none", pad=1.5, alpha=0.92))

    bits = []
    if cur and stop:
        bits.append(f"距停損 {(stop / cur - 1) * 100:+.1f}%")
    if cur and addon:
        bits.append(f"距加碼 {(addon[0] / cur - 1) * 100:+.1f}%")
    ax.set_title(f"黃金關鍵價位階梯　{rec.get('date') or ''}　" + "｜".join(bits),
                 fontsize=14, fontweight=600, color=C_TXT, pad=12)
    p = os.path.join(OUT, f"{os.path.basename(rec['rel']).rsplit('.', 1)[0].lower()}-gold-levels.png")
    fig.savefig(p, facecolor="white")
    plt.close(fig)
    return p


def chart_levels_timeline(plt, recs):
    """跨篇走勢：現價／進場中值／停損 隨時間的遷移（需 >= 2 篇）。"""
    recs = sorted(recs, key=lambda r: r["date"])
    xs = [datetime.date.fromisoformat(r["date"]) if r.get("date") else None for r in recs]
    xs = [x for x in xs if x]
    keep = [r for r in recs if r.get("date")]
    cur = [r["current"] for r in keep]
    stop = [r.get("stop") for r in keep]
    ent = [(r["entry"][0] + r["entry"][1]) / 2 if r.get("entry") else None for r in keep]

    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.plot(xs, cur, "-o", color=C_BAR, lw=2.4, ms=6, label="現價", zorder=4)
    if any(ent):
        ax.plot(xs, ent, "--s", color="#2e7d32", lw=1.8, ms=5, label="進場區中值", zorder=3)
    if any(stop):
        ax.plot(xs, stop, ":^", color="#c62828", lw=1.8, ms=5, label="停損", zorder=3)
    ax.fill_between(xs, [s if s else min(cur) * 0.98 for s in stop], cur,
                    color=C_BAR, alpha=0.10, zorder=1)
    ax.set_ylabel("黃金價格（USD/oz）", fontsize=11)
    ax.set_title("黃金關鍵價位走勢　" + f"{keep[0]['date']} – {keep[-1]['date']}",
                 fontsize=14, fontweight=600, color=C_TXT, pad=12)
    ax.grid(axis="y", color=C_GRID, lw=0.7, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=10.5, length=0)
    ax.legend(loc="best", fontsize=10.5, framealpha=0.95)
    import matplotlib.dates as mdates
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))
    p = os.path.join(OUT, "gold-levels-timeline.png")
    fig.savefig(p, facecolor="white")
    plt.close(fig)
    return p


def main():
    if not os.path.exists(INDEX):
        print("CHARTS：找不到 wiki_index.json，跳過", file=sys.stderr)
        return 1
    os.makedirs(OUT, exist_ok=True)
    plt, font = setup_font()
    per_cat, per_month = load_counts()
    total = sum(per_cat.values())
    made = [chart_mix(plt, per_cat, total), chart_timeline(plt, per_month)]

    # 關鍵價位圖（戰情室／黃金日報）：抓不到就不畫，絕不出現假價位
    import extract_levels
    recs, _partial = extract_levels.extract_all(verbose=False)
    post_charts, lvl_made = {}, []
    for r in recs:
        p = chart_level_ladder(plt, r)
        lvl_made.append(p)
        post_charts.setdefault(r["rel"], []).append(
            {"url": f"/charts/{os.path.basename(p)}", "alt": f"黃金關鍵價位階梯（{r.get('date')}）"})
    if len(recs) >= 2:
        p = chart_levels_timeline(plt, recs)
        lvl_made.append(p)
        newest = max(recs, key=lambda r: r["date"])
        post_charts.setdefault(newest["rel"], []).append(
            {"url": f"/charts/{os.path.basename(p)}", "alt": "黃金關鍵價位走勢（跨日報）"})
    json.dump(post_charts, open(POST_CHARTS, "w", encoding="utf-8"),
              ensure_ascii=False, indent=0, sort_keys=True)
    made += lvl_made

    ok = all(os.path.getsize(p) > 10_000 for p in made)
    detail = "、".join(f"{os.path.basename(p)}({os.path.getsize(p) // 1024}KB)" for p in made)
    print(f"CHARTS：{'產生' if ok else '異常'} {len(made)} 張｜{detail}｜字型 {font}｜語料 {total} 篇"
          f"｜價位圖 {len(lvl_made)} 張（{len(recs)} 篇可繪）", file=sys.stderr)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
