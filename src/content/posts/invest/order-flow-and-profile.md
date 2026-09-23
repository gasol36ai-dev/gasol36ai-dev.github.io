---
title: 'Advanced Order Flow & Market Profile'
description: 'Effective quantitative trading in 2026 relies on the intersection of three data streams:'
pubDate: 2026-05-05
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Order_Flow_and_Profile.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Advanced Order Flow & Market Profile
**Last Updated:** 2026-05-05

## Core Framework: The Confluence Triad
Effective quantitative trading in 2026 relies on the intersection of three data streams:

1. **Market Profile (The Map)**:
    - **Value Area (VA)**: Where 70% of volume occurs. Price inside VA = Balance; outside = Imbalance.
    - **Low Volume Nodes (LVN)**: Areas of rejection; often act as strong support/resistance.
2. **Order Flow / CVD (The Engine)**:
    - **Cumulative Volume Delta (CVD)**: Tracks net aggression (Market Buys - Market Sells).
    - **CVD Divergence**: Price makes a new high, but CVD fails to do so $\rightarrow$ Absorption (Bearish).
3. **VWAP (The Anchor)**:
    - The institutional average price. Deviation from VWAP combined with CVD signals identifies overextension or trend initiation.

## Transmission Mapping
`[CVD Divergence at LVN] -> [Absorption of Aggressive Orders] -> [Rapid Mean Reversion to VA]`
