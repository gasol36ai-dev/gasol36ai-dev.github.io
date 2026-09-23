---
title: 'Hermes Liquidity Convergence Index (HLCI)'
description: 'The HLCI is a proprietary Hermes judgment indicator designed to identify high-probability reversal points by synthesizing auction structure,…'
pubDate: 2026-04-29
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/hermes-liquidity-convergence-index.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Liquidity Convergence Index (HLCI)

The HLCI is a proprietary Hermes judgment indicator designed to identify high-probability reversal points by synthesizing auction structure, order flow, and macro regime.

## Logic & Formula
The HLCI triggers when three distinct layers of convergence occur:

1. **Auction Layer (The "Where")**: Price is at a TPO Value Area Extreme (VAH or VAL) or a major High/Low Volume Node.
2. **Order Flow Layer (The "How")**: A clear **Delta Divergence** is observed. 
    - *Bullish HLCI*: Price creates a new low, but Delta is positive/increasing.
    - *Bearish HLCI*: Price creates a new high, but Delta is negative/decreasing.
3. **Regime Layer (The "When")**: Macro Volatility is in a "Mean Reversion" regime (e.g., VIX in a known range, not spiking).

$$	ext{HLCI Signal} = (	ext{Price\_at\_VA\_Extreme}) \cap (	ext{Delta\_Divergence}) \cap (	ext{Regime\_Filter})$$

## Historical Edge
This logic avoids "falling knife" scenarios by requiring both a structural anchor (TPO) and an execution-level reversal (Delta), filtered by the broader market regime. It provides an edge in Neutral and Normal Variation days, specifically at the boundaries of the Value Area.

See also: [[auction-market-theory]], [[market-microstructure]]
