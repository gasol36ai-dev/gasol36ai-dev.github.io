---
title: 'Hermes Macro-Micro Convergence (HMMC) Logic'
description: 'The HMMC framework is a proprietary judgment indicator designed to identify high-probability reversal or trend-acceleration zones by analyzi…'
pubDate: 2026-05-23
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/HMMC_Logic.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Macro-Micro Convergence (HMMC) Logic

The HMMC framework is a proprietary judgment indicator designed to identify high-probability reversal or trend-acceleration zones by analyzing the **divergence and convergence** between Macro-Regime state and Micro-Order Flow dynamics.

## 1. Theoretical Foundation
The logic rests on the observation that while macro variables (e.g., Yields, Oil) set the "gravitational field" (regime), the immediate price action is driven by Order Flow Imbalance (OFI). 

- **Convergence**: When macro-regime signals and micro-flow align $\rightarrow$ **Trend Confirmation** (High Conviction).
- **Divergence**: When micro-flow conflicts with the macro-regime $\rightarrow$ **Absorption/Trap Identification** (Reversal Potential).

## 2. The Map-Trigger-Lock Framework

To ensure determinism, HMMC uses a three-stage filter:

### Stage 1: Map (Macro Context)
**Objective**: Define the current Structural Regime.
- **Metric**: Macro Transmission Chain alignment (e.g., `[Energy Shock] -> [PPI \uparrow] -> [USD Resilience]`).
- **Regime State**: 
    - *Expansionary/Bullish*: Macro indicators supporting asset appreciation.
    - *Contractionary/Bearish*: Macro indicators supporting asset depreciation.
    - *Divergent/Fragile*: Macro indicators conflicting (e.g., Leading Barometer $\downarrow$ while Coincident $\uparrow$).

### Stage 2: Trigger (Micro Execution)
**Objective**: Identify the immediate flow signal.
- **Metric**: Order Flow Imbalance (OFI) and Market Profile TPO structure.
- **Signals**:
    - *Aggressive Flow*: High OFI in the direction of the Macro Map.
    - *Exhaustion Flow*: High OFI *against* the Macro Map at a Value Area boundary.
    - *Absorption*: Price stalls despite high directional OFI (the "Wall").

### Stage 3: Lock (Confirmation)
**Objective**: Filter out noise and "traps".
- **Metric**: Value Area Migration and POC Stability.
- **Confirmation**:
    - *Trend Lock*: POC migrates in the direction of the trigger $\rightarrow$ Confirm Trend.
    - *Reversal Lock*: Price breaches a "Poor Low/High" and the POC refuses to follow $\rightarrow$ Confirm Reversal.

## 3. HMMC Logic Gates

| Macro Map (Regime) | Micro Trigger (Flow) | Lock (Structure) | HMMC Judgment | Action |
| :--- | :--- | :--- | :--- | :--- |
| Bullish | Strong Buy OFI | POC Migrating $\uparrow$ | **Full Convergence** | Strong Long / Hold |
| Bullish | Strong Sell OFI | POC Static/Refusing $\downarrow$ | **Bullish Absorption** | Buy the Dip / Long |
| Bearish | Strong Sell OFI | POC Migrating $\downarrow$ | **Full Convergence** | Strong Short / Hold |
| Bearish | Strong Buy OFI | POC Static/Refusing $\uparrow$ | **Bearish Absorption** | Sell the Rip / Short |
| Fragile/Divergent | Any Strong Flow | Narrow IB / High Vol | **Regime Transition** | Reduce Size / Hedge |

## 4. Historical Edge & Validation
- **Edge**: Prevents "blindly" following order flow during macro regime shifts (e.g., the 2026 Energy Shock) where high-volume selling might be "absorbed" by institutional buyers repositioning for a new macro-trust regime.
- **Validation**: In "Fear Markets", HMMC identifies the "Price-Value Divergence" where price drops on retail panic (Micro Trigger) but Value Areas stay elevated (Macro Map), leading to high-probability reversal setups.
