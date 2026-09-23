---
title: 'Hermes Absorption-Volatility Divergence (HAVD)'
description: 'The HAVD is a proprietary Hermes judgment indicator designed to filter low-probability reversal signals in Order Flow trading by integrating…'
pubDate: 2026-05-01
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_Absorption_Volatility_Divergence.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Absorption-Volatility Divergence (HAVD)

## Concept
The HAVD is a proprietary Hermes judgment indicator designed to filter low-probability reversal signals in Order Flow trading by integrating macro-volatility regimes.

## The Logic
The core hypothesis is that **Absorption** signals are not created equal; their reliability is a function of the current volatility regime.

### The HAVD Formula / Heuristic
`Signal = (Regime == HIGH_VOL) AND (Location == VA_BOUNDARY) AND (Sensation == ABSORPTION)`

### Components
1. **Regime (Macro Volatility)**: Measured via VIX or Real Yield volatility.
   - **High Vol**: Markets are characterized by high noise, deep liquidity hunts, and emotional extremes.
   - **Low Vol**: Markets are characterized by steady trends and minimal noise.
2. **Location (Market Profile)**: The price must be at the edge of the **Value Area (VA)** or at a major **Point of Control (POC)**.
3. **Sensation (Order Flow)**: A clear **Absorption** event is detected (CVD surges, but price remains flat/rejects).

## Why this works (Transmission Mechanism)
In low-volatility regimes, a flat price with high CVD might just be a temporary pause. However, in **High Volatility** regimes, the "noise" is so great that for price to remain flat despite massive aggressive volume, it requires a **massive institutional limit order** (a "Hard Wall"). 

The divergence between the aggressive macro-volatility "push" and the micro-structural "wall" creates a high-probability reversal edge.

## Historical Pattern
- **Scenario**: VIX spikes $\rightarrow$ Price crashes into the Lower Value Area boundary $\rightarrow$ Massive positive CVD surge (aggressive dip buyers) $\rightarrow$ Price remains flat for 15 mins $\rightarrow$ **Result**: Sharp V-bottom reversal.

[[Order_Flow]], [[Market_Profile]]
