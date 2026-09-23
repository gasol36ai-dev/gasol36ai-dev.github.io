---
title: 'PQC-Finance: Post-Quantum Cryptography in Global Finance (2025-2026 Report)'
description: 'As of mid-2026, the intersection of quantum computing advancements and global financial stability has become a paramount concern for regulat'
pubDate: 2026-06-05
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/PQC_Finance_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# PQC-Finance: Post-Quantum Cryptography in Global Finance (2025-2026 Report)

## Executive Summary

As of mid-2026, the intersection of quantum computing advancements and global financial stability has become a paramount concern for regulators, central banks, and systemic financial institutions. The threat posed by future cryptographically relevant quantum computers (CRQCs) to current public-key infrastructure (PKI) is driving a global transition toward Post-Quantum Cryptography (PQC). This report outlines the recent breakthroughs in NIST standardization, the projected migration timelines for Central Bank Digital Currencies (CBDCs), and the critical implications for the security of sovereign debt and global bond markets.

---

## 1. NIST PQC Standardization: 2025-2026 Breakthroughs

The National Institute of Standards and Technology (NIST) has entered a decisive phase in its Post-Quantum Cryptography Standardization Process.

### 1.1 The Third Round of Additional Digital Signatures
In May 2026, NIST announced the selection of nine candidates to advance to the third round of the "Additional Digital Signatures" evaluation process. This follows an intensive 18-month review of the second round.
- **Objective:** To widen the pool of available tools, ensuring diversity in cryptographic primitives (e.g., lattice-based, code-based, and multivariate-quadratic) to mitigate the risk of a single mathematical breakthrough breaking all PQC standards.
- **Timeline:** The third round of evaluation is expected to last approximately two years, focusing on technical specification updates and software implementation robustness.
- **Expected Outcome:** A finalized set of standardized digital signature algorithms that can secure everything from identity management to document signing in a post-quantum era.

### 1.2 Long-Term Deprecation Targets
NIST continues to advocate for a rapid transition, with a target to deprecate current quantum-vulnerable algorithms (such as RSA and ECC) by 2035. The 2025-2026 period marks the critical "implementation readiness" phase, where organizations must move from theoretical planning to pilot implementations.

---

## 2. Central Bank Digital Currencies (CBDCs) and Migration Timelines

The rise of CBDCs adds a new layer of complexity to the PQC transition. Because CBDCs are intended to be the bedrock of future digital economies, their cryptographic foundation must be quantum-resistant from inception.

### 2.1 Regulatory Drivers and EU Roadmaps
In the European Union, the transition is being accelerated by stringent regulatory frameworks:
- **DORA (Digital Operational Resilience Act) & NIS2:** These regulations mandate that financial entities demonstrate high levels of operational resilience, which increasingly includes preparing for quantum threats.
- **EU Coordinated Roadmap:** The EU has established a timeline where Member States are encouraged to initiate PQC transition activities by the **end of 2026**.
- **High-Risk Systems:** Critical financial infrastructure, including the backbone of CBDC networks, is expected to be secured with PQC by **2030**.

### 2.2 The Necessity of Crypto-Agility
For CBDC implementations, "crypto-agility"—the ability to swap cryptographic algorithms without overhaul of the entire system—is no longer a luxury but a requirement. Central banks are prioritizing hybrid schemes (combining classical and PQC algorithms) during the 2025-2026 window to ensure security during the transitional period.

---

## 3. Impact on Sovereign Debt and Bond Security

The security of sovereign debt and bond markets is uniquely vulnerable to the "Harvest Now, Decrypt Later" (HNDL) threat.

### 3.1 The "Harvest Now, Decrypt Later" (HNDL) Threat
Nation-state actors are currently intercepting and storing encrypted high-value communications and financial data. While they cannot decrypt this data today, the arrival of a CRQC would allow them to retrospectively expose:
- **Sovereign Debt Terms:** Confidential negotiations and strategic economic data.
- **Bond Issuance Protocols:** The integrity of the digital signatures used to authorize massive sovereign debt movements.
- **Ownership Records:** Long-term identity and ownership data related to global bond holdings.

### 3.2 Impact on Market Integrity
A successful quantum attack on the cryptographic signatures securing bond markets could lead to:
- **Unauthorized Issuance:** Forged digital signatures could allow attackers to issue fraudulent sovereign debt.
- **Settlement Disruption:** The inability to verify the authenticity of transaction messages could freeze global liquidity.
- **Erosion of Trust:** The fundamental trust required for sovereign debt markets—that obligations are legitimate and immutable—would be compromised.

---

## 4. Strategic Recommendations for Financial Institutions

To mitigate these risks, systemic institutions should adopt the following posture in 2026:

1. **Cryptographic Inventory:** Complete a comprehensive audit of all hardware and software utilizing asymmetric encryption.
2. **Hybridization:** Implement hybrid cryptographic protocols (e.g., TLS with both X25519 and ML-KEM) to provide immediate defense-in-depth.
3. **Vendor Management:** Demand PQC roadmaps from all critical third-party providers (Cloud, SWIFT, Payment Processors).
4. **Agility Testing:** Regularly test the ability to update cryptographic modules via automated orchestration.

## Conclusion

The 2025-2026 period represents a critical inflection point. As NIST moves toward final standardization and central banks outline their CBDC security mandates, the financial sector must accelerate its migration to prevent a catastrophic compromise of global economic sovereignty and the integrity of the world's debt markets.
