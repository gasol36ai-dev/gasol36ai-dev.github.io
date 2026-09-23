---
title: 'High-Density Report: Post-Quantum Cryptographic (PQC) Migration in Global Finance'
description: 'The transition to Post-Quantum Cryptography (PQC) is a systemic imperative for the global financial sector. The emergence of a Cryptographic'
pubDate: 2026-06-19
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/pqc_finance_migration.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# High-Density Report: Post-Quantum Cryptographic (PQC) Migration in Global Finance

## 1. Executive Summary
The transition to Post-Quantum Cryptography (PQC) is a systemic imperative for the global financial sector. The emergence of a Cryptographically Relevant Quantum Computer (CRQC) threatens the fundamental trust anchors of financial settlement: asymmetric encryption (RSA, ECC) and digital signatures. The primary risk is not merely future decryption, but the **"Store Now, Decrypt Later" (SNDL)** paradigm and the potential for systemic collapse of settlement layers if migration is non-uniform.

---

## 2. Transmission Mapping: Systemic Risk & Impact
The following mappings trace the path from quantum capability to financial instability.

### A. The Trust Collapse Path
**[CRQC Emergence]** $\rightarrow$ **[Shor's Algorithm execution on RSA/ECC]** $\rightarrow$ **[Instantaneous invalidation of digital signatures]** $\rightarrow$ **[Failure of Non-Repudiation in Settlement]** $\rightarrow$ **[Settlement Freeze]**
*   *Detail:* If a CRQC can forge signatures for RTGS (Real-Time Gross Settlement) systems, the authenticity of multi-billion dollar transfers cannot be verified. To prevent catastrophic fraudulent drains, central banks would be forced to freeze liquidity, halting global trade.

### B. The Data Exposure Path (SNDL)
**[Current Encrypted Traffic Capture]** $\rightarrow$ **[Quantum Decryption of Legacy TLS/VPN]** $\rightarrow$ **[Exposure of Historical Transactional Metadata]** $\rightarrow$ **[Market Manipulation/Corporate Espionage]** $\rightarrow$ **[Systemic Trust Erosion]**
*   *Detail:* Adversaries are currently harvesting encrypted data. Once a CRQC exists, historical data on sovereign bond movements or private equity deals becomes transparent, allowing for retroactive market analysis and strategic manipulation of current positions.

### C. The Infrastructure Bottleneck Path
**[PQC Algorithm Deployment]** $\rightarrow$ **[Increased Key/Signature Sizes (e.g., ML-KEM, ML-DSA)]** $\rightarrow$ **[Packet Fragmentation & HSM Buffer Overflows]** $\rightarrow$ **[Latency Spikes in High-Frequency Trading/Settlement]** $\rightarrow$ **[Operational Desynchronization]**
*   *Detail:* PQC keys are significantly larger than ECC keys. Legacy Hardware Security Modules (HSMs) and network protocols may experience buffer overflows or severe latency, causing timing-based failures in synchronized settlement windows (e.g., CLS).

### D. The Migration Asymmetry Path
**[Partial Network PQC Adoption]** $\rightarrow$ **[Downgrade Attacks/Fallback to Legacy Crypto]** $\rightarrow$ **[Creation of "Quantum Weak Points" in the Chain]** $\rightarrow$ **[Targeted Attack on Least-Secure Node]** $\rightarrow$ **[Cascading Failure of Interbank Trust]**
*   *Detail:* If Tier-1 banks migrate but Tier-3 regional banks do not, the entire settlement chain remains vulnerable. Attackers will target the legacy nodes to inject fraudulent instructions into the global stream, compromising the integrity of the entire network.

---

## 3. Impact on Financial Settlement Layers

### 3.1 RTGS and Large-Value Payment Systems (LVPS)
*   **Risk:** Total reliance on PKI for authentication and integrity.
*   **Mechanism:** If the root Certificate Authority (CA) is compromised via quantum attack, the entire hierarchy of trust in a central bank's settlement system vanishes.
*   **Reaction:** Transition to **"Hybrid Signatures"** (combining classical and PQC signatures) to maintain backward compatibility while ensuring quantum resistance.

### 3.2 SWIFT and Messaging Networks
*   **Risk:** Long-lived session keys and historical message archives.
*   **Mechanism:** SNDL attacks on the SWIFT network could expose decades of interbank communication, revealing strategic liquidity patterns.
*   **Reaction:** Rapid adoption of Quantum Key Distribution (QKD) for backbone fiber links and PQC for end-to-end messaging.

### 3.3 Digital Assets and Distributed Ledgers (DLT)
*   **Risk:** Public keys are often exposed on-chain (Address = Hash(PubKey)).
*   **Mechanism:** Once a transaction is initiated, the PubKey is revealed. A CRQC can derive the PrivateKey from the PubKey before the transaction is mined/confirmed, allowing for "front-running" theft of funds.
*   **Reaction:** Shift to hash-based signatures (e.g., XMSS, LMS) which are inherently quantum-resistant.

---

## 4. Migration Strategy & Technical Requirements

### 4.1 The "Crypto-Agility" Framework
Financial institutions must move from "hard-coded" cryptography to an abstracted layer where algorithms can be swapped without rewriting core application logic.
*   **Implementation:** API-driven cryptographic providers and modular security architectures.
*   **Goal:** Ability to rotate from ML-KEM to an alternative if a specific PQC primitive is found to be weak.

### 4.2 Hybrid Implementation Roadmap
To avoid a "cliff-edge" failure, a hybrid approach is mandatory:
1.  **Phase 1: Quantum Inventory:** Mapping every instance of RSA/ECC across the entire estate (shadow IT, third-party APIs).
2.  **Phase 2: Hybrid Encapsulation:** Wrapping current TLS tunnels in PQC-encrypted layers to mitigate SNDL.
3.  **Phase 3: PQC Primary:** Switching to PQC as the primary trust anchor, with classical as the secondary fallback.
4.  **Phase 4: Classical Deprecation:** Full removal of vulnerable algorithms once the ecosystem achieves critical mass.

---

## 5. Systemic Risk Summary Table

| Risk Factor | Mechanism | Systemic Impact | Priority |
| :--- | :--- | :--- | :--- |
| **SNDL** | Harvest now, decrypt later | High (Long-term confidentiality) | Immediate |
| **Signature Forgery** | Shor's $\rightarrow$ Private Key derivation | Critical (Immediate Liquidity Risk) | High |
| **HSM Obsolescence** | Key size $\rightarrow$ Memory exhaustion | Medium (Operational Downtime) | Medium |
| **Interop Gap** | Mixed PQC/Classical environment | High (Entry point for attackers) | High |
