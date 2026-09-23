---
title: 'Quantitative Trading & Market Microstructure (2026 Frontier)'
description: 'Order flow is the study of "causes" (the actual orders) rather than "effects" (the resulting price candles).'
pubDate: 2026-05-19
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Quant_Microstructure.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Quantitative Trading & Market Microstructure (2026 Frontier)

## 1. Order Flow & Market Microstructure
Order flow is the study of "causes" (the actual orders) rather than "effects" (the resulting price candles).

### Key Metrics & Tools
- **Limit Order Book (LOB)**: The snapshot of intent.
- **Order Flow Imbalance (OFI)**: The net change in liquidity across time.
- ** uma Order Book Imbalance (OBI)**: Measures the directional edge (Professional target: $\approx 0.65$).
- **VPIN (Volume-synchronized Probability of Informed Trading)**: A "toxicity" filter. High VPIN ($\approx 0.8$) indicates informed traders are exploiting market makers.
- **Footprint Charts**: Volume breakdown per price level to identify absorption and aggression.
- **Delta Divergence**: Price rising while Delta (net buy/sell volume) falls $\rightarrow$ Hidden selling pressure/Reversal.

### Unified Theory of Order Flow (2026)
Recent research suggests a single structural parameter $H_0$ (persistence of core flow) determines:
- Signed order flow persistence.
- Roughness of traded volume and volatility.
- Price impact following a power law.

## 2. Market Profile (TPO)
Organizes trading activity into price distributions to identify "fair value" and "acceptance/rejection".

- **Value Area (VA)**: Where 70% of volume occurs.
- **Point of Control (POC)**: The price level with the most activity.
- **Convergence**: When LOB signals (micro) align with Market Profile Value Areas (macro) $\rightarrow$ High-probability trend.
- **Divergence**: When price is in a Value Area but LOB shows extreme imbalance $\rightarrow$ Potential trap/Absorption.

## 3. Advanced Wave Theory (NEoWave/Elliott)
Modern wave theory integrates volume and momentum (RSI) for structural timing.
- **Wave 3**: Highest volume, strongest momentum.
- **Wave 5**: Price makes higher highs, but RSI makes lower highs (Divergence) $\rightarrow$ Impulse end.
- **Fibonacci Targets**: Now reached more precisely due to algorithmic amplification of crowd psychology.

## Strategic Transmission Mapping
`[Order Flow Imbalance] $\rightarrow$ [Liquidity Vacuum/Absorption] $\rightarrow$ [Price Breakout/Reversal] $\rightarrow$ [Market Profile Value Area Shift]`
