---
title: 'Hermes Macro-Micro Convergence Oscillator (HMCO)'
description: 'The Hermes Macro-Micro Convergence Oscillator (HMCO) is a proprietary indicator designed to distinguish between "False Breakouts" (Absorptio…'
pubDate: 2026-05-01
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_Macro_Micro_Convergence_Oscillator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Macro-Micro Convergence Oscillator (HMCO)

## Concept
The **Hermes Macro-Micro Convergence Oscillator (HMCO)** is a proprietary indicator designed to distinguish between "False Breakouts" (Absorption) and "True Trends" (Convergence) by correlating high-frequency Order Flow Imbalance (OFI) with low-frequency Macro Regimes.

## The Core Hypothesis
Order Flow is the **Engine** (how it moves), but the Macro Regime is the **Fuel/Direction** (why it moves). 
- **Convergence**: When OFI aligns with the Macro Regime $\rightarrow$ High Probability Trend.
- **Absorption**: When OFI conflicts with the Macro Regime $\rightarrow$ Potential Reversal/Trap.

## Logic & Formula
### 1. The Micro Component: Normalized OFI ($\text{OFI}_n$)
$$\text{OFI}_n = \frac{\text{Current OFI} - \text{Avg OFI}(20)}{\text{StdDev OFI}(20)}$$
This centers the order flow imbalance to identify extremes.

### 2. The Macro Component: Alignment Score ($\text{MAS}$)
The Alignment Score is calculated based on the trend of key macro variables (e.g., US 10Y Yield, VIX, Dollar Index).
- $\text{MAS} = +1$ (Bullish Alignment)
- $\text{MAS} = -1$ (Bearish Alignment)
- $\text{MAS} = 0$ (Neutral/Conflicting)

### 3. The Oscillator: $\text{HMCO}$
$$\text{HMCO} = \text{OFI}_n \times \text{MAS}$$

## Interpretation Matrix

| HMCO Value | Market State | Actionable Insight |
| :--- | :--- | :--- |
| **Strong Positive** | **Convergence (Bullish)** | Macro and Micro are aligned. High confidence in long positions. |
| **Strong Negative** | **Convergence (Bearish)** | Macro and Micro are aligned. High confidence in short positions. |
| **$\text{OFI}_n$ High, $\text{HMCO}$ Low** | **Absorption (Bullish Trap)** | Massive buying into a bearish macro regime. Likely to be absorbed by institutional sellers. |
| **$\text{OFI}_n$ Low, $\text{HMCO}$ Low** | **Drift/Neutral** | Lack of conviction on both levels. Avoid trending strategies. |

## Testing Logic
To validate HMCO, test against historical "News Events" (CPI, FOMC). 
- **Hypothesis**: During CPI releases, the HMCO will signal the true direction faster than traditional indicators by identifying whether the initial spike is "Absorption" or "Convergence".
