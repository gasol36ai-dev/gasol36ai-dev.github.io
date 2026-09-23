---
title: 'Institutional Order Flow & Liquidity'
description: 'Order Flow analysis is the study of the actual executed transactions and resting limit orders in the market. It reveals the "intent" of inst…'
pubDate: 2026-04-30
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Order-Flow.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Institutional Order Flow & Liquidity

Order Flow analysis is the study of the **actual executed transactions** and **resting limit orders** in the market. It reveals the "intent" of institutional players, which is often hidden from standard candlestick charts.

## Core Quantitative Tools

### 1. Footprint Charts (Cluster Charts)
Footprint charts show the volume traded at each specific price level within a candle.
- **Delta**: The difference between aggressive buyers (market buy) and aggressive sellers (market sell).
- **Cumulative Delta (CVD)**: The running total of delta over a period. A divergence between CVD and Price is a high-probability reversal signal.
- **Imbalances**: Occur when the aggressive buy volume at one price is significantly higher (e.g., 300%+) than the sell volume at the price above it. "Stacked Imbalances" indicate strong institutional conviction.

### 2. Liquidity & Inefficiency
Institutional traders create "holes" in the market when they move price aggressively.
- **Fair Value Gaps (FVG)**: A three-candle pattern where the wick of the first and third candles do not overlap, leaving a "gap" in the second candle. These are viewed as magnets that price typically returns to "fill" before continuing.
- **Liquidity Voids**: Areas of the order book with almost no resting limit orders, leading to rapid "slippage" and fast price movements.
- **Absorption**: When price hits a level and high volume occurs, but price fails to move further. This signals that a large limit order is "absorbing" all market aggression.

## Quantitative Implementation (2026)
Modern quant funds automate order flow detection using:
- **Tick-by-Tick Analysis**: Scanning the L2 order book for "spoofing" vs. genuine interest.
- **Delta Divergence Algorithms**: Automating the detection of "Price $\uparrow$ / CVD $\downarrow$" patterns.
- **FVG Clustering**: Identifying zones where multiple FVGs overlap, creating high-probability "Institutional Zones."

[[Market-Profile]], [[Hermes-Regime-Transition-Index]], [[quant]]
