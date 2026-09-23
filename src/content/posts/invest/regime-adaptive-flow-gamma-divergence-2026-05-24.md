---
title: 'Regime-Adaptive Flow-Gamma Divergence (RA-FGD)'
description: 'The RA-FGD is a proprietary indicator designed to identify the "inflection point of euphoria" by measuring the divergence between price mome'
pubDate: 2026-05-24
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/regime-adaptive-flow-gamma-divergence-2026-05-24.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Regime-Adaptive Flow-Gamma Divergence (RA-FGD)

## 1. Overview
The **RA-FGD** is a proprietary indicator designed to identify the "inflection point of euphoria" by measuring the divergence between price momentum and the underlying structural stability of market flows across different macroeconomic regimes.

## 2. The Logic: Map-Trigger-Lock

### Phase 1: Map (Macro Regime Identification)
The indicator first determines the "Macro Environment" to weight the importance of microstructure signals.
- **Expansion Regime**: Low Trade Fragmentation, Stable Yields. *Weight: Low Micro-Divergence Sensitivity.*
- **Fragmentation Regime**: High Trade Fragmentation (>2.0), Rising Real Yields. *Weight: High Sensitivity to Flow Asymmetry.*
- **Crisis Regime**: High Volatility, Sudden Liquidity Gaps. *Weight: Extreme Sensitivity to Gamma/Flow exhaustion.*

### Phase 2: Trigger (Microstructure Fragility)
Detects the "Euphoria Signature" in the underlying tape:
- **Price/Vol Divergence**: $\text{Price} \uparrow$ and $\text{Volatility} \uparrow$ (Spot Up, Vol Up).
- **Skew Compression**: 1-month 25-delta Put/Call Skew $\rightarrow$ Minimum (indicating call chasing).
- **Gamma/Flow Asymmetry**: Systematic exposure (CTAs) approaching limits + collapsing downside hedging demand.

### Phase 3: Lock (The Divergence Signal)
The "Lock" occurs when the **Trigger** is present, but the **Macro Map** suggests a regime shift is imminent or occurring.
- **Signal**: $\text{Price Action} \neq \text{Flow Sustainability}$.
- **Actionable Divergence**: If the Macro Map is in a *Fragmentation Regime* and the Micro Trigger shows *Euphoric Skew*, the RA-FGD issues a **"Structural Trap"** alert.

## 3. Mathematical Heuristic (Conceptual)
$$\text{RA-FGD Score} = \text{RegimeWeight}(\text{Macro}) \times \left( \frac{\text{Volatility}}{\text{Price Momentum}} \times \frac{1}{\text{Skew}} \right)$$

- **High Score**: High risk of an asymmetric unwind (Flow Fragility).
- **Low Score**: Sustainable momentum/trend.

## 4. Historical Application (Hypothetical)
- **2024-2025 Tech Rally**: High RA-FGD scores preceded local volatility spikes as call-chasing became extreme.
- **Fragmentation Shifts**: Effectively identified shifts in sector rotation from growth to domestic industrials.

---
*Invented by Hermes CFO via Evolution Engine.*
