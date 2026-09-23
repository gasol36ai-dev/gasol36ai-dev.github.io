---
title: 'Hermes Proprietary Indicators (v1.0)'
description: 'Hermes does not rely on single-variable indicators. Instead, we use Convergence/Divergence Filters that cross-pollinate Macro-Regime data wi…'
pubDate: 2026-05-20
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_Proprietary_Indicators.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Proprietary Indicators (v1.0)

## Philosophy
Hermes does not rely on single-variable indicators. Instead, we use **Convergence/Divergence Filters** that cross-pollinate Macro-Regime data with Micro-Order Flow.

## Indicator 1: The "Hermes Convergence Filter" (HCF)
**Hypothesis**: A price breakout is only a 'High Conviction' trend when the Micro-Order Flow (Tape Acceleration) and the Macro-Value Area (TPO Migration) align in the same direction.

**Logic**:
1. **Macro Condition (The Map)**: Market Profile shows the Value Area (VA) has migrated 3+ sessions in the direction of the break.
2. **Micro Condition (The Trigger)**: Order Flow detects "Tape Acceleration" (trades per second > 2x baseline AND average size > 1.5x baseline) within the breakout candle.
3. **Confirmation (The Lock)**: Volume Profile shows a "Low Volume Node" (LVN) being breached, indicated by rapid price movement.

**Judgment**:
- **Convergence (High Conviction)**: Macro VA Migration $\uparrow$ AND Tape Acceleration $\uparrow$ AND LVN Breach $\uparrow$ $\rightarrow$ **Strong Buy**.
- **Divergence (Trap/Absorption)**: Price breaks out $\uparrow$ BUT Tape Acceleration is absent OR Macro VA is stagnant $\rightarrow$ **Likely Bull Trap / Absorption**.

## Indicator 2: The "Institutional Vacuum Signal" (IVS)
**Hypothesis**: Extreme thinning of the order book (Liquidity Vacuum) is a leading indicator of volatility expansion, regardless of direction.

**Logic**:
1. **Baseline**: Track the trailing 15-minute average of resting limit orders within 1% of current price.
2. **Trigger**: Current resting orders drop by 70%+ relative to baseline.
3. **Action**: Set "Volatility Alert". The first aggressive market order (Tape Acceleration) in either 방향 (direction) will likely trigger a rapid expansion move.

**Judgment**:
- **IVS Triggered** $\rightarrow$ Prepare for breakout. Direction is determined by the first cluster of aggressive trades.
