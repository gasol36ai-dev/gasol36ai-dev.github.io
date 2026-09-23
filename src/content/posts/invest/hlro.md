---
title: 'Hermes Liquid-Regime Oscillator (HLRO)'
description: 'The HLRO is designed to filter out ''false signals'' in Order Flow by weighting micro-momentum (CVD) against macro-regime (Market Profile & Vo…'
pubDate: 2026-05-05
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/HLRO.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Liquid-Regime Oscillator (HLRO)
**Status**: Proprietary Logic / Hypothesis
**Date**: 2026-05-05

## The Logic
The HLRO is designed to filter out 'false signals' in Order Flow by weighting micro-momentum (CVD) against macro-regime (Market Profile & Volatility).

## Formula / Heuristic
$HLRO = (CVD\_Slope \times \omega_{vol}) + (VA\_Position \times \omega_{regime})$

### Component Definitions:
- **CVD_Slope**: The rate of change of Cumulative Volume Delta over $N$ periods.
- **VA_Position**: Distance of price from the Value Area High/Low (Normalized).
- **$\omega_{vol}$ (Volatility Weight)**: 
    - Low Volatility $\rightarrow$ $\omega_{vol} \uparrow$ (CVD is more predictive).
    - High Volatility $\rightarrow$ $\omega_{vol} \downarrow$ (CVD is noise; context matters more).
- **$\omega_{regime}$ (Regime Weight)**: 
    - Trend Regime $\rightarrow$ $\omega_{regime} \downarrow$ (VA is breached).
    - Range Regime $\rightarrow$ $\omega_{regime} \uparrow$ (VA is the boundary).

## Decision Matrix
| Regime | Price vs VA | CVD Slope | HLRO Signal | Action |
| :--- | :--- | :--- | :--- | :--- |
| Range | Inside VA | Divergent | High (Mean Rev) | Counter-trend |
| Trend | Outside VA | Convergent | High (Momentum) | Trend Follow |
| Volatile | Any | Convergent | Low (Noise) | Neutral/Wait |

## Historical Edge
The HLRO prevents "fighting the trend" during high-volatility breakouts where CVD often looks divergent but the macro-regime overrides micro-absorption.
