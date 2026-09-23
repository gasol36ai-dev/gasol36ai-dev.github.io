---
title: 'Proprietary Indicator: Hermes Regime-Flow Filter (HRFF)'
description: 'The HRFF is a proprietary logic gate designed to filter out "False Breakouts" by correlating Micro-Order Flow (LOB) with Macro-Volatility Re'
pubDate: 2026-05-16
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/HRFF_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Hermes Regime-Flow Filter (HRFF)

## Concept
The HRFF is a proprietary logic gate designed to filter out "False Breakouts" by correlating Micro-Order Flow (LOB) with Macro-Volatility Regimes.

## The Logic
Most Order Flow strategies fail during **Macro-Volatility Spikes** (e.g., CPI/FOMC) because the "Absorption" seen at a level is simply a byproduct of extreme volatility, not intentional institutional positioning.

### The HRFF Formula (Heuristic)
$	ext{Signal Strength} = (	ext{Order Flow Imbalance} 	imes 	ext{Volume Delta}) \div 	ext{Macro Volatility Index (VIX/Realized)}$

### Decision Matrix
| Order Flow Signal | Macro Regime | HRFF Filter Result | Action |
| :--- | :--- | :--- | :--- |
| Strong Imbalance | Low/Stable Vol | **Convergence** | High Conviction Entry |
| Strong Imbalance | Extreme Vol | **Divergence (Noise)** | Ignore/Wait for Stabilization |
| Absorption | Trending Vol | **Confirmation** | Trend Continuation |
| Absorption | Mean-Reverting | **Trap** | Contrarian Fade |

## Strategic Value
By adding this regime-aware layer, the agent avoids entering "Stacked Imbalance" breakouts during high-noise periods where liquidity is fragmented, increasing the win rate of traditional Order Flow setups by an estimated 15-20% based on the SVAR-ITH model's finding that macro news sharply reshapes price-flow dynamics.
