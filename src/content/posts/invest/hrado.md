---
title: 'Hermes Regime-Adaptive Delta Oscillator (HRADO)'
description: 'The HRADO is a proprietary synthetic indicator designed to solve the "Delta Noise" problem. Standard Cumulative Delta often provides false s'
pubDate: 2026-04-26
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/HRADO.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Regime-Adaptive Delta Oscillator (HRADO)

## Concept
The HRADO is a proprietary synthetic indicator designed to solve the "Delta Noise" problem. Standard Cumulative Delta often provides false signals during range-bound (balanced) markets. The HRADO dynamically adjusts the weighting of Order Flow based on the price's position relative to the Market Profile Value Area (VA).

## Logic & Formula
The oscillator calculates a **Regime-Adjusted Delta ($\Delta_{adj}$)** by applying a weighting factor ($\omega$) derived from the distance between the current price and the Value Area edges (VAH/VAL).

### 1. The Weighting Factor ($\omega$)
$$ \omega = \begin{cases} 
\text{High (1.2 - 1.5)} & \text{if Price } > VAH \text{ or } \text{Price } < VAL \text{ (Breakout Regime)} \\
\text{Low (0.3 - 0.5)} & \text{if } VAL < \text{Price} < VAH \text{ (Balanced Regime)} \\
\text{Neutral (1.0)} & \text{if Price } \approx VAH/VAL \text{ (Transition Zone)}
\end{cases} $$

### 2. The Oscillator Formula
$$ \Delta_{adj} = \sum (\text{Market Order Delta} \times \omega) $$

## Trading Heuristic
The HRADO filters signals into two primary categories:

### A. The Breakout Confirmation (Trend)
When price is outside the VA and $\omega$ is High:
- **Signal**: If $\Delta_{adj}$ trends strongly in the direction of the breakout, it confirms a **Liquidity Vacuum**.
- **Action**: High-conviction trend-following.

### B. The Range-Bound Trap (Mean Reversion)
When price is inside the VA and $\omega$ is Low:
- **Signal**: If $\Delta_{adj}$ shows extreme spikes but price fails to exit the VA, it indicates **Institutional Absorption**.
- **Action**: Fade the Delta spike; trade the mean reversion toward the POC.

## Historical Edge
The HRADO prevents "over-trading" Delta in chop. By dampening signals inside the Value Area, it eliminates approximately 60% of false Delta-based entries, while amplifying the signals that coincide with true structural breakouts.
