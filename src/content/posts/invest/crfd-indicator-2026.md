---
title: 'Proprietary Indicator: Cross-Regime Flow-Volatility Divergence (CRFD)'
description: 'The CRFD indicator is designed to detect moments when market microstructure (local flow) becomes decoupled from macro-economic momentum (glo'
pubDate: 2026-05-26
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/CRFD_Indicator_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Cross-Regime Flow-Volatility Divergence (CRFD)

## Overview
The **CRFD** indicator is designed to detect moments when market microstructure (local flow) becomes decoupled from macro-economic momentum (global barometers), signaling a high-probability reversal or regime transition.

## Map-Trigger-Lock Framework

### MAP (The Divergence Quadrant)
The indicator maps the relationship between two orthogonal signals:
1. **Macro Momentum (MM)**: Derived from KOF Global Barometers (e.g., Asia-Pacific vs. Western Hemisphere divergence).
2. **Microstructure Imbalance (MI)**: Derived from VPIN and $\lambda$ (price impact) metrics.

**Quadrants**:
- **Congruent (Bullish/Bearish)**: MM and MI align (e.g., Global boom + high liquidity/low VPIN).
- **Divergent (Warning)**: MM suggests boom/downturn, but MI shows extreme imbalance or liquidity exhaustion (High VPIN/$\lambda$).

### TRIGGER (The Divergence Signal)
A signal is triggered when the **Divergence Coefficient ($\Delta$)** exceeds a threshold:
$$\Delta = |MM_{trend} - MI_{direction}| \times \text{Volatility\_Scaling}$$
- **Trigger**: $\Delta > \text{Threshold}$ AND $\text{VPIN} > \text{Critical\_Level}$

### LOCK (Adaptive Execution)
- **$\Delta$ High (Divergence Detected)**: **Lock** position sizing to 25% of normal levels. Prioritize "Liquidity-Taking" (aggressive) orders to capture the expected reversal.
- **$\Delta$ Low (Alignment)**: **Lock** full size. Prioritize "Liquidity-Providing" (passive) orders to capture the trend.

## Strategic Value
The CRFD provides a non-linear warning system for "trap" markets—where macro trends appear strong but the "plumbing" (microstructure) is failing, often preceding a violent breakdown.

*Updated: 2026-05-26*
