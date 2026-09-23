---
title: 'Order Flow and Market Profile Knowledge Base'
description: 'Market Profile is a visualization of the distribution of price over time. It views the market as a continuous auction seeking "Fair Value."'
pubDate: 2026-05-18
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Order_Flow_Market_Profile.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Order Flow and Market Profile Knowledge Base

## 1. Market Profile (TPO - Time Price Opportunity)
Market Profile is a visualization of the distribution of price over time. It views the market as a continuous auction seeking "Fair Value."

### Core Components
- **TPO (Time Price Opportunity):** A letter representing a specific time period (usually 30 min) spent at a price level.
- **POC (Point of Control):** The price level with the most TPOs. It is the "heart" of the market and acts as a powerful magnet and support/resistance level.
- **Value Area (VA):** The range containing ~70% of the day's TPOs.
    - **VAH (Value Area High):** Upper boundary of the VA.
    - **VAL (Value Area Low):** Lower boundary of the VA.
- **Initial Balance (IB):** The range established in the first hour of trading (Periods A + B). It sets the day's framework.
- **Single Prints:** Prices visited by only one TPO letter, indicating fast rejection and high conviction moves.
- **Poor High/Low:** Extremes where multiple TPOs exist at the same level, suggesting an incomplete auction and a likely future revisit.

### Market Regimes
- **Balance (Equilibrium):** Symmetrical profile, price rotates between VAH and VAL, POC is stable.
- **Imbalance (Trending):** Asymmetrical profile, POC migrates, VA shifts rather than overlaps.
- **Value Area Overlap:** 
    - High Overlap (≥60%): Balance. Fade the edges.
    - Low Overlap (<40%): Strong Imbalance. Trade the trend.

### Trading Logic
- **The 80% Rule:** If price opens outside the previous day's VA and then re-enters it, there is an ~80% chance it will rotate to the opposite edge of the VA.
- **Entry:** Look for acceptance failure at VA edges. Price probes outside, fails to build TPOs, and closes back inside $\rightarrow$ Trade toward the POC/opposite edge.

---

## 2. Order Flow Analysis
Order Flow is the study of the interaction between aggressive (Market) and passive (Limit) orders.

### Key Metrics
- **Volume Delta:** (Aggressive Buys) - (Aggressive Sells).
- **Cumulative Delta (CVD):** The running total of delta. Used to find divergences.
- **Absorption:** When large limit orders "absorb" aggressive market orders, causing price to stall despite high volume/delta.
- **Footprint Charts:** Granular view of bid/ask volume at every price level.
- **Imbalances:** Occur when one side (Bid or Ask) is significantly larger (typically 3x+) than the opposite side at an adjacent price level.

### Signals and Patterns
- **Delta Divergence:** Price makes a new high, but CVD makes a lower high $\rightarrow$ Aggressive buyers are exhausting; potential reversal.
- **Bullish Absorption:** Price drops to support, high negative delta (aggressive selling), but price does not move lower $\rightarrow$ Large buyer absorbing. Bullish signal.
- **Stacked Imbalances:** Multiple imbalance levels in a row, creating a "zone of interest" that acts as strong support/resistance upon retest.

---

## 3. Synthesis: The "Where" and the "When"
- **Market Profile (TPO) $\rightarrow$ The "Where":** Identifies high-probability zones (POC, VA, IB).
- **Order Flow $\rightarrow$ The "When":** Provides the execution trigger (Absorption, Delta Divergence, Imbalances) within those zones.
- **Strategy:** 
    1. Identify the regime (Balance vs. Imbalance) via VA Overlap.
    2. Mark the key levels (VAH, VAL, POC).
    3. Wait for price to reach a level.
    4. Trigger trade based on Order Flow confirmation (e.g., Absorption at VAL during a Balance day).
