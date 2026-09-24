#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 2：讀 wiki_index.json → 產生 Astro 文章（含 frontmatter、NDA 宣告）

圖表：wiki 筆記內的本機圖片連結會先同步到 public/charts/，並改寫成 /charts/<檔名>
      （否則相對連結在網站上必定 404；見 sync_charts.py）。

用法：
    python3 scripts/import_wiki.py --dry-run    # 只報告，不寫檔
    python3 scripts/import_wiki.py              # 實際寫入 src/content/posts/invest/
"""
import argparse, json, os, re, shutil, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import nda_check
import sync_charts

WIKI = os.path.expanduser("~/.hermes/wiki/投資")
INDEX = os.path.join(ROOT, "scripts", "wiki_index.json")
DEST = os.path.join(ROOT, "src", "content", "posts", "invest")

LABEL2SLUG = {
    "每日戰情室": "warroom", "能源追蹤": "energy", "AI與機器人": "ai-robotics",
    "黃金分析": "gold", "台股IPO": "ipo", "顯示驅動市場": "display",
    "AI眼鏡": "ai-glasses", "研究筆記": "research",
}

FM_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


def slugify(name: str) -> str:
    s = unicodedata.normalize("NFKD", name)
    s = s.lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "post"


def derive_title(rel: str, body: str) -> str:
    """標題：優先取內文 H1；否則由檔名還原（底線轉空格、去日期前綴）。"""
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if m:
        t = re.sub(r"[#*`]+", "", m.group(1)).strip()
        if t:
            # H1 若實為檔名形式（含底線、無空格），還原成可讀標題
            if "_" in t and " " not in t:
                t = re.sub(r"\s{2,}", " ", t.replace("_", " ")).strip()
            return t[:120]
    stem = os.path.splitext(os.path.basename(rel))[0]
    stem = re.sub(r"^\d{4}-\d{2}-\d{2}[-_]\s*", "", stem)
    stem = stem.replace("_", " ")
    stem = re.sub(r"\s{2,}", " ", stem).strip()
    return (stem or os.path.splitext(os.path.basename(rel))[0])[:120]


def first_paragraph(body: str) -> str:
    """取首段作為摘要；剝除 Markdown 與 LaTeX 標記，過長加省略號。"""
    for raw in body.split("\n"):
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("|") or line.startswith(">"):
            continue
        if line.startswith(("-", "*", "```", "![")):
            continue
        # 含 LaTeX／跳脫字元的行直接跳過，改取第一段乾淨散文（避免碎片外露）
        if "$" in line or "\\" in line:
            continue
        txt = re.sub(r"[*_`\[\]]|\(http[^)]*\)", "", line)
        txt = re.sub(r"\s{2,}", " ", txt).strip(" -·|")
        if len(txt) >= 12:
            return txt[:140] + ("…" if len(txt) > 140 else "")
    return ""


def yaml_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "''")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(INDEX):
        sys.exit(f"❌ 找不到 {INDEX}，請先執行 classify_wiki.py")
    idx = json.load(open(INDEX, encoding="utf-8"))

    # 圖表同步（wiki 圖片 → public/charts/）；dry-run 時只計算不複製
    chart_map = sync_charts.sync(dry_run=args.dry_run)

    used = set()
    plan, skipped, with_charts = [], [], []

    for rel in sorted(idx):
        info = idx[rel]
        if info.get("excluded"):
            skipped.append((rel, f"NDA: {info.get('reason','')}"))
            continue
        if info.get("error"):
            skipped.append((rel, f"ERROR: {info['error']}"))
            continue
        cat_label = info.get("category", "研究筆記")
        topic = LABEL2SLUG.get(cat_label, "research")

        # 來源路徑也套用檔名黑名單（避免因改檔名而繞過）
        if nda_check.is_blocked_filename(rel):
            skipped.append((rel, "NDA: 來源檔名黑名單"))
            continue

        src_path = os.path.join(WIKI, rel)
        try:
            raw = open(src_path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError) as e:
            skipped.append((rel, f"READ: {e}"))
            continue
        body = FM_RE.sub("", raw).strip()
        if chart_map:
            new_body = sync_charts.rewrite(body, src_path, chart_map)
            if new_body != body:
                with_charts.append(rel)
            body = new_body

        slug = slugify(os.path.splitext(os.path.basename(rel))[0])
        if slug in used:
            slug = f"{slugify(os.path.basename(os.path.dirname(rel)))}-{slug}"
        n = 2
        base_slug = slug
        while slug in used:
            slug = f"{base_slug}-{n}"
            n += 1
        used.add(slug)

        title = derive_title(rel, body)
        date = info.get("date") or "2026-01-01"
        desc = first_paragraph(body)

        fm = [
            "---",
            f"title: '{yaml_escape(title)}'",
            f"description: '{yaml_escape(desc)}'",
            f"pubDate: {date}",
            "category: 'invest'",
            f"topic: '{topic}'",
            f"tags: ['{cat_label}']",
            "draft: false",
            f"source: '{yaml_escape(rel)}'",
            "nda_cleared: true",
            f"nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'",
            "---",
            "",
        ]
        out = "\n".join(fm) + body + "\n"
        plan.append((slug, topic, rel, out))

    print(f"可匯入 {len(plan)} 檔；排除 {len(skipped)} 檔")
    print(f"圖表 {len(chart_map)} 張（引用筆記 {len(with_charts)} 篇）")
    from collections import Counter
    print("\n═══ 分類分佈 ═══")
    for k, v in Counter(t for _, t, _, _ in plan).most_common():
        print(f"  {v:>5}  {k}")
    if skipped:
        print(f"\n═══ 排除清單（{len(skipped)}）═══")
        for rel, why in skipped[:20]:
            print(f"  {rel}\n      → {why}")

    if args.dry_run:
        print("\n（dry-run，未寫入任何檔案）")
        return

    # 最終 NDA 掃描（defense in depth）：寫入前逐篇再驗一次
    bad = []
    for slug, topic, rel, out in plan:
        f = []
        nda_check.scan_text(f"invest/{slug}.md", out, f)
        if any(x[0] == "BLOCK" for x in f):
            bad.append((slug, rel, sorted({x[3] for x in f if x[0] == "BLOCK"})))
    if bad:
        print(f"\n❌ 最終掃描攔阻 {len(bad)} 篇，已中止匯入：")
        for slug, rel, labels in bad[:10]:
            print(f"  {rel} → {'; '.join(labels)}")
        sys.exit(1)

    if os.path.isdir(DEST):
        shutil.rmtree(DEST)
    os.makedirs(DEST, exist_ok=True)
    for slug, topic, rel, out in plan:
        with open(os.path.join(DEST, f"{slug}.md"), "w", encoding="utf-8") as fh:
            fh.write(out)
    print(f"\n✅ 已寫入 {len(plan)} 篇 → {os.path.relpath(DEST, ROOT)}")


if __name__ == "__main__":
    main()
