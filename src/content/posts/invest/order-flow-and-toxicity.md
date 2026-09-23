---
title: 'Order Flow & Market Toxicity'
description: ''
pubDate: 2026-05-15
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Order_Flow_and_Toxicity.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Order Flow & Market Toxicity

## VPIN (Volume-Synchronized Probability of Informed Trading)
- **Definition**: A metric that estimates the probability of informed trading by analyzing order flow toxicity.
- **Mechanism**: Uses volume-synchronized buckets (instead of time) to normalize for burstiness.
- **Formula (Simplified)**: $VPIN = \frac{\sum |V_{buy} - V_{sell}|}{V_{total}}$ over $N$ buckets.
- **Directional VPIN (Hermes Extension)**: While standard VPIN measures magnitude, Directional VPIN tracks the sign of the imbalance to determine the *side* of the informed trade.

## High-Probability Order Flow Patterns
### Absorption
- **Pattern**: Massive volume traded at a level with little to no price movement.
- **Mechanism**: Aggressive market orders are being "absorbed" by a large resting limit order wall.
- **Signal**: Indicates institutional positioning; often precedes a sharp reversal once the aggressor is exhausted.

### Delta Divergence
- **Pattern**: Price makes a new high/low, but Cumulative Volume Delta moves in the opposite direction.
- **Mechanism**: Buyers/Sellers are becoming less aggressive even as price grinds higher/lower.
- **Signal**: Warning of momentum exhaustion; high-probability when confirmed by a liquidity sweep.

### Stacked Imbalance
- **Pattern**: 3 or more consecutive price levels where aggressive buying/selling dominates.
- **Signal**: Strong directional commitment; often accompanies range expansions.
