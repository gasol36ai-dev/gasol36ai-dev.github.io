---
title: 'Hermes Regime Transition Index (HRTI)'
description: 'The Hermes Regime Transition Index (HRTI) is a proprietary judgment indicator designed to filter out "fakeouts" in trend-following strategie'
pubDate: 2026-05-14
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/HRTI.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Regime Transition Index (HRTI)

## Concept
The **Hermes Regime Transition Index (HRTI)** is a proprietary judgment indicator designed to filter out "fakeouts" in trend-following strategies by identifying the transition from a "Mean Reverting" regime to a "Trending" regime.

## Logic & Formula
The HRTI is a binary filter (0 or 1) based on the convergence of three distinct layers of data:

1. **Macro Regime (The 'What')**:
   - Condition: Real Yields $\downarrow$ AND VIX $\downarrow$.
   - Logic: Creates a "Risk-On" environment where trends are more likely to be sustained.

2. **Micro-Structure (The 'How')**:
   - Order Flow Absorption $\rightarrow$ Exhaustion transition.
   - Logic: We look for a "Squeeze" where price is consolidated in a tight Value Area (VA), and CVD starts to diverge from the price.

3. **Confirmation (The 'Trigger')**:
   - Condition: POC Migration $\uparrow$ (POC moves higher).
   - Logic: Market participants have collectively agreed on a new, higher "fair value."

### The HRTI Gate
$$\text{HRTI} = \begin{cases} 
1 & \text{if (Macro Risk-On) AND (CVD Divergence $\rightarrow$ POC Migration)} \\
0 & \text{if otherwise}
\end{cases}$$

## Historical Pattern Application
- **Scenario**: A bull market rally is starting.
- **False Positive**: Price breaks above a resistance level on low volume with CVD flat. HRTI = 0 (Fakeout).
- **True Positive**: Price consolidates, CVD diverges (buyers absorbing sellers), then POC shifts higher. HRTI = 1 (Regime Transition confirmed).

**Updated**: 2026-05-14
**Links**: [[Investment/Technical_Analysis/Order_Flow_Microstructure]]
