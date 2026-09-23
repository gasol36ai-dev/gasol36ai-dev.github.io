#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NDA 內容檢查器 —— default-deny（預設拒絕）

用途：攔阻任何公司機密內容被發佈到公開網站。
兩道防線共用同一支腳本：
  1. 本機 git pre-commit hook（.githooks/pre-commit）
  2. GitHub Actions 部署前的 gate（.github/workflows/deploy.yml）

用法：
    python3 scripts/nda_check.py              # 掃描整個 repo（CI 用）
    python3 scripts/nda_check.py <file> ...   # 只掃描指定檔案（pre-commit 用）

退出碼：0 = 通過；1 = 攔阻（不得發佈）
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── 掃描範圍 ────────────────────────────────────────────────
SCAN_DIRS = ["src", "public"]
SCAN_FILES = ["README.md", "astro.config.mjs", "package.json"]

# 檢查器自身與政策文件必然提到這些詞，排除以免自我觸發
EXCLUDE = {"scripts/nda_check.py", "NDA_POLICY.md"}

SKIP_EXT = {
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".ico", ".svg",
    ".woff", ".woff2", ".ttf", ".otf", ".zip", ".pdf",
}

# ── A 級：絕對禁止，無任何例外 ──────────────────────────────
BLOCK_RULES = [
    # 公司／專案識別
    (r"ILITEK|奕力|ilitek", "公司名稱"),
    (r"公司機密|商業機密|營業秘密|機密文件|機密資料|機密等級|機密事項|機密資訊|內部使用|限閱|禁止外流|密件|請勿外傳", "機密標記"),
    # 暫存器設定（VIP 明令）
    (r"暫存器|寄存器", "暫存器字樣"),
    (r"register\s*(map|setting|table|list|value|address|name)", "register 設定字樣"),
    (r"\bREG_[A-Z0-9_]+\b|\breg_[a-z0-9_]+\b|\bRG_[A-Z0-9_]+\b", "暫存器命名"),
    (r"\b[A-Z][A-Z0-9_]{2,}_(REG|CTRL|CFG|TRIM|GAIN|BIAS)\b", "暫存器命名"),
    (r"0x[0-9A-Fa-f]{2,}", "十六進位常數（疑似暫存器值／位址）"),
    (r"\[[0-9]{1,2}:[0-9]{1,2}\]", "位元欄位表示法"),
    (r"\b(i2c|iic|spi)\s*(write|read|addr|address)", "匯流排暫存器存取"),
    # 內部文件／代號
    (r"\b(D-?COG|KGM|FPC[0-9]|Glass[0-9])\b", "內部專案代號"),
    (r"客戶(名稱|名單|規格|代號|專案|窗口|聯絡)|customer\s*(name|list|spec|project)", "客戶識別資訊"),
    # ── 家族基金／個人財務（VIP 明令不得公開）──
    (r"參考市值|帳面報酬|總持倉|持有基金|基金代碼|基金持股|家族基金|基金參考|StockQ|基富通", "基金持倉字樣"),
    (r"\b[0-9]{1,3}(,[0-9]{3})+\s*(TWD|元|USD|美金)\b", "千分位金額（疑似持倉市值）"),
    (r"\b(Pru|ALI|YUI)[0-9]{3}\b", "基金代碼（英數混合）"),
    (r"\|\s*[0-9]{6}\s*\|", "基金代碼（六位數字表格欄）"),
    (r"^\s*#\s*(Gasol|Donna|Elena)\s*[-－]\s*基金", "個人基金持股標題"),
    # ── 家族基金（第二輪補強：2026-09 實測洩漏後新增）──
    (r"family\s+fund|family_fund|fund_universe", "家族基金字樣（英文／資料檔名）"),
    (r"低檔加碼|加碼策略|持倉明細|Portfolio\s+Summary|全部基金", "家族基金操作策略字樣"),
    (r"^\s*#{1,4}\s*(Gasol|Donna|Elena|Nina|Cheese)\s*$", "家族成員姓名標題"),
    (r"貝萊德|摩根基金|聯博|法巴|DWS投資|PGIM保德信|元大全球|安聯投信|野村投信|瀚亞投信|群益投信|復華投信", "基金公司名稱（疑似持倉清單）"),
    (r"基金名稱\s*\|", "基金持倉表格欄位"),
    # ── power gui／power excel 專有內容（VIP 逐字：紅線所指的「公式」）──
    (r"\bCOL_(TOTAL|IC|PANEL|GOA)_[A-Z_]+\b", "功耗工具欄位對應常數"),
    (r"\bMIPI_CURRENTS\b|\bOSC_PLL_A\b|\bANCHORS_L\d+\b|\bVG[HLS]_PUMP_TABLE\b", "功耗係數表常數"),
    (r"\bpower_core\b|\bformula_engine\b|\bWorkbookEval\b|\bevaluate_sheet\b|\bparse_power_xlsx\b|\bcompute_power\b|\brender_table_html\b", "功耗工具內部介面"),
    (r"Power\s*Estimate", "客戶功耗評估檔"),
    (r"pump_vgh|pump_vgl|VSP_vgh|VSP_vgl|VSN_vgh|VSN_vgl|ckh_ratio", "功耗公式變數"),
    (r"\(Cf\s*\+\s*Cd\)|Cp\s*\*\s*2\s*\*|Cf\s*\*\s*Vb\s*\*\s*FR|Cgc\s*\*|Cgm\s*\*", "客戶功耗公式本體"),
    (r"\bSD_OP\b|\bOXI_BOE\b|SUBPIXEL\s*ON/OFF|L255\s*\(白\)|R255\s*/\s*G255\s*/\s*B255", "面板型號／pattern 命名"),
    (r"AN\s*\*\s*VDDI\s*\+\s*AO\s*\*\s*AVDD", "功耗總和公式"),
]

# 檔名黑名單：這些檔案名本身就是個人財務，不得進入 repo
BLOCKED_FILENAMES = {"gasol.md", "donna.md", "elena.md", "nina.md", "cheese.md", "fund_ref.md", "基金投資.md"}


def is_blocked_filename(path: str) -> bool:
    """檔名黑名單判定 —— 必須同時套用於『來源路徑』與『產出路徑』。"""
    return os.path.basename(path).lower() in BLOCKED_FILENAMES

# ── A2 級：區分大小寫的規則（僅全大寫才視為文件標記）──
BLOCK_RULES_CS = [
    (r"\bCONFIDENTIAL\b", "機密標記（全大寫文件標記）"),
]

# ── B 級：通用數學（LaTeX）—— 降為提示，不攔阻 ──────────────
# VIP 2026-09 逐字澄清：「所謂的公式是指 power gui & power excel 的資訊內容」。
# 因此通用財經／學術 LaTeX 不再視為機密；真正的機密公式由上方 POWER 規則攔阻。
MATH_RULES = [
    (r"\$\$|\\\(|\\\[", "LaTeX 數學環境"),
    (r"\\(frac|sqrt|sum|int|begin|end|times|cdot|alpha|beta|gamma|delta|Delta|mu|sigma|lambda|theta|omega|partial|nabla|approx|propto|leq|geq)\b", "LaTeX 數學符號"),
    (r"^\s*[A-Za-z][A-Za-z0-9_]*\s*=\s*\S.*[+\-*/^]", "等號運算式"),
    (r"^\s*[A-Za-z][A-Za-z0-9_]*\s*\([A-Za-z0-9_,\s]*\)\s*=", "函式定義式"),
]

# 排除：HTML 屬性、Markdown 連結、程式碼引用等誤判來源
FORMULA_LINE_EXCLUDE = re.compile(
    r"=\"|='|^\s*<|\b(class|href|src|id|style|width|height|type|rel|name|value|content|aria-[\w-]+|data-[\w-]+)\s*="
)

OVERRIDE_RE = re.compile(r"<!--\s*nda-ok\s*:\s*(\S.*?)\s*-->\s*$")

# ── C 級：提醒（不攔阻，只印出）────────────────────────────
WARN_RULES = [
    (r"\b(CTE|良率|yield|載板|基板|封裝|製程|參數)\b", "製程／封裝相關字樣，請自行確認是否為公開資訊"),
]

# ── 文章 frontmatter 必填聲明 ───────────────────────────────
REQUIRE_FRONTMATTER = True
FRONTMATTER_MIN_NOTES = 10


def iter_files():
    """列出所有需要掃描的檔案（相對路徑）。"""
    for d in SCAN_DIRS:
        base = os.path.join(ROOT, d)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [x for x in dirnames if x not in {".git", "node_modules", "dist", ".astro"}]
            for fn in filenames:
                if os.path.splitext(fn)[1].lower() in SKIP_EXT:
                    continue
                yield os.path.relpath(os.path.join(dirpath, fn), ROOT)
    for f in SCAN_FILES:
        if os.path.exists(os.path.join(ROOT, f)):
            yield f


def scan_text(rel, text, findings):
    # 檔名黑名單必須在 scan_text 內也生效：匯入器以合成路徑呼叫本函式，
    # 若只放在 main() 會完全繞過（2026-09 實測洩漏的根因）。
    if is_blocked_filename(rel):
        findings.append(("BLOCK", rel, 1, "檔名黑名單", os.path.basename(rel),
                         "此檔名為個人財務資料，不得進入 repo"))
        return
    lines = text.splitlines()
    in_frontmatter = False
    for i, line in enumerate(lines, 1):
        if i == 1 and line.strip() == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if line.strip() == "---":
                in_frontmatter = False
            continue

        for pat, label in BLOCK_RULES:
            m = re.search(pat, line, re.IGNORECASE)
            if m:
                # 內容級規則可用 <!-- nda-ok: 理由 --> 人工放行（例如「禁止條款本身」的敘述文字）。
                # 檔名黑名單與全大寫 CONFIDENTIAL 標記一律不可放行。
                if OVERRIDE_RE.search(line):
                    findings.append(("OVERRIDE", rel, i, label, m.group(0), line.strip()[:100]))
                else:
                    findings.append(("BLOCK", rel, i, label, m.group(0), line.strip()[:100]))

        for pat, label in BLOCK_RULES_CS:
            m = re.search(pat, line)
            if m:
                findings.append(("BLOCK", rel, i, label, m.group(0), line.strip()[:100]))

        if not FORMULA_LINE_EXCLUDE.search(line):
            allowed = OVERRIDE_RE.search(line)
            for pat, label in MATH_RULES:
                m = re.search(pat, line, re.IGNORECASE)
                if m and not allowed:
                    findings.append(("MATH", rel, i, label, m.group(0), line.strip()[:100]))

        for pat, label in WARN_RULES:
            m = re.search(pat, line, re.IGNORECASE)
            if m:
                findings.append(("WARN", rel, i, label, m.group(0), line.strip()[:100]))


def check_frontmatter(rel, text, findings):
    """每篇文章必須明確聲明已通過 NDA 審查。"""
    if not rel.startswith("src/content/posts/") or not rel.endswith(".md"):
        return
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        findings.append(("BLOCK", rel, 1, "缺少 frontmatter", "-", "無法確認 NDA 聲明"))
        return
    fm = m.group(1)
    if not re.search(r"^nda_cleared:\s*true\s*$", fm, re.MULTILINE):
        findings.append(("BLOCK", rel, 1, "缺少 nda_cleared: true", "-", "文章未聲明已通過 NDA 審查"))
    notes = re.search(r"^nda_notes:\s*(.+)$", fm, re.MULTILINE)
    if not notes or len(notes.group(1).strip().strip("'\"#")) < FRONTMATTER_MIN_NOTES:
        findings.append(("BLOCK", rel, 1, "nda_notes 缺失或過短", "-", f"需 >= {FRONTMATTER_MIN_NOTES} 字元說明審查依據"))


def main():
    targets = sys.argv[1:]
    if targets:
        rels = []
        for t in targets:
            r = os.path.relpath(os.path.abspath(t), ROOT)
            if os.path.splitext(r)[1].lower() in SKIP_EXT:
                continue
            if r in EXCLUDE:
                continue
            rels.append(r)
    else:
        rels = [r for r in iter_files() if r not in EXCLUDE]

    findings = []
    scanned = 0
    for rel in sorted(set(rels)):
        path = os.path.join(ROOT, rel)
        if not os.path.isfile(path):
            continue
        if os.path.basename(rel).lower() in BLOCKED_FILENAMES:
            findings.append(("BLOCK", rel, 1, "檔名黑名單", os.path.basename(rel), "此檔名為個人財務資料，不得進入 repo"))
            continue
        try:
            text = open(path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        scanned += 1
        scan_text(rel, text, findings)
        check_frontmatter(rel, text, findings)

    blocks = [f for f in findings if f[0] == "BLOCK"]
    warns = [f for f in findings if f[0] == "WARN"]
    overrides = [f for f in findings if f[0] == "OVERRIDE"]
    maths = [f for f in findings if f[0] == "MATH"]

    print(f"NDA 檢查：掃描 {scanned} 檔")
    print(f"  · 通用數學式（提示，不攔阻）：{len(maths)} 行")
    if overrides:
        print(f"\n── 人工放行（nda-ok）{len(overrides)} 筆 ──")
        for kind, rel, ln, label, hit, ctx in overrides[:20]:
            print(f"  [OVERRIDE] {rel}:{ln}  {label}  →  {hit}")
    if warns:
        print(f"\n── 提醒（不攔阻）{len(warns)} 筆 ──")
        for kind, rel, ln, label, hit, ctx in warns[:20]:
            print(f"  [WARN] {rel}:{ln}  {label}  →  {hit}")
        if len(warns) > 20:
            print(f"  …另有 {len(warns) - 20} 筆")

    if blocks:
        print(f"\n❌ 攔阻 {len(blocks)} 筆 —— 不得發佈：\n")
        for kind, rel, ln, label, hit, ctx in blocks:
            print(f"  [{kind}] {rel}:{ln}")
            print(f"          規則：{label}")
            print(f"          命中：{hit}")
            print(f"          內容：{ctx}")
        print("\n公司機密（含公式、暫存器設定）絕對不得上網。")
        print("若確認為公開通用內容，請於該行末尾加： <!-- nda-ok: 你的理由 -->")
        return 1

    print("\n✅ 通過：未發現公司機密內容")
    return 0


if __name__ == "__main__":
    sys.exit(main())
