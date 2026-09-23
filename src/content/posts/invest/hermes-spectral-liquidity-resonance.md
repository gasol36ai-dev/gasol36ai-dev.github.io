---
title: 'Proprietary Indicator: Hermes Spectral Liquidity Resonance (SLR)'
description: 'The Spectral Liquidity Resonance (SLR) indicator is a high-conviction judgment tool that synthesizes micro-structure order flow, spectral fr'
pubDate: 2026-05-16
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_Spectral_Liquidity_Resonance.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Hermes Spectral Liquidity Resonance (SLR)

## Concept
The **Spectral Liquidity Resonance (SLR)** indicator is a high-conviction judgment tool that synthesizes micro-structure order flow, spectral frequency analysis, and macro liquidity cycles.

## Logic Framework

### Component 1: Spectral Frequency Alignment ($\Phi$)
Using **Continuous Wavelet Transforms (CWT)**, the system identifies the dominant cyclical frequency of the current price regime. 
- **Resonance:** When the short-term cycle (intra-day) aligns in phase with the medium-term cycle (weekly).

### Component 2: Order Flow Imbalance Intensity ($\Omega$)
Measuring the **Net Liquidity Flow** (a weighted average of market and limit order flows).
- **Imbalance:** $\Omega > \text{threshold}$ indicates strong directional conviction.

### Component 3: Macro Liquidity Phase ($\Lambda$)
Tracking the global liquidity cycle (e.g., Central Bank balance sheets, Treasury General Account flows).
- **Expansion:** $\Lambda = 1$ (Bullish tailwind).
- **Contraction:** $\Lambda = -1$ (Bearish headwind).

## The SLR Formula (Conceptual)
$$SLR = (\Phi_{alignment} \times \Omega_{intensity}) \times \Lambda_{phase}$$

## Interpretation
- **High Positive SLR:** "Perfect Storm" for Longs. Spectral resonance + High Buy Imbalance + Macro Expansion.
- **High Negative SLR:** "Perfect Storm" for Shorts. Spectral resonance + High Sell Imbalance + Macro Contraction.
- **Low/Zero SLR:** "Noise Regime." No alignment between cycles and flow. Avoid high-leverage positions.

## Trading Application
- **Entry:** Trigger long when $SLR$ crosses a positive threshold while price is at a **Volume POC** support.
- **Exit:** Close when $\Phi_{alignment}$ breaks (frequency shift), suggesting the cycle has ended regardless of price level.
