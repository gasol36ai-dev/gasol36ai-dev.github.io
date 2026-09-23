---
title: 'Frontier Quantitative Trading: Order Flow & Market Profile (2026)'
description: 'The core philosophy is that the market is a continuous auction seeking "Fair Value." Price movement is the process of finding where institut…'
pubDate: 2026-05-22
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Order_Flow_Market_Profile_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Frontier Quantitative Trading: Order Flow & Market Profile (2026)

## 1. Auction Market Theory (AMT)
The core philosophy is that the market is a continuous auction seeking "Fair Value." Price movement is the process of finding where institutional participants are willing to transact.

## 2. Market Profile (TPO) & Volume Profile (VP)
### TPO (Time Price Opportunity)
- **Focus**: Time spent at price.
- **Key Metrics**: 
    - **Initial Balance (IB)**: Range of the first hour; sets the day's tone.
    - **Point of Control (POC)**: Level with the most time spent (fairest price).
    - **Value Area (VA)**: Range where 70% of time was spent.
    - **Single Prints**: Fast moves indicating institutional "tails" or urgency.
- **Insight**: Reveals the *structure* of the auction.

### Volume Profile (VP)
- **Focus**: Actual contracts traded at price.
- **Key Metrics**:
    - **High Volume Nodes (HVN)**: Areas of acceptance/accumulation.
    - **Low Volume Nodes (LVN)**: Areas of rejection/liquidity gaps.
- **Insight**: Reveals where the *money* is.

**Synergy**: When TPO POC and Volume POC align, it creates a **"Super POC"**, a massive magnet for price.

## 3. Advanced Order Flow (Micro-Structure)
### Delta Analysis
- **Delta**: $\text{Aggressive Buyers} - \text{Aggressive Sellers}$.
- **Delta Divergence**: Price makes a new low, but Delta is less negative (or positive) $\rightarrow$ Institutional absorption/reversal signal.
- **Cumulative Delta**: Tracks the net aggression over a session to identify trend exhaustion.

### Absorption
- **Definition**: High volume at a price level with minimal price movement.
- **Significance**: Indicates a massive institutional "iceberg" order is absorbing all aggressive market orders, often preceding a sharp reversal.

### Participant Clustering (2026 Frontier)
- **Shift**: Moving away from raw Order Book Imbalance (LOB) which decays quickly.
- **Approach**: Clustering Market-By-Order (MBO) streams into three archetypes:
    1. **Directional Informed**: Leave persistent footprints (Alpha source).
    2. **Opportunistic Liquidity Takers**: Short-term noise.
    3. **Market Makers**: Predictable cancellation/repositioning patterns.
- **Edge**: Separating participant *intent* provides cleaner predictive signals than raw imbalance.

## 4. Execution Innovation: Flow-Matching Imitation (FlowOE)
- **Problem**: RL agents lock into one regime and break during volatility shifts.
- **Solution**: Uses flow-matching imitation learning to blend multiple expert policies, dynamically adapting to the current market regime in real-time.
- **Result**: Material reduction in slippage for block execution.

## 5. Operational Setups
### The Poor Low Reversal
1. **Identify**: Poor low structure (tail with single prints) on Market Profile.
2. **Confirm**: Delta divergence (price new low, delta less negative).
3. **Trigger**: Price trades back through (repairs) the single print zone.
4. **Target**: Previous day's POC.
