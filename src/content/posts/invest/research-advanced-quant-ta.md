---
title: 'Advanced Quant TA Patterns'
description: 'This repository stores reusable quantitative and technical analysis patterns used across the Hermes organization. These patterns combine mac…'
pubDate: 2026-06-08
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Advanced_Quant_TA.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Advanced Quant TA Patterns

This repository stores reusable quantitative and technical analysis patterns used across the Hermes organization. These patterns combine macro-economic filters, structural market analysis, and microstructure order flow to create high-probability execution windows.

## 1. Macro-Micro Synthesis Patterns

The core philosophy is that **Macro provides the direction, Structure provides the location, and Order Flow provides the timing.**

### Real-Yield Absorption Pivot (RYAP)
**Pattern**: Macro Exhaustion $\rightarrow$ Structural Rejection $\rightarrow$ Micro Absorption.

- **Macro Filter**: US 10Y Real Yields.
    - *Bullish Pivot*: Real yields must have peaked and entered a plateau or declining phase. Since real yields represent the "true cost" of capital, a peak often coincides with a peak in equity/commodity pricing pressure.
    - *Bearish Pivot*: Real yields are trending sharply upward or breaking out of a long-term consolidation, increasing the discount rate for future cash flows.
- **Structural Location**: Low Volume Node (LVN).
    - Price must enter an LVN (an area of low historical acceptance). LVNs act as "repulsion zones" where price tends to move quickly through or reject sharply from.
- **Micro Confirmation**: Cumulative Delta Divergence.
    - *Bullish Divergence*: Price makes a Lower Low (LL) while Cumulative Delta makes a Higher Low (HL). This indicates that despite price falling, aggressive sellers are being absorbed by passive limit buyers.
- **Lógica**: Macro exhaustion provides the fuel (lack of further pressure), structure provides the location (a zone of rejection), and microstructure provides the timing (absorption of the final sellers).
- **Expected Outcome**: Sharp V-bottom or inversion top with rapid recovery.

---

## 2. Order Flow & Microstructure Patterns

### Passive Absorption & Initiation
Absorption occurs when one side of the market (usually institutional) places large limit orders that "absorb" all aggressive market orders without allowing price to move.

- **Absorption Signature**:
    - High volume at a specific price level.
    - Large Delta (aggressive buying/selling) but zero to minimal price movement.
    - *Example*: Massive positive delta at a resistance level with price failing to break higher indicates passive selling absorption.
- **Initiation Signature**:
    - Occurs immediately after absorption.
    - A shift in Delta polarity (e.g., from positive to negative) accompanied by a breakout from the absorption zone.
    - High-velocity movement away from the level, confirming the "winning" side has taken control.

### Liquidity Void & Gap Fill Dynamics
Liquidity voids are areas where price moved so rapidly that very few limit orders were filled, creating a "vacuum" in the Volume Profile.

- **The Void Fill**: Price is magnetically drawn to fill these voids to establish a new "Fair Value."
- **Quant Trigger**:
    - Identify a gap in the Volume Profile (Volume $\approx 0$ over a price range).
    - Wait for a structural shift (Change of Character) in the opposite direction.
    - Target the 50% equilibrium point of the void (Consequent Encroachment) as the primary take-profit.

---

## 3. Volume Profile Analysis (VPA)

### Value Area (VA) and Point of Control (POC)
- **Value Area (VA)**: The price range where 70% of the volume occurred.
- **Point of Control (POC)**: The single price level with the highest volume.

**Trading the Value Area**:
- **VA-High/Low Rejection**: If price opens outside the VA and fails to enter it within the first 30 minutes, the market is "imbalanced," and the trend is likely to continue.
- **VA-Mean Reversion**: If price enters the VA and stabilizes, it is likely to rotate toward the POC.
- **POC Migration**: If the POC moves higher/lower over several sessions, it indicates a structural trend shift (Value Migration).

## 4. Execution Checklist for Quant TA
1. **Macro Check**: Are Real Yields/DXY aligned with the trade direction?
2. **Structural Check**: Is price at a HVN (Support/Resistance) or LVN (Rejection)?
3. **Micro Check**: Is there a Delta divergence or Absorption pattern on the footprint chart?
4. **Confirmation**: Has a "Market Initiation" candle closed outside the value area?
