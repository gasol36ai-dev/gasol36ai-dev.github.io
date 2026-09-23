---
title: 'Order Flow and Market Microstructure (2026 Frontier)'
description: 'Order flow trading analysis examines the real-time stream of buy and sell orders to reveal the buying and selling pressures that drive price…'
pubDate: 2026-05-15
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Order_Flow_Microstructure.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Order Flow and Market Microstructure (2026 Frontier)

## Overview
Order flow trading analysis examines the real-time stream of buy and sell orders to reveal the buying and selling pressures that drive price movements. Unlike traditional TA, it focuses on the **market microstructure**—the "how" and "why" of price movement rather than just the "what".

## Core Components
### 1. Depth of Market (DOM)
- **Definition**: A real-time view of pending limit orders on both sides of the book.
- **Insights**: 
    - **Imbalances**: Large clusters of orders at a specific price can indicate strong support/resistance.
    - **Spoofing**: Rapid cancellation of large orders to mislead other participants.
    - **Liquidity**: Wide spreads indicate high volatility; deep books suggest stability.

### 2. Footprint Charts (Cluster Charts)
- **Definition**: Visualizes volume traded at each price level within a single candle.
- **Insights**: 
    - **Aggression**: Shows whether buyers or sellers are more aggressive at the highs or lows of a candle.
    - **Imbalances**: Large disparities between buy and sell volume at a price level signal strong momentum.

### 3. Delta and Cumulative Delta
- **Delta**: The net difference between buy and sell volume for a given period.
- **Cumulative Delta**: The running total of Delta over time.
- **Divergence**: Price rising while Cumulative Delta is falling signals "hidden selling" and a likely reversal.

### 4. Market Profile & Value Areas
- **Market Profile**: Distributes price based on time spent at each price level.
- **Value Area (VA)**: The range where 70% of the volume occurred.
- **Point of Control (POC)**: The price level with the highest volume. POCs from previous sessions act as "magnets" for price.

## 2026 Advanced Strategies
- **Absorption Patterns**: When high volume is traded at a level without price moving, it signals institutional "absorption" of orders, often preceding a sharp reversal.
- **AI-Enhanced DOM**: Real-time automated detection of spoofing and institutional footprints using ML models.
- **Order Flow Imbalances**: The Federal Reserve (2025) noted that order flow imbalances amplify price movements in volatile markets (e.g., US Treasury markets).

## Application to Hermes Digital Organization
For the CTO's technical analysis of fund holdings (e.g., NVIDIA, Apple), integrating Order Flow data allows the agent to distinguish between a "retail-driven rally" and "institutional accumulation."
