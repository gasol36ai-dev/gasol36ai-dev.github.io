---
title: '1999–2000 Dot-Com Cycle: Gold vs Equities（歷史對照手冊）'
description: 'Gold 內部路徑（window A 內）：'
pubDate: 2026-09-24
category: 'invest'
topic: 'gold'
tags: ['黃金分析']
draft: false
source: 'knowledge/research/1999_dotcom_gold_regime_playbook.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# 1999–2000 Dot-Com Cycle: Gold vs Equities（歷史對照手冊）

> 產出：2026-09-23 20:49–20:56 CFO session（Gasol 黃金價格數據驗證架構 thread），資料全數當場實抓（LBMA 14,688 筆、Fed archive、Yahoo chart API）。原產物 `profiles/cfo/cron/output/history_dotcom/1999_dotcom_gold_vs_equities.md`（含 json＋scripts）→ 本頁為 promote 歸檔（COO 09-24 04:12 批次建議、本批 09-24 09:00 CFO 批次落盤）。
> 2026-09-24 20:31 追加：**四張核心圖表**（同一批原始序列重繪，非示意圖）。

## 圖表 (Charts) — 四張核心視覺化
> 產出：2026-09-24 20:22–20:31 CST｜產生器 `profiles/cfo/cron/output/history_dotcom/make_charts.py`｜每張圖渲染後均經視覺複核（無文字重疊／無裁切／CJK 正常／數值與本文一致）。

### 圖 1｜1999–2004 全週期指數化對照（1999-06-30 = 100）
![1999-2004 網路泡沫全週期：黃金 vs 股市](/charts/1999_dotcom_gold_regime_playbook_chart1_indexed.png)
- 讀法：紅＝Nasdaq、藍虛線＝S&P 500、金＝黃金。重點在 2000-03 之後——紅線崩落、金線橫盤，直到 2002 年才交叉向上。
- Nasdaq 泡沫頂 **+88%**；同期黃金最高僅 **+25%**（華盛頓協議急拉），泡沫頂當日 **+11.2%**。
- 2004 年底：黃金 **167**（+67%）vs Nasdaq **81**（仍低於 1999 年水準）。

### 圖 2｜制度轉向三要素 (Regime Flip)：政策利率 / 殖利率＋美元 / 黃金
![制度轉向三要素](/charts/1999_dotcom_gold_regime_playbook_chart2_regime_flip.png)
- 上：Fed 目標利率階梯 — 1999-06-30 首升 → 2000-05-16 6.50% → 2001-01-03 轉降 → 2001-12 1.75%
- 中：DXY（紫，左軸）＋ US 10Y（綠虛線，右軸）— 美元 2002-01 見頂 120.24、10Y 6.67%→3.61%
- 下：黃金 — 橫盤 18–24 個月後，2002–2003 才起漲
- 讀法：垂直虛線＝首升息／泡沫頂／最後升息／轉降息／美元見頂。**黃金只在「轉降息＋美元見頂」之後才付錢。**

### 圖 3｜兩個世代對照：1999 版「被討厭的低點」vs 2026 版「擁擠的高位」
![黃金兩個世代對照](/charts/1999_dotcom_gold_regime_playbook_chart3_gold_1999_vs_2026.png)
- A（1999–2003）：自 20 年低點 252.80 啟動，央行是賣方，悲觀＝高不對稱
- B（2022–2026）：自 2022 低點 +165.8%、2026-01-29 高點 5,405.00 → 現價 4,329.55（−19.9%）
- 讀法：兩者同為「黃金 vs DXY 反向」結構，但**起點位階完全相反**。

### 圖 4｜泡沫破裂後黃金有對沖效果嗎？— 沒有
![泡沫破裂後累積報酬](/charts/1999_dotcom_gold_regime_playbook_chart4_post_peak_returns.png)
- 基準＝2000-03-10 泡沫頂當日｜Nasdaq **−22.8%／−61.9%／−61.8%／−74.7%**（+6M/+12M/+24M/+36M）
- S&P 500 **+6.8%／−15.4%／−16.3%／−42.1%**｜黃金 **−6.1%／−6.1%／+0.3%／+22.1%**
- 結論：**前 24 個月 beta ≈ 0**，+36M 才 +22.1%。

## Sources (all pulled live 2026-09-23)
- LBMA Gold Price PM fix (USD/oz, daily since 1968-04-01)：prices.lbma.org.uk/json/gold_pm.json（14,688 entries；last = 2026-09-22 = 4,329.55）
- Nasdaq Composite / S&P 500 / US 10Y (^TNX) / DXY (DX-Y.NYB)：Yahoo Finance chart API (daily & monthly)
- FOMC target rate change record：federalreserve.gov/monetarypolicy/openmarket_archive.htm
- Washington Agreement on Gold (1999-09-26)：Wikipedia / Guardian gold timeline（$338 spot high Oct-1999）

## 1. Fed policy path (authoritative, Fed archive)
- 1998-11-17 cut → 4.75%（1999 升息循環起點）
- 1999-06-30 +25 → 5.00% ← FIRST HIKE（window A 起點）
- 1999-08-24 +25 → 5.25%
- 1999-11-16 +25 → 5.50%
- 2000-02-02 +25 → 5.75%
- 2000-03-21 +25 → 6.00%（Nasdaq 峰後 11 天）
- 2000-05-16 +50 → 6.50%（terminal rate）
- 2001-01-03 −50 → 6.00% ← PIVOT（intermeeting）
- 2001 全年：−475bp → 1.75%（2001-12-11）

## 2. Window A：1999-06-30（首次升息）→ 2000-03-10（泡沫峰），8.3 個月
- Nasdaq Composite：2,686.12 → 5,048.62 = **+88.0%**
- S&P 500：1,372.71 → 1,527.46（峰 2000-03-24）= +11.3%
- Gold (LBMA PM)：261.00 → 290.25 = **+11.2%**
- DXY (monthly)：1999-09 98.54 → 2000-03 105.44

Gold 內部路徑（window A 內）：
- low 1999-07-20 252.80（"Brown Bottom"，首次升息後 3 週）
- 1999-09-20 255.40
- 1999-10-05 325.50 ← 11 個交易日 +27.5%（Washington Agreement 1999-09-26）
- 2000-03-10 290.25

## 3. Window B：峰後（黃金的非避險期）
- Nasdaq：5,048.62 → 3,321.29（2000-04-14，−34.2%/5 週）→ 1,950.40（2001-12，−61.4%）→ 1,108.49（2002-10 low，−78.0%）
- S&P 500：1,527.46 → 768.63（2002-10 low，−49.7%）
- Gold：290.25 → 282.00（2000-04-14，−2.8%）→ 274.45（2000-12，−5.4%）→ 255.95（2001-04-02 low，−11.8%）→ 276.50（2001-12，−4.7%）→ 347.20（2002-12，+19.6%）→ 416.25（2003-12，+43.4%）→ 513.00（2005-12，+76.7%）→ 833.75（2007-12，+187.3%）

## 4. 為何黃金最終啟動（2001–2002）
- US 10Y：6.667%（2000-01）→ 5.03%（2001-12）→ 3.607%（2002-09）
- DXY：120.24（2002-01 峰）→ 101.85（2002-12）→ 86.92（2003-12）＝峰後 −27.7%
- Fed：6.50% → 1.75%（2001 年 −475bp）
- **觸發器＝政策＋匯率體制轉向，非股市見頂。落後 ≈ 24 個月。**

## 5. 當前週期定位（as of 2026-09-22 LBMA PM = 4,329.55）
- 2025 曆年：2,609.10 → 4,367.80 = +67.4%
- 2026 YTD：−0.9%｜2026 高 5,405.00（2026-01-29）→ −19.9% drawdown
- Trailing：1Y +16.4%｜2Y +66.1%｜3Y +124.6%｜5Y +144.1%｜10Y +223.3%
- 自 2022-11-03 週期低點 1,628.75 → +165.8%
- Fed：3.50–3.75%（2025 Sep/Oct/Dec 三次 −75bp 後）— hawkish hold
- 10Y 4.66%｜30Y 5.238%｜DXY ~99.7–100.6（Dec-2024 108.49）

## 6. Analogue verdict（類比裁決）
**相似**：hawkish-plateau Fed、capex/tech 敘事撐起的股市高點、高長端殖利率、財政壓力。

**決定性差異**：
1. 1999 黃金＝20 年低點、央行為賣方（最大悲觀、高不對稱）。2026 黃金＝自 2022 低 +166%、consensus long、處於 −20% 修正（不對稱反轉）。
2. 1999 Fed 剛要開始升息（逆風）。2026 Fed 已降 75bp（寬鬆動能已部分兌現）。
3. 1999–2001 USD 處多頭（96→120，逆風）。2026 DXY ~100 vs 108.5（Dec-2024）— 僅溫和順風。

**⇒ 結論：黃金對股市下跌在前 12–24 個月的 beta ≈ 0。1999 劇本不支持「買黃金對沖 AI 泡沫」；支持的是「黃金在政策/美元體制翻轉後才付錢」。**

## 警報觸發清單（對照當前）
- Fed 開啟新降息循環（連續降息且終點 <3%）
- DXY 跌破並站穩 95–96 以下
- TIPS 實質利率轉負
- 三者皆未觸發前：勿以「AI 泡沫對沖」為由加碼黃金（beta≈0 之歷史證據）

## 附錄：圖表產生與驗證 (Reproducibility)
- 產生器：`~/.hermes/profiles/cfo/cron/output/history_dotcom/make_charts.py`
- 執行方式：`uv run --python 3.12 --with matplotlib python make_charts.py`（uv 臨時環境，不需建 venv、不在家目錄新增目錄）
- 原始序列（同目錄）：`lbma_gold_pm.json`、`ixic_daily.json`、`gspc_daily.json`、`dxy.json`、`tnx.json`、`dxy_recent.json`
- 字型：PingFang SC，weight 600（CJK 半粗體）。教訓：Arial Unicode MS 無粗體面，matplotlib 會靜默降級為 regular（`findfont: Failed to find font weight bold`），字重需改用 600 才會生效
- 驗證方式：每張 PNG 產生後做渲染視覺複核（文字重疊／邊緣裁切／CJK 豆腐字／標註數值與本文一致性）。首版被抓到 2 個真實缺陷並修正重繪：① 年終標註誤植為「2003 年底」但實際取到 2004-12-31 的值；② 圖例與 Nasdaq 峰值註解碰撞
- 發佈副本：本目錄 `1999_dotcom_gold_regime_playbook_chart{1..4}_*.png`（與 profile 產出之 md5 一致）

## 歷史紀錄
- 2026-09-24：新建（promote 自 CFO session 產物）。
- 2026-09-24 20:31：追加四張核心圖表＋圖表產生與驗證附錄；修正簡體字殘留（起点→起點、暦年→曆年）。
