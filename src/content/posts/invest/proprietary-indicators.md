---
title: 'Hermes Proprietary Judgment Indicators (HPI)'
description: 'The Hermes Proprietary Indicators (HPI) are synthetic judgment metrics designed to bridge the gap between raw technical data (Order Flow/VP)'
pubDate: 2026-06-18
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Proprietary_Indicators.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Proprietary Judgment Indicators (HPI)

## Introduction
The Hermes Proprietary Indicators (HPI) are synthetic judgment metrics designed to bridge the gap between raw technical data (Order Flow/VP) and macro-economic sentiment. They are designed to be "Deterministic Judgment" metrics—reducing the reliance on subjective "feel" and replacing it with a multi-factor logical trigger.

## HPI-1: The "Liquidity-Macro Divergence" (LMD)
**Logic**: Detects when the macro narrative (e.g., "Recession fear") is driving prices down, but the order flow is showing massive institutional absorption at key levels.
|- **Indicator Signal**: 
    - Macro Sentiment $\rightarrow$ Bearish (via news/feeds)
    - Price $\rightarrow$ Decreasing or Flat
    - Order Flow $\rightarrow$ Large positive Delta / High-volume absorption at HVN (High Volume Node)
|- **Judgment**: "Institutional Accumulation during Panic."
|- **Action**: Contrarian Long entry.

## HPI-2: The "Vacuum-Volatility Squeeze" (VVS)
**Logic**: Identifies the moment before an explosive move by detecting an asymmetric "thinning" of the order book.
|- **Indicator Signal**:
    - DOM $\rightarrow$ Thin liquidity (Low Volume Nodes) on the Upside
    - DOM $\rightarrow$ Heavy resting limit orders on the Downside
    - Cumulative Delta $\rightarrow$ Accelerating Positive
|- **Judgment**: "Path of Least Resistance is Up."
|- **Action**: Momentum Long.

## HPI-3: The "Funding-Value Convergence" (FVC)
**Logic**: Identifies the exact reversal point of a crowded trade by finding the intersection of extreme funding and a Market Profile Value Area edge.
|- **HPI-3 Signal**:
    - Funding Rate $\rightarrow$ Extremely Positive (> 0.05%)
    - Price $\rightarrow$ Touching the Value Area High (VAH) of a 30-day composite profile.
    - Order Flow $\rightarrow$ Negative Delta emerging at the VAH.
|- **Judgment**: "Crowded Longs Trapped at Value Ceiling."
|- **Action**: Mean-reversion Short.

## Verification & Backtesting Logic
To test these indicators, the Hermes agent shall:
1. Identify a historical period of extreme macro volatility.
2. Map the Order Flow/VP data for that period.
3. Apply HPI-1, HPI-2, and HPI-3 triggers.
4. Compare result to the actual price move.
5. Refine the thresholds (e.g., change 0.05% funding to 0.07%).

## HPI-4: Geometric-Macro Fragility (GMF)
**Logic**: Detects 'Structural Liquidity Traps' where the market manifold undergoes intense geometric deformation (Shear) without price discovery (Drift) in a fragile macro regime.
|- **Indicator Signal**:
    - Macro Regime $\rightarrow$ Fragmentation (High Fragmentation + Rising Vol)
    - Micro Trigger $\rightarrow$ High SDR Acceleration + Spectral Gap ($\Delta\lambda$) Contraction
|- **Judgment**: "Structural Liquidity Trap - Imminent Volatility/Gap."
|- **Action**: Aggressive De-risking / Volatility Hedge.


## HPI-5: The "Kinematic-Liquidity Divergence" (KLD)
**Logic**: Detects when price momentum (kinematic speed/acceleration) is decoupled from the order book's underlying liquidity depth, signaling a "phantom move" prone to instant reversal.
|- **Map**: `[Price Velocity (dV/dt)] + [Order Book Depth Imbalance (Liquidity Delta)]`
|- **Trigger**: `[High Acceleration (d^2V/dt^2) with decreasing Depth in the direction of the move]`
|- **Lock**: `[Automatic reduction of Risk Budget by 25% for momentum-based entries if KLD signal is detected]`
|- **Judgment**: "Phantom Momentum - Liquidity Exhaustion Imminent."
|- **Action**: Avoid momentum long/short; wait for liquidity re-accumulation.


# Proprietary Indicator: Cross-Venue Liquidity Divergence (CVLD)
Date: 2026-05-28
Status: **PROPOSED**

## Overview
The **Cross-Venue Liquidity Divergence (CVLD)** identifies potential "liquidity traps" or "flash crashes" by detecting extreme divergence between centralized exchange (CEX) order flow and decentralized exchange (DEX) liquidity depth.

## Map-Trigger-Lock Framework

### 1. Map (Data Inputs)
|- **Input A**: CEX Order Flow Imbalance (OFI) - Directional aggressiveness of market orders.
|- **Input B**: DEX Liquidity Depth (L-Depth) - The available depth in automated market maker (AMM) pools for the same asset.
|- **Input C**: Real-time Spread - The bid-ask spread across both venues.

### 2. Trigger (The Signal)
A signal is generated when:
**[CEX Aggressive Buying (High OFI)] + [DEX Liquidity Depletion (Falling L-Depth)] + [Widening Spreads]**
*This suggests that while CEX buyers are aggressive, there is no underlying liquidity support in the broader ecosystem, leading to a high risk of a price crash/reversion.*

### 3. Lock (The Action)
Upon a **Cross-Venue Liquidity Divergence (CVLD)** signal:
|- **Risk Action**: Automatically reduce the Risk Budget by **35%** for all volatile asset positions.
|- **Execution Action**: Move stop-losses closer to the mid-price and increase hedging frequency.

## Strategic Value
Provides a predictive signal for "Liquidity Cracks" that traditional single-venue indicators miss.



## HPI-6: The "Triple Sovereign Convergence Gate" (TSCG)
**Date**: 2026-06-03
**Status**: **ACTIVE**

### Overview
The **Triple Sovereign Convergence Gate (TSCG)** is a high-fidelity judgment indicator designed to detect the non-linear transition of a nation-state into a "Hyper-Sovereign" state. It identifies the simultaneous crossing of criticality thresholds in three disparate but interdependent infrastructure layers: **Compute (Photonics)**, **Finance (RWA/Programmable Rails)**, and **Matter (Synthetic Bio)**. 

When all three gates open, the state achieves **Absolute Infrastructure Resilience**, rendering it immune to traditional external sanctions, compute-choke points, and biological dependencies.

### Map-Trigger-Lock Framework

#### 1. Map (Strategic Inputs)
|- **Input A (Compute):** `[Domestic Photonic-TDP (Tensor-Density-Power) Ratio]` - The capacity to execute LLM inference via domestic integrated photonics, bypassing silicon-based EUV dependencies.
|- **Input B (Finance):** `[RWA-Sovereign-Debt Penetration %]` - The proportion of national debt settled via domestic programmable rails, removing reliance on the legacy Eurodollar/SWIFT system.
|- **Input C (Matter):** `[Bio-Digital Material Autonomy Index]` - The ability to synthesize critical industrial/defense materials via domestic Bio-OS and automated biofoundries.

#### 2. Trigger (The Signal)
A **TSCG-Positive** signal is generated when:
**[Domestic Photonic-TDP > Threshold_X] + [RWA-Rails Penetration > Threshold_Y] + [Bio-Material Autonomy > Threshold_Z]**
*Sovereign Premium Cascade: The simultaneous crossing of these thresholds triggers a step-function re-rating of the nation's strategic risk profile and bond yields.*

#### 3. Lock (The Action)
Upon a **TSCG-Positive** signal:
|- **Judgment:** "Hyper-Sovereign Transition Detected - Absolute Infrastructure Resilience achieved."
|- **Strategic Action:** 
    - Pivot long-term capital allocation toward the state's domestic strategic industrials.
    - Recalibrate geopolitical risk models to account for the state's immunity to traditional "Choke-Point Diplomacy."
    - Increase weighting of domestic "Bio-Digital" assets.

### Strategic Value
The TSCG identifies the "Event Horizon" of sovereignty. While single-domain gains (e.g., just having a good AI chip) are incremental, the **Convergence** of the three creates a non-linear jump in national power, shifting the global balance from "Interdependent Fragility" to "Sovereign Autonomy."

## HPI-7: The 'Quantum-Bio-Sovereignty' (QBS) Convergence Gate
**Date**: 2026-06-18
**Status**: **ACTIVE**

### Overview
The **Quantum-Bio-Sovereignty (QBS) Convergence Gate** is a hyper-sovereign indicator designed to detect the moment a nation-state achieves "Biological-Quantum Autarky." It identifies the convergence of three critical, non-linear capabilities: **Warm Quantum Coherence (Bio-Computing)**, **Agentic Geopolitical Autonomy (Swarm Diplomacy)**, and **Cryptographic Resource Provenance (ZK-Supply Chains)**.

When these three vectors align, the state transitions from a "Techno-Biological Sovereign," capable of maintaining intelligence and resource integrity even under extreme kinetic or electronic warfare conditions.

### Map-Trigger-Lock Framework

#### 1. Map (Strategic Inputs)
|- **Input A (Quantum-Bio):** `[Biological Coherence Duration (BCD)]` - The stability and duration of quantum-coherent states within synthetic biological substrates used for sovereign compute.
|- **Input B (Agentic Geopolitics):** `[Swarm-to-Policy Latency (SPL)]` - The speed at which autonomous agentic swarms can adjust trade and resource flows in response to real-time sovereign resource shifts.
|- **Input C (ZK-Provenance):** `[Resource Attestation Density (RAD)]` - The percentage of critical mineral/energy flows verified via Zero-Knowledge proofs, ensuring untraceable yet verifiable sovereign supply chains.

#### 2. Trigger (The Signal)
A **QBS-Positive** signal is generated when:
**[BCD > Threshold_Q] + [SPL < Threshold_A] + [RAD > Threshold_Z]**
*This indicates the convergence of Biological Quantum Intelligence, Agentic Geopolitical Speed, and Cryptographic Resource Secrecy.*

#### 3. Lock (The Action)
Upon a **QBS-Positive** signal:
|- **Judgment:** "Techno-Biological Autarky Detected - Hyper-Sovereign Transition Imminent."
|- **Strategic Action:** 
    - Pivot long-term capital allocation into "Wet-Quantum" and "ZK-Infrastructure" domestic sectors.
    - Recalibrate geopolitical risk models to account for the state's immunity to traditional "Choke-Point Diplomacy."
    - Increase weighting of domestic "Bio-Digital" assets.
"""
