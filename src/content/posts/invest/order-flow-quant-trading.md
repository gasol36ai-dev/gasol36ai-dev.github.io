---
title: 'Advanced Order Flow & Quant Trading (2026)'
description: 'Order flow is the study of the actual buy and sell orders entering the market, focusing on the microstructure of the market rather than hist…'
pubDate: 2026-05-13
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Order_Flow_Quant_Trading.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Advanced Order Flow & Quant Trading (2026)

## 1. Order Flow Trading (OFT)
Order flow is the study of the actual buy and sell orders entering the market, focusing on the **microstructure** of the market rather than historical price patterns.

### Core Concepts
- **Depth of Market (DOM)**: The real-time view of pending limit orders. Used to identify imbalances, liquidity pockets, and "spoofing" (fake orders to mislead).
- **Footprint Charts**: Breakdown of volume within each candle by price level, showing buyer/seller aggression.
- **Delta Divergence**: When price rises but Delta (net difference between buy/sell volume) is negative, indicating hidden selling pressure (absorption).
- **Absorption**: Large volumes traded at a level without price movement, signaling institutional accumulation or distribution.

### 2026 Quant Trends
- **AI-Enhanced DOM**: Using ML to automatically detect patterns of institutional "footprints" in the real-time order book.
- **Cross-Asset Order Flow**: Monitoring liquidity supply and demand between correlated assets (e.g., S&P 500 ETF vs. E-mini Futures) to find lead-lag relationships and price discovery signals.
- **Order Flow Coherency**: The lead-lag effect of order flow changes on price changes, often stronger in medium-to-low frequency bands.

## 2. Market Profile & Volume Profile
- **Value Area (VA)**: The price range where 70% of the volume occurred.
- **Point of Control (POC)**: The price level with the highest traded volume.
- **High Volume Nodes (HVN)**: Areas of high acceptance; act as magnets or stability zones.
- **L-shaped/P-shaped Profiles**: Identify if the market is in a trend or a range.

## 3. Advanced Wave Theory
- **Quantitative Wave Analysis**: Moving from subjective "Elliott Wave" counting to algorithmic wave identification based on volatility and volume clusters.

## 4. Macro-Micro Convergence
- **Lead-Lag Relationship**: Order flow often reveals the impact of macro news *before* it is fully priced into the candle.
- **Order Flow as Private Information**: Order flow is a proxy for "private information" (informed traders), whereas macro news is "public information."
- **Volatility Link**: A positive relationship exists between the absolute value of order flow and volatility—higher order flow activity generally leads to higher volatility.
