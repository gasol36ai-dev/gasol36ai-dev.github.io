---
title: 'Proprietary Indicator: The Hermes Liquidity-Regime Convergence (LRC) Index'
description: 'Version: 1.0'
pubDate: 2026-05-19
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_LRC_Index.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: The Hermes Liquidity-Regime Convergence (LRC) Index
Version: 1.0
Date: 2026-05-19

## 1. Logic & Hypothesis
Traditional indicators fail because they are regime-agnostic. The LRC Index hypothesizes that the reliability of a micro-signal (Order Flow) is a function of the macro-regime (Volatility/Liquidity).

**Core Thesis**: A "Liquidity Vacuum" in the macro-regime amplifies the predictive power of "Order Book Imbalance" (OBI) while rendering "Value Area" (VA) rotations irrelevant.

## 2. The Formula/Heuristic
The LRC Index is a composite score:
$$LRC = (OBI_{strength} \times \text{LOB}_{depth\_slope}) \div \text{VPIN}_{toxicity}$$

- **High LRC (> 0.7)**: High-conviction directional move. The market is "efficiently" moving toward a new value area.
- **Low LRC (< 0.3)**: "Toxic" or "Synthetic" environment. High probability of spoofing or HFT-driven noise.
- **LRC Divergence**: Price rising but LRC falling $\rightarrow$ "Absorption Trap." Institutional distribution is occurring under the guise of a trend.

## 3. Operational Guardrails
- **The Toxicity Stop**: If $VPIN > 0.8$ AND $LRC < 0.4$, immediately exit all delta-positive positions.
- **The Breakout Filter**: Only take breakouts from the Initial Balance (IB) if $LRC > 0.6$ at the moment of the breach.

## 4. Historical Pattern Validation
- **Flash Crashes**: Characterized by a precipitous drop in LRC (due to LOB depth collapse) *before* the price cliff.
- **Institutional Accumulation**: Characterized by a "flat" LRC despite rising volume, signaling heavy absorption at the POC.
