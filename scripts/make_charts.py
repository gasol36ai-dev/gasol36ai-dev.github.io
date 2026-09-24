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


def main():
    if not os.path.exists(INDEX):
        print("CHARTS：找不到 wiki_index.json，跳過", file=sys.stderr)
        return 1
    os.makedirs(OUT, exist_ok=True)
    plt, font = setup_font()
    per_cat, per_month = load_counts()
    total = sum(per_cat.values())
    made = [chart_mix(plt, per_cat, total), chart_timeline(plt, per_month)]

    ok = all(os.path.getsize(p) > 10_000 for p in made)
    detail = "、".join(f"{os.path.basename(p)}({os.path.getsize(p) // 1024}KB)" for p in made)
    print(f"CHARTS：{'產生' if ok else '異常'} {len(made)} 張｜{detail}｜字型 {font}｜語料 {total} 篇",
          file=sys.stderr)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
