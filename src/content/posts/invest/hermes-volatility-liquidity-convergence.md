---
title: 'Hermes Volatility-Liquidity Convergence Indicator (HVLC)'
description: 'The Hermes Volatility-Liquidity Convergence (HVLC) indicator is a proprietary judgment logic designed to identify "High-Conviction Reversals…'
pubDate: 2026-05-05
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_Volatility_Liquidity_Convergence.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Volatility-Liquidity Convergence Indicator (HVLC)

## 1. Concept & Logic
The **Hermes Volatility-Liquidity Convergence (HVLC)** indicator is a proprietary judgment logic designed to identify "High-Conviction Reversals" by analyzing the divergence between macro volatility and micro order flow.

### The Hypothesis
Traditional volatility indicators (e.g., ATR, VIX) are lagging. Real reversals are preceded by **Liquidity Absorption**, where price stops moving despite massive order flow (the "Absorption Wall").

### The Logic Gate
A **High-Conviction Reversal (HCR)** is signaled when:
1. **Macro Volatility is High** (Price is moving violently, VIX/ATR $\uparrow$).
2. **Micro Order Flow is Divergent** (Price hits a level, but Footprint Charts show massive volume *without* price movement $\rightarrow$ Absorption).
3. **Liquidity Sweep** (Price briefly pierces a known liquidity zone and immediately snaps back).

**Formula/Heuristic:**
$\text{Signal} = (\text{High Macro Vol}) \text{ AND } (\text{Price Stagnation} \mid \text{High Delta}) \text{ AND } (\text{Liquidity Sweep})$

## 2. Historical Pattern Application
- **The "Spring" Pattern**: In a downtrend, price crashes into a liquidity zone with high volatility, hits an "Absorption Wall" (massive buy orders absorbing all sells), and reverses.
- **The "Trap" Pattern**: Price breaks out of a range with high volatility, but Order Flow shows no follow-through (Delta $\downarrow$ while Price $\uparrow$), leading to a rapid reversal.

## 3. Strategic Implementation
- **Filter**: Use HVLC as a final filter for any long/short entry.
- **Action**: If HVLC = True, increase position size (High Conviction). If HVLC = False, use standard risk.

## 4. Verification Logic
To verify an HVLC signal:
- Check the 1-minute Footprint Chart for a "Zero-Print" or "Imbalance" at the extreme of the move.
- Confirm the Macro Regime is in a "Mean Reversion" or "Trend Exhaustion" state.
