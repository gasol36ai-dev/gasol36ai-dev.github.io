---
title: 'Frontier Quantitative Trading & TA (May 2026)'
description: 'The use of Adaptive Wavelet Networks (e.g., AdaWaveNet, WaveDSTN) has become critical for financial time series.'
pubDate: 2026-05-22
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Frontier_Quant_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Frontier Quantitative Trading & TA (May 2026)

## Wavelet-Based Non-Stationarity Handling
The use of **Adaptive Wavelet Networks** (e.g., AdaWaveNet, WaveDSTN) has become critical for financial time series.
- **Adaptive Wavelets**: Instead of fixed basis functions, learnable lifting operators are used to discover optimal multi-scale representations for non-stationary signals.
- **Multiscale Decomposition**: Separating "trend" from "fluctuation" allows for specialized modeling strategies for each component, reducing MSE in FX and equity markets.

## Neuro-Symbolic & Physics-Informed Finance
- **ARTEMIS**: Integrates Neural SDEs with **physics-informed losses** (Feynman-Kac PDE residuals) to enforce local no-arbitrage conditions.
- **Symbolic Bottleneck**: Distills continuous-time latent dynamics into human-readable, closed-form alpha factors, solving the "black box" problem of deep learning in finance.

## Order Flow & Fundamental Linkage
- **Information Aggregation**: Order flow is a superior predictor of future macro fundamentals (GDP, inflation) compared to spot rates.
- **Horizon Decay**: The association between order flow and returns is strongest at intraday/daily frequencies and weakens significantly beyond two weeks.
- **Liquidity Interaction**: The price impact of order flow is non-linear and weakest during periods of maximum market activity.

## Regime-Aware Forecasting
- **WaveESN-RegimeMLP**: Combines reservoir networks with HMM-based regime detection. Conditioning the final MLP on the inferred regime (from ESN residuals) significantly reduces RMSE during volatile transitions.
