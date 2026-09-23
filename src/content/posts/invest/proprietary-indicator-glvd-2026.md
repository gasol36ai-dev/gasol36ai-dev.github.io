---
title: 'Proprietary Indicator: Geometric Liquidity-Volatility Divergence (GLVD)'
description: 'The Geometric Liquidity-Volatility Divergence (GLVD) is a high-order synthesis indicator designed to detect the "phase transition" from stab…'
pubDate: 2026-05-26
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Proprietary_Indicator_GLVD_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Geometric Liquidity-Volatility Divergence (GLVD)

## 🧠 Overview
The **Geometric Liquidity-Volatility Divergence (GLVD)** is a high-order synthesis indicator designed to detect the "phase transition" from stable market regimes to chaotic, liquidity-starved environments. It moves beyond linear correlation by analyzing the *geometry* of the volatility-liquidity manifold.

## 🏗️ Framework (Map-Trigger-Lock)

### 1. Map (The Inputs)
The indicator maps three distinct dimensions into a single divergence score:
- **Dimension A: Macro Volatility State** ($V_{macro}$) 
    - *Source*: CBOE VIX or equivalent regime-adaptive volatility index.
- **Dimension B: Microstructure Liquidity Depth** ($L_{micro}$)
    - *Source*: Order book depth (top 5 levels) and bid-ask spread volatility across major liquid venues.
- **Dimension C: Order Flow Kinetic Energy** ($K_{flow}$)
    - *Source*: Aggressiveness of market orders (hitting bid/ask) relative to passive limit order replenishment.

### 2. Trigger (The Signal)
A **GLVD Signal** is triggered when the following geometric condition is met:
$$\text{GLVD} = \frac{\Delta V_{macro}}{\Delta L_{micro}} \cdot K_{flow} > \text{Threshold}_{\text{crit}}$$

**Visualizing the Trigger**:
- In a "Normal" regime: Volatility and Liquidity move in tandem (High $L$ during High $V$).
- In a "GLVD" regime: Volatility spikes while Liquidity *contracts* geometrically, accompanied by high-kinetic, unidirectional order flow.

### 3. Lock (The Reaction)
Upon a GLVD signal, the system executes the following deterministic protocols:
- **Protocol 1: Risk De-leveraging**: Immediate 30% reduction in all directional exposure (Risk Budget $\rightarrow$ 0.7x).
- **Protocol 2: Liquidity Buffer Expansion**: Increase cash/stablecoin reserves by 15% to ensure operational continuity during volatility spikes.
- **Protocol 3: Alpha Guard**: Suspend all "High-Frequency/Low-Margin" strategies that rely on tight spreads.

## 💡 Strategic Value
The GLVD provides a **non-linear early warning system**. Unlike standard volatility measures, it identifies when volatility is becoming "expensive" (due to lack of liquidity), allowing for defensive positioning *before* the liquidity vacuum causes a catastrophic price move.

---
**Validation Status**: Hypothesized (Requires historical backtesting against 2024-2026 liquidity events).
**Iteration**: 1.0
