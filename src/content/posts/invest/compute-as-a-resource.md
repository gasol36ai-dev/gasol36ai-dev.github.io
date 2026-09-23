---
title: 'Compute-as-a-Resource (CaaR)'
description: 'CaaR implements a three-layer stack to commoditize compute:'
pubDate: 2026-07-07
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/compute_as_a_resource.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Compute-as-a-Resource (CaaR)

## Definition
**Compute-as-a-Resource (CaaR)** is an economic and technical framework that treats raw computational power—specifically FLOPs and hardware capacity (GPUs, TPUs, NPUs)—as a tokenized, liquid commodity. It shifts the paradigm from "Cloud Leasing" (centralized) to "Resource Liquidity" (decentralized).

## Technical Details
CaaR implements a three-layer stack to commoditize compute:
1. **Hardware Layer (The RWA):** Physical GPU clusters are tokenized as Real-World Assets (RWAs). Each token represents a specific slice of compute capacity (e.g., 1 H100-hour).
2. **Utility Layer (The Market):** A decentralized exchange (DEX) for compute. Users buy or lease compute tokens to execute workloads. The network uses "proof-of-compute" or verifiable computation (ZK-proofs) to ensure the work was actually performed.
3. **Yield Layer (The Investment):** Token holders who provide compute to the network receive a portion of the leasing fees, turning hardware ownership into a yield-generating financial asset.

## Use Cases
- **Fractionalized Capex:** Allowing small labs or startups to access high-end H100 clusters by purchasing fractional compute tokens rather than investing millions in hardware.
- **Dynamic Load Balancing:** Automatically routing AI training jobs to the cheapest available compute tokens globally, optimizing for cost and energy efficiency.
- **Sovereign Compute Pools:** A state can create a national compute reserve by tokenizing all public-sector GPUs into a single CaaR pool, ensuring strategic priority for critical national projects.

## Sovereign Implications
- **Breaking Cloud Monopolies:** CaaR reduces the strategic leverage of "Hyperscalers" (AWS, Azure, GCP) by creating a competitive, liquid market for raw compute.
- **Compute Autarky:** By tokenizing and optimizing internal resources, a state can maximize its "computational GDP," ensuring that no FLOP is wasted.
- **Financialization of Intelligence:** CaaR turns compute into a new asset class, where the value of a token is tied directly to the demand for AI inference and training.

## Related Concepts
- [[Sovereign_Compute_Autarky_2026]]
- [[RWA_Capital_Sovereignty]]
- [[Sovereign_Compute_DePIN]]
