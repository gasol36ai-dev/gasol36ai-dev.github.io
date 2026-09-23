---
title: 'Hermes Regime Filter (HRF)'
description: 'The Hermes Regime Filter (HRF) is a proprietary judgment indicator designed to determine whether a price move is driven by Fundamental Macro…'
pubDate: 2026-04-27
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/hermes-regime-filter.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Regime Filter (HRF)

The **Hermes Regime Filter (HRF)** is a proprietary judgment indicator designed to determine whether a price move is driven by **Fundamental Macro Logic** or **Internal Speculative Logic**.

## The Hypothesis
Technical indicators (Order Flow, Market Profile) provide high-alpha signals, but their reliability varies based on the underlying market regime. 
- In a **Fundamental Regime**, macro variables (e.g., Real Yields) dominate.
- In a **Speculative Regime**, internal liquidity and order flow dominate.

## The Logic
The HRF correlates the shift in a major asset's **Value Area (VA)** with the movement in **Real Yields**.

### Heuristic Formula
$$\text{HRF} = \frac{\Delta \text{Value Area}}{\Delta \text{Real Yields}} \times \text{Volatility Correction}$$

### Interpretation
| HRF Value | Regime | Dominant Driver | Strategy Priority |
|------------|---------|------------------|-------------------|
| **High** | Speculative | Internal Liquidity | $\rightarrow$ Prioritize Order Flow / Delta |
| **Low** | Fundamental | Macro Yields | $\rightarrow$ Prioritize Macro / Fund. Analysis |
| **Neutral** | Transition | Mixed | $\rightarrow$ Wait for confirmation |

## Historical Application
- **Gold (2024-2025)**: Observed periods where Gold rose despite rising Real Yields (High HRF). This signaled a "Systemic Trust" regime, making Order Flow signals significantly more reliable than Macro-Yield models.
- **BTC**: Often exhibits High HRF during "Retail Manias," where Macro ignores the move, and only Order Flow/Liquidity can time the peak.

[[order-flow-trading]], [[market-profile]], [[neowave]]
