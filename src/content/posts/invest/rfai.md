---
title: 'Hermes Proprietary Indicator: Regime-Filtered Absorption Index (RFAI)'
description: 'The RFAI is a filter designed to increase the win rate of Order Flow reversal trades by gating them through a Macro Volatility regime.'
pubDate: 2026-05-01
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/RFAI.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Proprietary Indicator: Regime-Filtered Absorption Index (RFAI)
**Updated:** 2026-05-01
**Category:** Investment/Technical_Analysis/Innovation

## Logic
The RFAI is a filter designed to increase the win rate of Order Flow reversal trades by gating them through a Macro Volatility regime.

## Hypothesis
Order Flow divergences (Price vs. Cumulative Delta) are ambiguous. 
- In **Low Volatility regimes**, divergences typically signal **Absorption** (genuine reversals).
- In **High Volatility regimes**, divergences typically signal **Traps** (trend continuation despite aggressive counter-participation).

## Formula / Heuristic
`RFAI Signal = (OrderFlow_Divergence) AND (Macro_Volatility_Regime)`

| Macro Regime | Order Flow Signal | RFAI Interpretation | Action |
| :--- | :--- | :--- | :--- |
| **Low Volatility** | Divergence | **Absorption** | Trade Reversal |
| **High Volatility** | Divergence | **Trap/Squeeze** | Avoid Reversal / Trend Follow |

## Historical Pattern Validation
- **Range-bound markets**: RFAI identifies the "edge" of the range where aggressive sellers are absorbed by passive buyers, leading to high-probability bounces.
- **Trending/Volatile markets**: RFAI prevents "catching the falling knife" by identifying that aggressive buying into a crash is being absorbed by larger institutional sell-orders (The Trap).
