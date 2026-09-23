---
title: 'Hermes Macro-Order Flow Convergence Oscillator (MOFCO)'
description: 'The Hermes Macro-Order Flow Convergence Oscillator (MOFCO) is a proprietary judgment indicator designed to detect "True Reversals" vs. "Fake…'
pubDate: 2026-05-13
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/MOFCO.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Macro-Order Flow Convergence Oscillator (MOFCO)

## Concept
The **Hermes Macro-Order Flow Convergence Oscillator (MOFCO)** is a proprietary judgment indicator designed to detect "True Reversals" vs. "Fakeouts" by measuring the convergence of Macro-fundamental drivers and Micro-order flow imbalances.

## Logic & Hypothesis
Most "fakeouts" occur when price breaks a level based on macro news, but the order flow (Delta/Footprint) shows **absorption** rather than **aggression**.

### Indicator Components
1. **Macro Divergence Score (MDS)**: 
   - Quantifies the strength of the macro driver (e.g., Interest Rate hike, GDP surprise).
   - Scale: -10 to +10.
2. **Order Flow Aggression Index (OFAI)**:
   - Measures the net Delta and Footprint imbalance.
   - Scale: -10 to +10.
3. **Convergence Factor (CF)**:
   - $CF = \text{sign}(\text{MDS}) \times \text{sign}(\text{OFAI})$
   - If $CF = 1$, the macro and micro signals are **convergent**. (High probability of trend continuation).
   - If $CF = -1$, they are **divergent**. (High probability of a "Fakeout" or reversal).

## Operational Rule
- **Strong Buy**: MDS > 2 AND OFAI > 2 AND CF = 1.
- **Strong Sell**: MDS < -2 AND OFAI < -2 AND CF = 1.
- **Trap Warning**: MDS is strong, but OFAI is opposite sign $\rightarrow$ High risk of absorption.

## Testing Logic (Historical Pattern)
- **Scenario**: High-impact news (MDS = +5) releases, price spikes up, but Footprint shows heavy selling at the top (OFAI = -3).
- **Result**: $CF = -1$. The MOFCO indicator would have flagged this as a "Trap" despite the positive news.
