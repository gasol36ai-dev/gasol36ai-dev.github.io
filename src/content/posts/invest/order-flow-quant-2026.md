---
title: 'Advanced Quantitative TA & Order Flow (2026)'
description: ''
pubDate: 2026-05-16
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Order_Flow_Quant_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Advanced Quantitative TA & Order Flow (2026)

## 1. Order Flow Microstructure
### Order Flow Imbalance (OFI)
- **Definition:** The net difference between buyer-initiated and seller-initiated trades at the best bid/offer.
- **Key Insight:** OFI is a primary predictor of short-term price movement. High asymmetry in limit flows (LOB fade) often precedes large price jumps.
- **Macro Correlation:** Macroeconomic news announcements systematically reshape the return-flow relationship, typically increasing price impact while dampening flow impact.

### CVD (Cumulative Volume Delta)
- Used to identify **absorption** (price doesn't move despite high delta) and **divergence** (price makes new high, CVD makes lower high), signaling imminent reversals.

## 2. Market Profile & Volume Analysis
### TPO & Value Area (VA)
- **TPO (Time Price Opportunity):** Identifies where the market spends the most time.
- **POC (Point of Control):** The price level with the highest TPO count.
- **Rotational Strategy:** Trading the rotation between Value Area High (VAH) and Value Area Low (VAL) during consolidation.
- **Initiative vs. Responsive Activity:** Gaps outside the previous day's VA signal initiative activity (strong conviction), while trading within the VA is responsive.

### Volume Profile Integration
- **VPOC (Volume POC):** The level with the highest actual volume. Often a stronger support/resistance level than TPO POC.
- **Composite Profiles:** Aggregating profiles over weeks/months to identify long-term institutional "fair value" zones.

## 3. Spectral Analysis & Wave Theory
### Fourier & Wavelet Transforms
- **Fourier Analysis:** Extracting dominant market frequencies to identify cyclical signatures and filter high-frequency noise.
- **Wavelet Transforms:** Used for **Regime Detection**. Unlike Fourier, wavelets pinpoint *when* a frequency shift occurs, allowing for the detection of volatility clusters and structural breaks in real-time.
- **Denoising:** Applying optimal wavelet-based frameworks to boost signal stability without introducing the lag associated with traditional moving averages.
