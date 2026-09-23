---
title: 'Wiki Entry: Quantum-Resistant Cryptography (PQC) & Sovereign Data Rails'
description: 'The transition from classical to post-quantum cryptography (PQC) is no longer a theoretical exercise but a national security imperative. The'
pubDate: 2026-06-02
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/PQC_Sovereign_Data_Rails_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Wiki Entry: Quantum-Resistant Cryptography (PQC) & Sovereign Data Rails

## Executive Summary
The transition from classical to post-quantum cryptography (PQC) is no longer a theoretical exercise but a national security imperative. The emergence of **Cryptanalytically Relevant Quantum Computers (CRQCs)** threatens the foundational asymmetric encryption (RSA, ECC) that secures global finance, government communications, and national digital identities. To mitigate this, nations are developing **Sovereign Data Rails**—digitally independent infrastructure and "Sovereign Trust Layers"—that integrate NIST-standardized PQC algorithms to ensure long-term data sovereignty and systemic resilience.

---

## 1. The Quantum Threat & PQC Standards
### The "Harvest Now, Decrypt Later" (HNDL) Risk
The primary driver for immediate PQC adoption is the **HNDL attack vector**. Adversaries are currently capturing encrypted sensitive data (government secrets, financial records) with the intent to decrypt it once a CRQC becomes available. This makes the "quantum horizon" a present-day vulnerability for any data with a secrecy requirement exceeding 5–10 years.

### NIST Standardization (The New Baseline)
The National Institute of Standards and Technology (NIST) has finalized the first set of PQC standards to replace classical public-key cryptography:
*   **ML-KEM (formerly Kyber):** For general encryption (key encapsulation).
*   **ML-DSA (formerly Dilithium):** For digital signatures.
*   **SLH-DSA (formerly SPHINCS+):** A stateless hash-based signature scheme.
*   **Falcon (FIPS 206):** A lattice-based signature scheme currently in development.

---

## 2. Sovereign Data Rails & National Infrastructure
### Defining Sovereign Data Rails
"Sovereign Data Rails" refer to the underlying digital public infrastructure (DPI)—including payment systems, identity layers, and cloud environments—that a state controls independently of foreign providers. This ensures that the **"Trust Layer"** of a nation's digital economy is not subject to foreign kill-switches or surveillance.

### The Sovereign Trust Layer
To prevent a systemic collapse of trust, nations are implementing a **Sovereign Trust Layer**. This architecture integrates:
*   **Quantum-Resistant Encryption:** Replacing vulnerable SSL/TLS and VPN protocols.
*   **Quantum Randomness:** Using Quantum Random Number Generators (QRNG) to ensure entropy cannot be predicted by quantum adversaries.
*   **Local Control:** Hosting cryptographic keys and root certificates within national borders to avoid dependency on external Certificate Authorities (CAs).

---

## 3. PQC in CBDCs and Financial Systems
Central Bank Digital Currencies (CBDCs) represent the highest-stakes application of PQC due to their role in national monetary sovereignty.

### The BIS Approach & Project Tourbillion
The Bank for International Settlements (BIS) and various central banks (e.g., Bank of France, Bundesbank) have conducted tests in live-like payment systems (such as TARGET2) to validate PQC. **Project Tourbillion** specifically explored the intersection of PQC, privacy, and scalability for CBDCs.

### Post-Quantum Financial Infrastructure Framework (PQFIF)
The PQFIF is emerging as a blueprint for the financial sector, emphasizing:
*   **Verifiable Transition:** A phased roadmap for regulated institutions to migrate digital assets to PQC standards.
*   **Quantum-Resilient Privacy Ledgers (QRPL):** Research into combining NIST PQC with **Hash-based Zero-Knowledge Proofs (ZKP)** to allow for transaction confidentiality and selective disclosure without compromising the ledger's quantum security.
*   **Hybrid Signatures:** The temporary use of "dual-signatures" (classical + PQC) to maintain backward compatibility while securing against future quantum threats.

---

## 4. Strategic Migration Framework
The transition is characterized by a shift from "static security" to **"cryptographic agility."**

### The Migration Roadmap (2024–2035)
Most national roadmaps (US CNSA 2.0, EU, Canada) target full quantum-resistance by **2030–2035**. The process follows three main phases:
1.  **Discovery & Inventory:** Using **Cryptographic Bills of Materials (CBOMs)** and automated discovery tools to map every instance of RSA/ECC across the infrastructure.
2.  **Prioritization:** Identifying "High Value Assets" (HVAs) and data with long-term sensitivity (HNDL risk) for immediate migration.
3.  **Agile Deployment:** Implementing a modular architecture where algorithms can be swapped without rewriting the entire software stack (**Crypto-Agility**).

### Summary Table: Classical vs. Post-Quantum Infrastructure

| Component | Classical Infrastructure | Sovereign PQC Infrastructure |
| :--- | :--- | :--- |
| **Primary Algorithms** | RSA, ECDSA, Diffie-Hellman | ML-KEM, ML-DSA, SLH-DSA |
| **Trust Model** | Global/Foreign CAs | National Sovereign Trust Layers |
| **Data Risk** | Susceptible to HNDL | Quantum-Safe from inception |
| **Flexibility** | Hard-coded primitives | Cryptographic Agility (Modular) |
| **CBDC Design** | Standard DLT / Centralized DB | PQC-DLT with ZKP Privacy |

## Conclusion
The transition to PQC is not a simple software update; it is a fundamental re-architecting of national trust. By building **Sovereign Data Rails**, nations are ensuring that their digital financial systems (CBDCs) and critical infrastructure remain secure and autonomous in an era where the mathematical assumptions of the last 40 years are no longer valid.

***

**Transmission Mapping**:
`[Advancement in Quantum Cryptanalysis] -> [NIST PQC Standardization] -> [Sovereign Data Rail Deployment] -> [Long-term National Digital Sovereignty]`
