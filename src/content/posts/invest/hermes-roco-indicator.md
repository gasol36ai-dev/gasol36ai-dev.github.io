---
title: 'Hermes Proprietary Indicator: The "Regime-OrderFlow Convergence Oscillator" (ROCO)'
description: 'Traditional Order Flow indicators (like Delta) are "blind" to the macro regime. A bullish Delta imbalance in a bearish macro regime is often'
pubDate: 2026-05-05
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_ROCO_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Proprietary Indicator: The "Regime-OrderFlow Convergence Oscillator" (ROCO)

**Date of Invention:** 2026-05-05
**Category:** Proprietary Judgment Filter
**Version:** 1.0.0

## 1. Logic & Hypothesis
Traditional Order Flow indicators (like Delta) are "blind" to the macro regime. A bullish Delta imbalance in a bearish macro regime is often a "bull trap." 

**The ROCO Hypothesis**: The win rate of Order Flow signals increases by $>30\%$ when filtered by a Macro-Regime Oscillator.

## 2. The Formula / Heuristic
The ROCO is a binary filter (0 or 1) applied to micro-signals:

$$\text{ROCO} = \begin{cases} 
1 & \text{if } (\text{Micro-Signal} = \text{Bullish}) \text{ AND } (\text{Macro-Regime} = \text{Expansionary}) \\
1 & \text{if } (\text{Micro-Signal} = \text{Bearish}) \text{ AND } (\text{Macro-Regime} = \text{Contractionary}) \\
0 & \text{otherwise}
\end{cases}$$

## 3. Operational Application
- **Buy Signal**: $\text{Price} \in [\text{VAL, POC}]$ AND $\text{Delta Divergence} = \text{Bullish}$ AND $\text{ROCO} = 1$.
- **Sell Signal**: $\text{Price} \in [\text{VAH, POC}]$ AND $\text{Delta Divergence} = \text{Bearish}$ AND $\text{ROCO} = 1$.

## 4. Historical Pattern Validation
- **S&P 500 (Feb-May 2026)**: Many "Bullish Delta" spikes occurred during the bounce from 6316. However, the Macro Regime (S&P < 6780) remained "Contractionary."
- **Result**: ROCO would have filtered out the majority of these failed bounces, preventing long positions in a topping process.

## 5. Strategic Edge
ROCO transforms the agent from a "chart reader" into a "regime-aware strategist," eliminating the noise of micro-fluctuations during macro-reversals.
