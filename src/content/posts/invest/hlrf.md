---
title: 'Hermes Liquidity-Regime Filter (HLRF) v3.0'
description: 'The HLRF is a proprietary judgment gate that filters Order Flow signals based on the current Market World State. Version 3.0 evolves the fil'
pubDate: 2026-05-01
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/hlrf.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Liquidity-Regime Filter (HLRF) v3.0

## 1. Logic
The HLRF is a proprietary judgment gate that filters Order Flow signals based on the current **Market World State**. Version 3.0 evolves the filter from *static regime detection* to *predictive state divergence*, integrating "Next-State Prediction" logic from World Models.

## 2. World State Mapping & Predictive Divergence
Instead of simply identifying the current regime, HLRF v3.0 analyzes the **divergence** between the *Simulated World State* (Macro-sim) and the *Actual Order Flow* (Micro-execution).

| World State | Physics (Causal Link) | Regime Coefficient | Predictive Signal | Action |
| :--- | :--- | :--- | :--- | :--- |
| **Equilibrium** | Price $\approx$ Value; Mean Reversion dominates. | **1.0 (High)** | State Stability | Trade Mean Reversion |
| **Discovery** | Price $\neq$ Value; Trend/Momentum dominates. | **1.0 (High)** | State Extension | Trade Breakouts |
| **Fragile** | Low Liquidity; High sensitivity to Macro shocks. | **0.3 (Low)** | State Decay | Tight Stops / Reduce Size |
| **Pre-Shift** | World Model predicts transition; Order Flow lagging. | **2.0 (Alpha)** | **Synthetic Divergence** | **Golden Entry (Reversal)** |
| **Chaotic** | World Model Break; Correlations invert. | **0.1 (Trap)** | State Collapse | **NO TRADE** / Hedge Only |

## 3. The Heuristic
`Signal_Confidence = (Order_Flow_Intent * World_State_Coefficient) + Divergence_Bonus`

### State Identification:
- **Equilibrium**: POC is stable; VAH/VAL are respected.
- **Discovery**: Price stays outside Value Area; LVNs are breached aggressively.
- **Fragile**: High VIX + Low Volume at POC (Liquidity Vacuum).
- **Pre-Shift**: High-confidence World Model prediction of regime change (e.g., Yield shift) while Order Flow is still exhibiting peak trend-momentum (Synthetic Divergence).
- **Chaotic**: High VIX + Correlation Inversion + Delta Divergence across all timeframes.

## 4. Application
- **The Golden Entry**: Long if `World_State == Pre-Shift` AND `Order_Flow == Peak Exhaustion (Sells)`. This identifies the exact moment the "World State" shifts before the "Market" realizes it.
- **The Regime Trap**: If `Intent == Aggressive Buying` but `World_State == Chaotic`, the signal is flagged as a "Regime Trap" and ignored.
