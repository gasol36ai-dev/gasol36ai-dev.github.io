---
title: 'Hermes Regime Transition Index (RTI)'
description: 'The RTI is a proprietary Hermes judgment indicator designed to distinguish between simple mean-reversion signals and genuine market regime s'
pubDate: 2026-04-28
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Regime-Transition-Index.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Regime Transition Index (RTI)

The RTI is a proprietary Hermes judgment indicator designed to distinguish between simple mean-reversion signals and genuine market regime shifts.

## Hypothesis
In high-volatility environments, standard mean-reversion (betting on a return to the Value Area) fails when aggressive order flow is absorbed by a new, dominant passive player. This signals the birth of a new "Fair Value" rather than a temporary excursion.

## Logic & Formula
The RTI is a synthetic score based on three variables:

1. **Relative VA Width (VAW)**: `Current VA Width / 20-Day Avg VA Width`.
2. **CVD Divergence (CVDD)**: Binary (1 if Price and CVD are diverging at a key level, 0 otherwise).
3. **Macro Volatility (MV)**: `VIX / 20-Day Avg VIX`.

**RTI Score** = `(VAW * 0.4) + (CVDD * 0.3) + (MV * 0.3)`

## Interpretation
- **RTI < 0.5**: Mean Reversion Regime. Standard Market Profile logic applies.
- **0.5 < RTI < 0.8**: Transition Zone. High uncertainty; tighten stops.
- **RTI > 0.8**: Regime Shift Regime. High probability of a breakout. **Do not fade the move**; follow the absorption side.

## Historical Pattern
During systemic trust crises (e.g., "Broken Correlation" events), the RTI typically spikes before the price breaks out of the Value Area, as the "Wall" (Absorption) is built before the move occurs.

See also: [[Order-Flow]]
