---
title: 'Frontier Quant & Order Flow Trading (2026)'
description: 'Last Updated: 2026-05-19'
pubDate: 2026-05-19
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Frontier_Quant_2026_Update.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Frontier Quant & Order Flow Trading (2026)
Last Updated: 2026-05-19

## 1. Market Microstructure: The Study of Causes
Traditional TA studies *effects* (candles); Microstructure studies *causes* (the Limit Order Book - LOB).
- **Order Book Imbalance (OBI)**: A primary lead indicator for short-term directional edge.
- **VPIN (Volume-synchronized Probability of Informed Trading)**: Used to detect "Toxic Flow" (informed traders exploiting market makers).
    - *Protocol*: When VPIN > 0.8, cancel open limit orders to avoid being "picked off."
- **Liquidity Holes**: Rapid thinning of LOB depth (>70% in <60s) signals an emergency state and potential flash crash.

## 2. Auction Market Theory (AMT) & Market Profile
The "Why" behind price movement.
- **TPO (Time Price Opportunity)**: Organizes data by time to reveal the "fairest" price (Point of Control - POC).
- **Value Area (VA)**: The range where 70% of activity occurs.
- **Super POC**: Convergence of TPO POC and Volume POC; acts as a massive price magnet.
- **Session Types**:
    - *Trend Day*: Narrow, elongated profile.
    - *Normal Variation*: Initial Balance (IB) established, then expanded.
    - *Neutral Day*: D-shaped profile; price rotates back to POC.

## 3. Order Flow Integration (The "Forensic" Layer)
Combining structural context (Market Profile) with execution data (Order Flow).
- **Footprint Charts**: Breaking down volume by price to detect buy/sell aggression.
- **Absorption**: Large volume traded without price movement $\rightarrow$ Institutional involvement.
- **Delta Divergence**: Rising price with negative delta $\rightarrow$ Hidden selling pressure/reversal signal.
- **Iceberg Detection**: Using T&S (Time and Sales) logs to detect hidden institutional POV algorithms (e.g., constant size every 1.25s).

## 4. Synthesis: Structural + Immediate Dynamics
The highest probability setups occur at the confluence of:
- **Structural Support/Resistance** (Market Profile VA/POC) $\cap$ **Immediate Demand/Supply** (Order Flow Imbalances/Absorption).
