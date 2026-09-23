---
title: 'Hermes Divergence-Flow Nexus (DFN)'
description: 'The Hermes Divergence-Flow Nexus (DFN) is a proprietary judgment framework designed to filter micro-structural price signals through the len…'
pubDate: 2026-05-23
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/hermes-divergence-flow-nexus.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Divergence-Flow Nexus (DFN)

## Overview
The **Hermes Divergence-Flow Nexus (DFN)** is a proprietary judgment framework designed to filter micro-structural price signals through the lens of the current **Macro Transmission Regime**. 

The DFN solves the "False Breakout" problem by identifying **Sovereign Traps**—situations where micro-level order flow suggests a trend reversal, but the underlying macro-transmission mechanisms (e.g., the Energy-Inflation-Growth Loop) remain fundamentally opposed to that move.

## Logic Framework: Map-Trigger-Lock

The DFN operates as a deterministic filter for execution:

### 1. Map (Macro Regime Alignment)
**Condition**: $\text{Transmission-Consistency Check}$
- **Action**: Compare the current asset move against the active transmission chains in `[[macro-transmission-2026]]`.
- **Categories**:
    - **Pro-Regime**: The move aligns with the macro-transmission (e.g., USD $\uparrow$ during EU stagflation).
    - **Contra-Regime**: The move opposes the macro-transmission (e.g., EUR $\uparrow$ while Energy prices are spiking and EU growth is decelerating).
- **Role**: Sets the **Probabilistic Bias**. Contra-Regime moves are treated as "Fragile" and subject to higher scrutiny.

### 2. Trigger (Micro Signal)
**Condition**: $\text{Structural Breakout + Flow Imbalance}$
- **Signal**: 
    1. Price breaks and holds outside the previous session's TPO Value Area ($\text{Price} > \text{VAH}$ or $\text{Price} < \text{VAL}$).
    2. Order Flow Imbalance (OFI) exceeds $2\sigma$ relative to the 20-day moving average.
- **Role**: The **Execution Trigger**. This identifies that a move is occurring with significant institutional participation.

### 3. Lock (Confirmation/Filter)
**Condition**: $\text{Delta-Regime Convergence}$
- **Scenario A: Pro-Regime $\rightarrow$ Delta Convergence**
    - Signal: $\text{Price} \uparrow$ and $\text{Cumulative Delta} \uparrow$ (Aggressive buying supporting the move).
    - **Result**: **"Transmission Wave"** $\rightarrow$ High-Conviction Entry.
- **Scenario B: Contra-Regime $\rightarrow$ Delta Divergence**
    - Signal: $\text{Price} \uparrow$ but $\text{Cumulative Delta} \downarrow$ (Price is being pushed up by a lack of liquidity/stop-runs, not by aggressive buying).
    - **Result**: **"Sovereign Trap"** $\rightarrow$ High-Conviction Fade (Short).
- **Scenario C: Contra-Regime $\rightarrow$ Delta Convergence**
    - Signal: $\text{Price} \uparrow$ and $\text{Cumulative Delta} \uparrow$.
    - **Result**: **"Regime Shift Warning"** $\rightarrow$ Avoid trade; macro-transmission may be evolving.

## Convergence vs. Divergence Lens

| State | Macro (Transmission) | Micro (Order Flow) | Result | Action |
| :--- | :--- | :--- | :--- | :--- |
| **Convergence** | Pro-Regime | Convergent (Aligned) | **Transmission Wave** | Aggressive Entry |
| **Divergence** | Contra-Regime | Divergent (Opposed) | **Sovereign Trap** | Aggressive Fade |
| **Conflict** | Contra-Regime | Convergent (Aligned) | **Regime Shift** | Neutral / Observation |
| **Noise** | Pro-Regime | Divergent (Opposed) | **Liquidity Gap** | Scalp Only |

## Strategic Value
The DFN prevents "fighting the macro" during temporary micro-spikes. In the context of "The Great Divergence," it allows Hermes to distinguish between a genuine recovery in European assets and a temporary "short-squeeze" that is fundamentally unsupported by the energy-security asymmetry.
