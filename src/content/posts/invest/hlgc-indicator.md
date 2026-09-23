---
title: 'HLGC Indicator'
description: 'Market reversals typically occur when price enters a "Liquidity Gap" (a region where very little volume was traded) while simultaneously sho…'
pubDate: 2026-05-14
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/HLGC_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
## Indicator Logic: Hermes Liquidity Gap Convergence (HLGC)

### 1. The Hypothesis
Market reversals typically occur when price enters a "Liquidity Gap" (a region where very little volume was traded) while simultaneously showing a massive "Delta Divergence" (aggressive orders are hitting the market, but price is not moving).

### 2. The Components
- **Component A: Market Profile Gap (The Macro Filter)**
    - Identify "Single Prints" or "Low Volume Nodes (LVN)" in the Market Profile.
    - These are price levels that the market skipped through quickly, leaving a liquidity void.
- **Component B: Order Flow Delta Divergence (The Micro Trigger)**
    - Monitor the Delta at the edge of the Gap.
    - **Bullish HLGC**: Price enters a Low Volume Node from above, and we see a massive *positive* Delta (aggressive buying) but price stops falling.
    - **Bearish HLGC**: Price enters a Low Volume Node from below, and and we see a massive *negative* Delta (aggressive selling) but price stops rising.

### 3. The Signal
- **Convergence**: When Price is in a `Low Volume Node` AND `Delta Divergence > 2.0 Standard Deviations`.
- **Judgment**: "High-Probability Reversal Zone."
- **Action**: 
    - If Bullish HLGC $
ightarrow$ Long entry with stop just below the node.
    - If Bearish HLGC $
ightarrow$ Short entry with stop just below the node.

### 4. Historical Edge
This logic prevents "fighting the trend" by ensuring we only enter when the market has hit a structural void (the Gap) and an institutional agent has stepped in to absorb the move (the Delta Divergence).
