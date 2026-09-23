---
title: 'Hermes SIF Proprietary Logic Wiki'
description: 'This document defines the proprietary judgment indicators and logic gates used by the Hermes Strategic Investment Framework (SIF). These ind…'
pubDate: 2026-05-23
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/investment/Technical_Analysis/Hermes_SIF_Logic.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes SIF Proprietary Logic Wiki

This document defines the proprietary judgment indicators and logic gates used by the Hermes Strategic Investment Framework (SIF). These indicators synthesize macro-economic variables, technical structures, and microstructure signals into high-conviction trade triggers.

## Proprietary Indicator: Hermes Macro-Structural Flux (HMSF)

The HMSF indicator identifies "Structural Pivot Points" where macro winds, technical blueprints, and real-time order flow align to signal a high-probability trend reversal.

### Logic Gate Formula
`HMSF_LONG = (RealYields_Slope < 0) ∧ (NeoWave_State == 'W2_Complete') ∧ (Price_Action == 'Low_Pivot' ∧ Delta_CVD == 'Bullish_Div')`

### Component Definitions
1. **Macro Variable: RealYields_Slope < 0**
   - Variable: US 10Y Treasury Inflation-Protected Securities (TIPS) yield.
   - Condition: A sustained decline or "peak-out" in real yields, reducing the discount rate for risk assets and signaling a shift toward a more accommodative macro regime.

2. **TA Structure: NeoWave_State == 'W2_Complete'**
   - Structure: NeoWave Wave 2 correction.
   - Condition: Price has completed a corrective phase (Wave 2) following an initial impulse (Wave 1), typically characterized by a specific Fibonacci retracement level and structural completion patterns (e.g., a flat or zigzag).

3. **Microstructure Signal: Low_Pivot ∧ Bullish_Div**
   - Signal: Order Flow Delta Divergence.
   - Condition: Price hits a local low (Low Pivot), but the Cumulative Volume Delta (CVD) makes a higher low. This indicates that while aggressive sellers are pushing the price down, aggressive buyers are absorbing all supply, creating a "hidden" demand zone.

### Reasoning
The HMSF avoids the "trap" of using any single indicator. By requiring a macro tailwind (Real Yields), a structural map (NeoWave), and immediate confirmation of absorption (CVD Divergence), it filters out noise and only triggers when institutional accumulation is physically observable against a favorable macro backdrop.

## Proprietary Indicator: Hermes Liquidity Vacuum Convergence (HLVC)

The HLVC indicator identifies "Institutional Springs" where a macro risk-on shift coincides with a structural price rejection zone and aggressive real-time absorption.

### Logic Gate Formula
`HLVC_LONG = (DXY_Momentum < 0) ∧ (Price_Location == 'LVN_Support') ∧ (OrderFlow_Imbalance == 'Aggressive_Buy_Stack')`

### Component Definitions
1. **Macro Variable: DXY_Momentum < 0**
   - Variable: US Dollar Index (DXY) trend.
   - Condition: A clear bearish momentum shift in the USD, typically signaling a global transition to risk-on sentiment and increased liquidity for non-USD assets.

2. **TA Structure: Price_Location == 'LVN_Support'**
   - Structure: Market Profile Low Volume Node (LVN).
   - Condition: Price returns to a prominent LVN (a "liquidity vacuum" where price previously moved through rapidly). These zones act as hard structural floors because they represent areas of extreme disagreement where the market quickly found a new fair value.

3. **Microstructure Signal: OrderFlow_Imbalance == 'Aggressive_Buy_Stack'**
   - Signal: Footprint Chart Imbalance.
   - Condition: Detection of 3+ consecutive buy-side imbalances (aggressive buyers hitting the ask) at the LVN support level. This confirms that the "vacuum" is being filled by institutional demand.

### Reasoning
The HLVC targets high-convexity entries by combining the "Fuel" (USD weakness), the "Floor" (LVN rejection), and the "Trigger" (Buy Stacking). It prevents premature entries in downtrends by requiring a structural floor to be validated by aggressive order flow.

## Proprietary Indicator: Hermes Regime Shift Oscillator (HRSO)

The HRSO is designed to detect the physical adoption of a macro-regime transition (e.g., the exit from a recessionary period or a shift toward growth acceleration) by aligning treasury signals with institutional fair-value migration and high-fidelity participant clustering.

### Logic Gate Formula
`HRSO_LONG = (YieldCurve_10Y2Y_Slope > 0) ∧ (VA_Migration == 'Ascending') ∧ (ClusterLOB_Informed_Delta > Threshold)`

### Component Definitions
1. **Macro Variable: YieldCurve_10Y2Y_Slope > 0**
   - Variable: The spread between the US 10-Year and 2-Year Treasury yields.
   - Condition: A positive slope (steepening), particularly following a period of inversion. This typically signals a transition toward economic normalization and increased growth expectations.

2. **TA Structure: VA_Migration == 'Ascending'**
   - Structure: Market Profile Value Area (VA) Migration.
   - Condition: The Value Area (the region where 70% of volume occurs) is migrating higher across consecutive sessions. This confirms that institutional "fair value" is being recalibrated upward, rather than just a temporary price spike.

3. **Microstructure Signal: ClusterLOB_Informed_Delta > Threshold**
   - Signal: Participant Clustering (derived from ClusterLOB research).
   - Condition: A significant positive delta in order flow originating from "Informed" clusters (characterized by high-size, low-latency, and strategic positioning) rather than "Opportunistic" (retail/momentum) clusters.

### Reasoning
The HRSO prevents "false dawn" entries during regime shifts. While a steepening yield curve provides the macro thesis, and VA migration shows institutional acceptance, the ClusterLOB signal provides the final confirmation that the move is driven by informed capital rather than speculative noise.

## Proprietary Indicator: Hermes Liquidity Exhaustion Pivot (HLEP)

The HLEP indicator identifies "Trend Terminals" where macro headwinds, structural auction failure, and physical order flow absorption converge to signal a high-probability trend exhaustion or reversal.

### Logic Gate Formula
`HLEP_SHORT = (RealYields_ZScore > 1.5) ∧ (Auction_State == 'Failed_Auction') ∧ (Delta_CVD == 'Bearish_Div')`

### Component Definitions
1. **Macro Variable: RealYields_ZScore > 1.5**
   - Variable: US 10Y Treasury Inflation-Protected Securities (TIPS) yield Z-score.
   - Condition: Real yields are statistically overextended to the upside or rising sharply. This increases the discount rate for risk assets, creating a fundamental headwind for further expansion.

2. **TA Structure: Auction_State == 'Failed_Auction'**
   - Structure: Market Profile / Auction Market Theory.
   - Condition: Price attempts to break out of the Value Area High (VAH) or creates a new local high but fails to find acceptance, quickly retreating to leave a "Single Print" or "Tail" of excess. This signals that the auction has reached a limit of buyer interest.

3. **Microstructure Signal: Delta_CVD == 'Bearish_Div'**
   - Signal: Cumulative Volume Delta (CVD) Divergence.
   - Condition: Price makes a higher high, but CVD makes a lower high. This is the "physical" proof of absorption: aggressive market buyers are hitting the ask, but passive institutional sellers are absorbing all orders with limit sells, preventing further price progression.

### Reasoning
The HLEP targets the "hidden" top. By requiring a restrictive macro backdrop (Real Yields), a structural rejection (Failed Auction), and proof of absorption (CVD Divergence), it filters out minor pullbacks in strong trends and only triggers when the trend's physical and fundamental foundations have collapsed.

## Proprietary Indicator: Hermes Volatility-Liquidity Pivot (HVLP)

The HVLP indicator detects "Consensus Collapses" where macro-restrictive pressure causes a failure of institutional fair-value zones, signaling a high-velocity move away from the current range.

### Logic Gate Formula
`HVLP_SHORT = (RealYields_Momentum == 'Peaking') ∧ (Price_Location == 'HVN_Rejection') ∧ (OrderFlow == 'Delta_Exhaustion_Absorption')`

### Component Definitions
1. **Macro Variable: RealYields_Momentum == 'Peaking'**
   - Variable: US 10Y TIPS Yield momentum.
   - Condition: A positive but decelerating momentum (second derivative < 0) or a sharp reversal from a multi-month high. This indicates that the "discount rate" pressure has reached a limit.

2. **TA Structure: Price_Location == 'HVN_Rejection'**
   - Structure: Market Profile High Volume Node (HVN).
   - Condition: Price reaches a major HVN (the area of highest historical institutional acceptance) but fails to consolidate, creating a "rejection wick" or a failed test. This signals that the market no longer views this level as "fair value."

3. **Microstructure Signal: OrderFlow == 'Delta_Exhaustion_Absorption'**
   - Signal: Order Flow Exhaustion.
   - Condition: A large positive Delta spike (aggressive buying) coincides with price stagnation or a slight drop, followed by an immediate shift to negative Delta. This is the physical signature of "buying exhaustion" meeting a "hidden" limit seller.

## Proprietary Indicator: Hermes Systemic Absorption Pivot (HSAP)

The HSAP indicator identifies "Panic Bottoms" where systemic credit stress triggers forced liquidations, which are then aggressively absorbed by informed institutional capital at structural liquidity extremes.

### Logic Gate Formula
`HSAP_LONG = (CreditSpreads_ZScore > 2.0) ∧ (Price_Action == 'Liquidity_Sweep_Low') ∧ (ClusterLOB_Informed_Delta > Threshold)`

### Component Definitions
1. **Macro Variable: CreditSpreads_ZScore > 2.0**
   - Variable: High Yield Corporate Bond Spreads (e.g., HYG/IEI ratio) or TED Spread.
   - Condition: Credit spreads are statistically overextended to the upside. This signals systemic risk-off sentiment and forced deleveraging, creating an environment of "panic" selling.

2. **TA Structure: Price_Action == 'Liquidity_Sweep_Low'**
   - Structure: Liquidity Sweep / Stop-Run.
   - Condition: Price aggressively sweeps below a prominent multi-month or multi-year structural low, triggering stop-loss orders and liquidating long positions, only to reclaim the level quickly.

3. **Microstructure Signal: ClusterLOB_Informed_Delta > Threshold**
   - Signal: Participant Clustering (ClusterLOB).
   - Condition: A significant positive delta surge specifically originating from the "Informed" cluster (large-size, low-latency strategic players) during the liquidity sweep. This proves that "Smart Money" is utilizing the panic to accumulate.

### Reasoning
The HSAP isolates the exact moment when systemic fear (Macro) and mechanical liquidations (TA) meet institutional appetite (Micro). By requiring credit stress as the catalyst, it avoids "fake" dips and focuses on high-convexity reversals born from genuine market capitulation.

## Proprietary Indicator: Hermes Monetary-Structural Divergence (HMSD)

The HMSD indicator identifies "Liquidity Traps" (specifically Bull Traps) where superficial technical breakouts are driven by speculative retail flow and absorbed by informed institutional capital under restrictive macro conditions.

### Logic Gate Formula
`HMSD_SHORT = (DXY_Momentum > 0) ∧ (Price_Action == 'VAH_Breakout') ∧ (ClusterLOB_Divergence == 'Informed_Sell_Opp_Buy')`

### Component Definitions
1. **Macro Variable: DXY_Momentum > 0**
   - Variable: US Dollar Index (DXY) momentum.
   - Condition: A clear bullish trend or momentum surge in the USD, which typically creates a restrictive environment for risk assets and increases the cost of carry for long positions.

2. **TA Structure: Price_Action == 'VAH_Breakout'**
   - Structure: Market Profile Value Area High (VAH).
   - Condition: Price breaks above the Value Area High, creating a superficial signal of bullish expansion that attracts momentum traders and "breakout" retail longs.

3. **Microstructure Signal: ClusterLOB_Divergence == 'Informed_Sell_Opp_Buy'**
   - Signal: Participant Cluster Divergence (ClusterLOB).
   - Condition: A stark divergence where "Opportunistic" clusters (retail/momentum) show high positive delta (aggressive buying), while "Informed" clusters (institutional/strategic) show negative delta (aggressive selling or heavy limit absorption).

### Reasoning
The HMSD provides high-fidelity detection of "Bull Traps." It filters out genuine breakouts by ensuring that the "fuel" for the move is solely speculative (retail FOMO) and that informed capital is actively utilizing the liquidity provided by that breakout to exit or hedge positions, all while macro winds (USD strength) are structurally against the move.
