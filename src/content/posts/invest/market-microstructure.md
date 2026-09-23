---
title: 'Market Microstructure & Order Flow'
description: 'Market Microstructure is the study of the mechanics behind price movements—specifically how volume, aggressive orders, and institutional act'
pubDate: 2026-04-29
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/market-microstructure.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Market Microstructure & Order Flow

Market Microstructure is the study of the mechanics behind price movements—specifically how volume, aggressive orders, and institutional activity shape the market in real time.

## Order Flow Analysis Tools
- **DOM (Depth of Market)**: A real-time list of pending limit orders. Reveals liquidity walls and institutional intent.
- **Footprint Charts**: Displays executed buy and sell volume at each price level within a candle.
    - **Delta**: The net difference between buying and selling pressure ($	ext{Delta} = 	ext{Buy Vol} - 	ext{Sell Vol}$).
    - **Absorption**: When high volume occurs at a price level but price fails to break, signaling a strong counter-force.
    - **Initiation**: Large volumes driving rapid price movements.
- **Delta Divergence**: A critical reversal signal where price moves in one direction while Delta moves in the opposite.

## Institutional Activity
- **Iceberg Orders**: Large orders broken into smaller pieces to hide total size.
- **Smart Tape**: Filtering for large block trades to identify institutional footprints.

See also: [[auction-market-theory]], [[hermes-liquidity-convergence-index]]
