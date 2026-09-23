---
title: 'Advanced Quantitative Trading (2026)'
description: 'Order flow is the study of market microstructure—the real-time stream of buy and sell orders that drive price movement.'
pubDate: 2026-05-17
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Quantitative_Trading_OrderFlow.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Advanced Quantitative Trading (2026)

## 1. Order Flow Analysis (The "Soil" of the Market)
Order flow is the study of market microstructure—the real-time stream of buy and sell orders that drive price movement.

### Core Metrics & Indicators
- **Limit Order Book (LOB)**: The "Battle of Intent." A snapshot of resting supply and demand.
- **Order Flow Imbalance (OFI)**: The net change in liquidity across time.
- **Order Book Imbalance (OBI)**: Ratio of bids to asks. A value > 0.65 typically indicates a short-term directional edge.
- **VPIN (Volume-synchronized Probability of Informed Trading)**: Measures "toxicity." When VPIN > 0.8, the market is considered toxic, and informed traders are exploiting market makers.
- **Delta**: The difference between market buy and market sell volume. 
- **Cumulative Delta**:Cumulative delta tracks this over time to confirm trend strength.
- **Absorption**: When high volume is traded without significant price movement, signaling institutional involvement.

### Tactical Application
- **LOB Shape Analysis**:
    - Heavy Bid / Thin Ask + Flat Price $\rightarrow$ Absorption (Buy for breakout).
    - Thin Bid / Heavy Ask + Rising Price $\rightarrow$ Liquidity Vacuum (Short for reversal).
- **Iceberg Detection**: Using transaction logs (Time & Sales) to detect hidden institutional algorithms.

## 2. Market Profile & Volume Profile
These tools organize trading activity by price rather than time.

### Market Profile (TPO)
- **Time Price Opportunity (TPO)**: Measures time spent at a price level.
- **Value Area (VA)**: The range where 70% of trading activity occurs (fair value).
- **Point of Control (POC)**: The price with the most time and volume spent.
- **Single Prints**: Price levels with minimal time/volume, often representing "unfair" prices that institutions later repair.

### Volume Profile (VP)
- **Superiority**: Volume reveals *conviction* (commitment), whereas time only reveals *presence*.
- **HVN (High Volume Node)**: Strong support/resistance (institutional positions).
- **LVN (Low Volume Node)**: Weak zones where price accelerates through.
- **P-shape / b-shape**: Indicate bullish/bearish sentiment.

## 3. Synthesis: The High-Resolution View
The most powerful edge comes from the confluence of structural support (Market Profile) and immediate supply/demand dynamics (Order Flow).
- **Strategy**: Identify a key level (HVN/POC) $\rightarrow$ Shift to Footprint charts $\rightarrow$ Confirm Absorption or Imbalance $\rightarrow$ Execute.
