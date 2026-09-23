---
title: 'Harvest Now, Decrypt Later (HNDL)'
description: '"Harvest Now, Decrypt Later" (HNDL) is a cyber-attack strategy where an adversary captures and archives encrypted data today, with the inten'
pubDate: 2026-07-10
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/HNDL.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Harvest Now, Decrypt Later (HNDL)

## Definition
**Category:** Threat Modeling
**Related to:** QRSF, Intelligence, Cybersecurity

"Harvest Now, Decrypt Later" (HNDL) is a cyber-attack strategy where an adversary captures and archives encrypted data today, with the intention of decrypting it in the future once a sufficiently powerful quantum computer (a Cryptographically Relevant Quantum Computer, or CRQC) becomes available.

## Application to Sovereign Finance
- **Strategic Debt**: National treasuries communicate long-term debt strategies and diplomatic financial agreements. If these are harvested today, a quantum-capable adversary could uncover sovereign secrets decades after the communication occurred.
- **Secret Accounts**: Diplomatic funds or clandestine financial operations relying on current encryption can be retroactively exposed.
- **Long-term Obligations**: Financial instruments with 30-year maturities are particularly vulnerable, as the "harvesting" window overlaps with the expected arrival of CRQC.

## Transmission Mapping
`[Encrypted Sovereign Data Stream] -> [Adversary Capture & Cold Storage] -> [CRQC Emergence] -> [Retroactive Decryption] -> [Strategic Intelligence Exposure]`

## Core Logic: The Quantum Vulnerability Window
The risk is defined by the **Quantum Threat Timeline**:
$$\text{Exposure Risk} = (\text{Data Secrecy Duration}) + (\text{Harvesting Window}) > (\text{Time to CRQC})$$
If the required secrecy of the data exceeds the time remaining until a CRQC is realized, the data is effectively "compromised" the moment it is harvested.

## Mitigation Strategies
- **Immediate Adoption of PQC**: Transitioning to post-quantum algorithms (e.g., CRYSTALS-Kyber) now to ensure that today's traffic is quantum-safe.
- **Hybrid Encryption**: Using a combination of classical and quantum-safe keys to ensure a baseline of security during the transition.
- **Quantum Key Distribution (QKD)**: Utilizing physical quantum properties (e.g., photon polarization) to create keys that are immune to harvesting and decryption by any future computer.
