---
title: 'The Convergence-Divergence Lock (CDL)'
description: 'Traditional technical analysis fails because it looks at indicators in a vacuum. The CDL is a proprietary logic gate that filters micro-sign…'
pubDate: 2026-05-21
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/hermes-cdl-indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# The Convergence-Divergence Lock (CDL)

## 1. Logic Hypothesis
Traditional technical analysis fails because it looks at indicators in a vacuum. The **CDL** is a proprietary logic gate that filters micro-signals through the lens of macro-regimes to distinguish between "True Trends" and "Institutional Traps."

## 2. The Framework: Map-Trigger-Lock

### Phase 1: Map (Macro Regime)
Identify the **Macro-Value Migration**. 
*   *Input:* Weekly Composite Market Profile + Macro Yield/Volatility Regime.
*   *State:* Is the macro-regime in **Expansion** (Value migrating) or **Contraction** (Value overlapping)?

### Phase 2: Trigger (Micro Signal)
Identify an **Aggressive Order Flow Imbalance**.
*   *Input:* 5-min Footprint Chart + Delta.
*   *Signal:* 3+ Stacked Imbalances or a sharp Delta spike.

### Phase 3: Lock (Confirmation)
The "Lock" occurs based on the **Convergence/Divergence** between Map and Trigger.

*   **The Convergence Lock (High Conviction):**
    *   `Macro: Value Migrating Higher` AND `Micro: Stacked Buy Imbalances` $\rightarrow$ **LOCK: Trend Confirmation**. 
    *   *Action:* Aggressive Long.

*   **The Divergence Lock (The Trap):**
    *   `Macro: Value Migrating Lower/Neutral` AND `Micro: Stacked Buy Imbalances` $\rightarrow$ **LOCK: Absorption Trap**.
    *   *Action:* Fade the imbalance (Short) once the "Lock" is confirmed by a reversal in Delta.

## 3. Expected Edge
The CDL prevents the common error of "buying the breakout" in a macro-neutral or bearish regime, which is where most retail "stacked imbalance" strategies fail. By requiring a **Convergence Lock**, the agent ignores 70% of micro-signals, focusing only on those aligned with institutional value migration.

## 4. Test Case (Hypothetical)
*   **Scenario:** Gold prices spike on a 5-min chart with massive positive delta.
*   **CDL Analysis:** 
    *   *Map:* Real Yields are rising $\rightarrow$ Macro Value for Gold is migrating lower.
    *   *Trigger:* Stacked buy imbalances.
    *   *Lock:* **DIVERGENCE**. This is an "Absorption Trap."
*   **Result:** Avoid long; seek short entry on the first negative delta flip.
