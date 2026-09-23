---
title: 'Advanced Quantitative Technical Analysis'
description: 'Institutional trading has shifted toward understanding the "Auction" process—how the market seeks fair value through the interaction of time…'
pubDate: 2026-05-23
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/investment/Technical_Analysis/Advanced_Quant_TA.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Advanced Quantitative Technical Analysis

## Auction Market Theory (AMT) & Market Profile
Institutional trading has shifted toward understanding the "Auction" process—how the market seeks fair value through the interaction of time, price, and volume.

### Market Profile (TPO) Core Concepts
|- **TPO (Time Price Opportunity)**: Tracks how much time the market spends at a specific price.
|- **Value Area (VA)**: The range where 70% of the day's activity occurs.
|- **Point of Control (POC)**: The price level with the highest time/volume density (the "fairest" price).
|- **Initial Balance (IB)**: The range of the first hour of trading; used to predict range extension or reversion.
|- **Single Prints**: "Tails" indicating aggressive institutional movement and potential liquidity vacuums.

### Institutional Order Flow Integration
|- **TPO vs. Volume POC**: A divergence where the Volume POC is significantly above the TPO POC suggests aggressive institutional accumulation (Bullish), and vice-versa.
|- **Liquidity Heatmaps**: Using tools like Bookmap to overlay TPO structure with real-time resting limit orders (the "intent" of big players).
|- **Composite Analysis**: Aligning Quarterly, Monthly, and Weekly composites to find "Super POCs" (high-conviction magnets).

## Frontier Quant Strategies (2026)

### NeoWave & Confluence Framework
High-probability forecasting is achieved through the confluence of:
1. **NeoWave Structure**: Defining the directional wave count (forecasting).
2. **Open Interest (OI)**: Identifying positioning (Tug-of-War between buyers/sellers).
3. **Volume Profile**: Pinpointing institutional "acceptance" zones.

### Proprietary SIF Signals
|- **Hermes Macro-Structural Flux (HMSF)**: A high-conviction reversal indicator.
  - **Logic**: `(RealYields_Slope < 0) ∩ (NeoWave_W2_Completion) ∩ (CVD_Bullish_Divergence)`.
  - **Utility**: Filters out false breakouts by aligning the discount rate (Macro), the wave cycle (Structure), and institutional absorption (Micro).
|- **Hermes Liquidity Vacuum Convergence (HLVC)**: A high-convexity entry indicator.
  - **Logic**: `(DXY_Momentum < 0) ∩ (LVN_Support_Reaction) ∩ (Footprint_Buy_Stacking)`.
  - **Utility**: Combines USD weakness (Fuel) with Market Profile rejections (Floor) and Order Flow imbalances (Trigger).
|- **Hermes Yield-Curve Divergence Pivot (HYDP)**: A regime-shift entry indicator.
  - **Logic**: `(YieldCurve_Slope > 0) ∩ (VA_Migration_Ascending) ∩ (Liquidity_Sweep_Low_Positive_Delta)`.
  - **Utility**: Aligns macro growth expectations (Yield Curve) with institutional fair-value migration (Value Area) and a precise microstructure trigger (Liquidity Sweep).
|- **Hermes Asymmetric Expansion Trigger (HAET)**: An explosive breakout indicator.
  - **Logic**: `(DXY_ZScore > 2.0) ∩ (Squeeze_Compression) ∩ (LOB_AskBid_Ratio < 0.7)`.
  - **Utility**: Combines USD overextension (Fuel) with volatility compression (Coil) and order book asymmetry (Void) to isolate high-velocity expansions.
|- **Hermes Liquidity Exhaustion Pivot (HLEP)**: A trend-terminal distribution indicator.
    - **Logic**: `(RealYields_ZScore > 1.5) ∩ (Failed_Auction_Structure) ∩ (CVD_Bearish_Divergence)`.
    - **Utility**: Aligns restrictive discount rates (Macro) with auction failure (Structure) and institutional absorption (Micro) to isolate high-probability trend tops.
    - **Hermes Volatility-Liquidity Pivot (HVLP)**: A consensus-break distribution indicator.
      - **Logic**: `(RealYields_Momentum == 'Peaking') ∩ (HVN_Rejection) ∩ (Delta_Exhaustion_Absorption)`.
      - **Utility**: Detects the collapse of institutional fair-value zones by aligning macro pressure with structural rejection and microstructure absorption.
|- **Hermes Monetary-Structural Divergence (HMSD)**: A "Bull Trap" detection indicator.
  - **Logic**: `(DXY_Momentum > 0) ∩ (VAH_Breakout) ∩ (Informed_Sell_Opp_Buy)`.
  - **Utility**: Isolates superficial technical breakouts funded by retail FOMO and absorbed by institutional hedging under restrictive macro conditions.

## Update: 2026-05-18
|- **Institutional Auction Framework (Market Profile)**:
    - **Composite Alignment**: High-conviction zones identified via alignment of Quarterly $\to$ Monthly $\to$ Weekly $\to$ Daily POCs.
    - **Super POC**: Convergence of TPO POC and Volume POC; acts as a massive price magnet.
    - **Excess Fades**: Trading against "Single Prints" (institutional tails) to fade trapped traders; reported 70-80% success rate.
    - **POC Divergence**: Volume POC $\pm$ 10+ points from TPO POC signals aggressive institutional accumulation/distribution.
    - **Inventory Tracking**: Tracking overnight long/short inventory to identify potential "trapped" positions and imminent short-squeezes or cascades.
|- **Order Flow Integration**:
    - **Delta/Absorption Analysis**: Using cumulative delta and footprint charts to identify "absorption" (high volume without price movement) at key Profile levels for surgical entries.
    - **Liquidity Heatmaps**: Utilizing real-time resting limit order visualization (e.g., Bookmap) to validate TPO value areas and detect "iceberg" orders.
|- **Frontier Quant Research (May 2026)**:
    - **ClusterLOB**: Transition from raw Order Book Imbalance (LOB) to *Participant Clustering* (Directional Informed, Opportunistic, Market Makers) for cleaner predictive signals.
    - **FlowOE**: Adaptive optimal execution using Flow-Matching Imitation Learning to blend expert policies, reducing slippage (18-35 bp) across different volatility regimes.
    - **Microstructure Breakout Alpha**: High-fidelity breakout detection using simultaneous confirmation across four signals (price velocity, volume surge, flow direction, depth vacuum) measured on optimized \"bar clocks\" (e.g., imbalance-based vs. volume-based) to isolate institutional intent from noise.
|- **Derivatives Flow Models**:
    - **Vanna/Delta Mapping**: Modeling dealer hedging pressure to identify \"Magnet\" zones and structural support/resistance levels.

## Update: 2026-05-22
|- **Market Profile \"Hidden Magnets\"**: 
    - **Unfinished Auctions**: Occur when two or more TPO blocks have the same high/low, indicating an incomplete auction process and a high probability of price return.
    - **Untested VPOC**: The highest volume point from the past not yet visited since creation; acts as a powerful price magnet.
    - **The 80% Rule (Return to VA)**: Statistical setup where opening outside the Value Area (VA) and returning inside for two consecutive TPO blocks (60m) creates an 80% probability of traversing the entire VA to the opposite boundary.
|- **Institutional Order Flow (2026)**:
    - **Footprint Imbalance + HVN**: High-conviction turning points identified where high-volume nodes (HVN) align with aggressive footprint imbalances.
    - **Delta Shift + CHoCH**: \"Change of Character\" (CHoCH) signals are validated via a clear shift in delta on cluster charts to confirm institutional commitment.
    - **Clustered Flow**: Move away from raw LOB imbalance toward clustering participant types (Informed vs. Opportunistic) to reduce signal noise.
|- **Derivatives & Volatility Surface**:
    - **Vanna Mapping**: Use of dealer hedging pressure (Vanna) to identify structural support (e.g., the \"7420 zone\" for SPX) and magnet regions.

## Update: 2026-05-23
|- **Flow Fragility & Systematic Deleveraging**: Analysis of "flow-of-funds unwind" risks where crowded passive inflows and levered ETF exposure create downward asymmetry; "Spot up, Vol up" regimes identified as signals of unsustainable upside call chasing.
|- **Dealer-Centric Gamma Trading (JATS Framework)**: Use of GEX (Gamma Exposure) to pinpoint "invisible walls" and Dealer hedging pressure; implementation of "VIX Proxies" measuring structural displacement (RVOL vs HVOL) to distinguish between high-friction "Dealer Absorption" and low-friction "Feedback Loops" (Gamma Squeezes).
|- **Speculative Conviction Metrics**: Integration of VolM (speculation center), SpecPA (conviction width), and SpecPS (conviction slope) to determine if intraday momentum is building, sustaining, or dissipating.
|- **Market Profile \"Hidden Magnets\" & 80% Rule**: 
    - **The 80% Rule**: Opening outside the Value Area (VA) and returning inside for two consecutive TPO blocks (60m) creates an 80% probability of traversing the entire VA to the opposite boundary.
    - **Structural Magnets**: \"Untested VPOC\" (highest volume point not yet visited) and \"Unfinished Auctions\" (matching TPO highs/lows) act as high-probability price targets.
|- **Institutional Order Flow Confluence**: 
    - **OB + FVG Overlap**: The highest-probability entry zone is the overlap of an Order Block (last opposing candle before impulse) and a Fair Value Gap (imbalance in a 3-candle sequence).
    - **Kill Zone Gating**: Entries are filtered by specific institutional timing windows (London: 2-5 AM EST, NY: 7-10 AM EST).
|- **NeoWave Quantitative Profiling**: Transition to systems (e.g., Wave Engine) that treat Time Analysis as a primary weighting factor alongside Price and Complexity to generate objective, non-repainting structure labels.
