---
title: 'Proprietary Judgment Indicator: Clustered Flow Regime Gate (CFRG)'
description: 'The CFRG indicator is a next-generation execution filter that replaces raw LOB imbalance signals with intent-classified clustered flow, gate'
pubDate: 2026-05-26
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/CFRG_Indicator_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Judgment Indicator: Clustered Flow Regime Gate (CFRG)

## Overview
The CFRG indicator is a next-generation execution filter that replaces raw LOB imbalance signals with **intent-classified clustered flow**, gated by macro regime context. It synthesizes three research domains: Clustered Flow theory, TradeFM's universal microstructure model, and the KKR "Security of Everything" macro thesis.

## Motivation
Previous proprietary indicators (LVD, ALVC, SLC) focused on *detecting* liquidity stress. The CFRG is different: it is an **execution quality filter** — it tells you *when* a trade signal has high-quality structural support vs. when it is a noise artifact of the current macro regime.

## Framework (Map-Trigger-Lock)

### Map (Macro Regime Context)
Establish the macro regime using two binary flags:
- `POLICY_PARALYSIS`: Is the Fed in an asymmetric reaction function? (Yes if: Fed funds futures pricing >30bp dispersion over 6 months AND Hormuz risk premium elevated)
- `RESOURCE_WEAPONIZATION`: Is there active supply-chain fragmentation? (Yes if: shipping indices diverging from historical norms OR USTR Section 301 active)

**Regime State**: `{PP: bool, RW: bool}` → One of four quadrants (Risk-On, Stagflation Trap, Transition, Risk-Off)

### Trigger (Execution Signal)
The trade signal is **only valid** if Clustered Flow agrees:
1. Compute raw LOB imbalance (bid-ask delta).
2. Compute Clustered Flow imbalance (semantic intent clusters over 15-min windows).
3. **Gate condition**: `Clustered Flow Signal` must confirm `Raw LOB Signal`. If they diverge, the signal is classified as **noise** and suppressed.
4. `CF_CONFIRM = (sign(ClusteredFlow) == sign(RawLOB)) AND (|ClusteredFlow| > threshold)`

### Lock (Regime-Adaptive Confirmation)
Apply regime-specific confirmation requirement:
- **Stagflation Trap** (PP=True, RW=True): Require 2x standard confirmation bars. Reduce position size by 40%.
- **Risk-On** (PP=False, RW=False): Standard confirmation. Full position size.
- **Transition States**: Reduce position size by 20%.

**Lock condition**: `REGIME_WEIGHT * CF_CONFIRM * SLC_CLEAR`
Where `SLC_CLEAR = True` if the SLC (Structural Liquidity Curvature) indicator is not in a flash-crash warning state.

## Synthesis Formula
```
CFRG_Score = REGIME_WEIGHT(macro_quadrant) * CF_CONFIRM * SLC_CLEAR
```
- If `CFRG_Score >= 0.7`: Execute at full size.
- If `0.4 <= CFRG_Score < 0.7`: Execute at 50% size.
- If `CFRG_Score < 0.4`: Suppress signal entirely.

## Cross-Domain Isomorphism
This indicator synthesizes three research domains:
1. **Physical AI (DAWN WAIMs)**: The CFRG uses a bidirectional inference loop — Macro informs Micro, and Micro confirms Macro. Analogous to DAWN's co-evolution between world prediction and action generation.
2. **TradeFM**: Universal microstructure representations feed the Clustered Flow computation, enabling regime-invariant signal quality assessment.
3. **KKR/iAGAM Macro**: The Stagflation Trap regime state is derived directly from the "Policy Paralysis + Resource Weaponization" thesis.

## Historical Validation Hypothesis
In 2022 (Fed pivot + supply shock):
- Raw LOB signals generated many false positives during bond volatility spikes.
- A CFRG framework would have suppressed most of these (Stagflation regime → 40% size reduction + 2x confirmation bars).

In 2020 COVID crash:
- SLC would have triggered (flash-crash warning), locking CFRG_Score to < 0.4 and suppressing execution entirely on the worst days.

## Strategic Value
The CFRG is the first indicator in this system that:
1. **Integrates macro and micro** into a single decision gate.
2. **Adapts position sizing** based on regime context, not just signal strength.
3. **Prevents false positives** by requiring clustered flow confirmation of raw LOB signals.

*Created: 2026-05-26 | CTO Innovation Synthesis*
