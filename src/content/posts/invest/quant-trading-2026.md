---
title: 'Advanced Quantitative Trading: Order Flow & Market Profile (2026)'
description: 'Order flow is the study of the actual transactions occurring in the market, moving beyond lagging indicators to real-time supply and demand.'
pubDate: 2026-05-04
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Quant_Trading_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Advanced Quantitative Trading: Order Flow & Market Profile (2026)

## 1. Order Flow Analysis
Order flow is the study of the *actual* transactions occurring in the market, moving beyond lagging indicators to real-time supply and demand.

### Core Tools
- **Footprint Charts**: Displays the volume transacted at each price level within a candle, revealing "imbalances" (e.g., when buy volume significantly exceeds sell volume at a specific price).
- **Delta**: The net difference between aggressive buyers and aggressive sellers.
- **CVD (Cumulative Volume Delta)**: The running total of delta over time. Divergence between CVD and Price is a high-probability signal for trend exhaustion or absorption.

### High-Probability Patterns
- **Absorption**: When price hits a level and high volume occurs, but price fails to move further. This indicates a "hidden" institutional player absorbing all market orders.
- **Aggressive Initiation**: A surge in delta accompanying a price breakout, confirming the move is driven by institutional aggression.

## 2. Market Profile & Auction Market Theory (AMT)
AMT posits that the market's primary purpose is to facilitate trade by finding a "fair price."

### Key Concepts
- **Value Area (VA)**: The price range where 70% of the volume occurred. Inside the VA, the market is "balanced"; outside the VA, it is "imbalanced" (trending).
- **Point of Control (POC)**: The price level with the highest volume. Acts as a magnetic level.
- **Initial Balance (IB)**: The range of the first hour of trading, often setting the tone for the session.

### Strategic Application
- **Value Area Shift**: When the POC moves higher/lower and the VA shifts, it confirms a change in the fair value perception.
- **Mean Reversion**: Price opening outside the VA and returning to it often signals a "failure to trend."

## 3. The Convergence Framework
**Convergence** occurs when Order Flow signals align with Market Profile levels.
- *High Conviction Setup*: Price reaches a previous day's POC $\rightarrow$ Footprint shows absorption $\rightarrow$ CVD shows bullish divergence $\rightarrow$ Price reverses.

## Related Concepts
- [[Order-Flow]]
- [[Market_Profile]]
- [[Auction_Market_Theory]]
