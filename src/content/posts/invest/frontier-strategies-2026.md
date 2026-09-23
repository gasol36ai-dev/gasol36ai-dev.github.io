---
title: 'Frontier Order Flow & Quantitative Trading (2026)'
description: 'Price Action reveals what happened; Order Flow reveals why it happened. The goal is to identify institutional commitment (absorption/imbalan'
pubDate: 2026-05-16
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Frontier_Strategies_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Frontier Order Flow & Quantitative Trading (2026)

## Core Philosophy
Price Action reveals *what* happened; Order Flow reveals *why* it happened. The goal is to identify institutional commitment (absorption/imbalance) before it manifests as a candlestick pattern.

## High-Impact Tools & Metrics
- **Volume Profile (VP)**:
  - **POC (Point of Control)**: The price level with the most volume; acts as a magnet and a high-conviction support/resistance.
  - **VA (Value Area)**: The range containing 70% of volume. Price outside VA indicates conviction/trending; inside indicates fairness/range.
  - **LVN (Low Volume Nodes)**: Areas of rejection where price accelerates quickly.
- **Delta & Footprint**:
  - **Delta**: Aggressive Buyers minus Aggressive Sellers.
  - **Absorption**: High volume at a level with minimal price movement $\rightarrow$ Institutions are defending the zone.
  - **Stacked Imbalances**: 3+ consecutive price levels where one side is 3x+ larger than the other $\rightarrow$ Strong directional momentum.

## Institutional-Grade Setup: The "Double Confirmation"
1. **Structural Context**: Use Volume Profile to identify a Heavy Volume Zone (HVZ) or POC.
2. **Micro Trigger**: Use Footprint/Delta to identify a **Delta Shift** (Negative $\rightarrow$ Positive at support) or **Absorption** (High volume, no breach).
3. **Confirmation**: Combined High Volume + High Time at a level = Highest significance.

## Quantitative Models
- **Structural VAR (SVAR-ITH)**: Used to disentangle the contemporaneous price impact of Order Flow Imbalance (OFI) from the reverse flow impact of returns, especially during macro news events.
- **Hybrid VAR-FNN**: Combining linear Vector Auto Regression (VAR) for dependencies and Feedforward Neural Networks (FNN) for non-linear residuals to forecast OFI and trading intensity.
