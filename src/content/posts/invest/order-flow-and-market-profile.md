---
title: 'Order Flow and Market Profile Analysis (Updated 2026-05-19)'
description: 'Market Profile analyzes the time spent at specific price levels to reveal the "fair value" as perceived by institutional participants.'
pubDate: 2026-05-19
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Order_Flow_and_Market_Profile.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Order Flow and Market Profile Analysis (Updated 2026-05-19)

## 1. Market Profile (TPO - Time Price Opportunity)
Market Profile analyzes the *time* spent at specific price levels to reveal the "fair value" as perceived by institutional participants.

### Core Concepts
*   **TPO (Time Price Opportunity)**: A letter represents a time period (e.g., 30 mins) where price traded.
*   **Point of Control (POC)**: The price level with the most TPOs (the "fairest" price).
*   **Value Area (VA)**: The range where 70% of the session's time was spent.
*   **Initial Balance (IB)**: The price range established during the first hour of trading.
*   **Composite Profile**: Merging multiple days/weeks of TPO data to see long-term institutional positioning.
*   **Excess**: A "tail" on the profile indicating a sharp rejection; identifies trapped traders.
*   **Poor Highs/Lows**: Price levels that lack excess, signaling "unfinished business" and a likely return to that level.

## 2. Order Flow Trading
While Market Profile shows *where* trading happened, Order Flow shows *how* it happened via market microstructure.

### Key Tools & Metrics
*   **DOM (Depth of Market)**: Visualizes resting limit orders. Heatmaps (e.g., Bookmap) show where liquidity is concentrated.
*   **Footprint Charts**: Shows the actual volume traded at the bid vs. the ask inside each candle.
*   **Delta**: The net difference between buying volume (lifting offers) and selling volume (hitting bids).
*   **Cumulative Delta**: Tracks delta over time to identify divergences.

### High-Probability Setups
| Setup | Trigger | Logic |
| :--- | :--- | :--- |
| **Delta Divergence** | Price makes new high, but Cumulative Delta fails to do so. | Hidden selling pressure; likely reversal. |
| **Absorption Fade** | Huge volume at a key level (POC/VA) but price fails to move. | Institutions are absorbing all orders; price likely reverses. |
| **Stacked Imbalances** | 3+ consecutive footprint imbalances in one direction. | Strong aggressive momentum; high-conviction trend. |

## 3. Integration Strategy
**The Professional Workflow:**
1.  **Macro/Context**: Determine bias using Weekly Composite Profiles and Overnight Inventory.
2.  **Structure**: Identify key levels using the daily TPO POC and Value Area.
3.  **Timing**: Use Footprint imbalances and Delta Divergence for the precise entry trigger.
