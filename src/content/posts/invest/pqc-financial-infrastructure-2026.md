---
title: 'Post-Quantum Cryptographic Financial Infrastructure (PQC-FI)'
description: 'Post-Quantum Cryptographic Financial Infrastructure (PQC-FI) refers to the systemic overhaul of the global financial system''s cryptographic …'
pubDate: 2026-06-09
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/PQC_Financial_Infrastructure_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Post-Quantum Cryptographic Financial Infrastructure (PQC-FI)

## Executive Summary
Post-Quantum Cryptographic Financial Infrastructure (PQC-FI) refers to the systemic overhaul of the global financial system's cryptographic primitives to resist attacks from future cryptographically relevant quantum computers (CRQCs). The transition is driven by the vulnerability of current asymmetric encryption (RSA, ECC) to Shor's algorithm, which threatens the integrity of payment settlements, asset ownership, and confidential financial communications. By 2026, the focus has shifted from theoretical research to the implementation of NIST's finalized PQC standards (FIPS 203, 204, 205) and the pursuit of "crypto-agility" across systemic financial institutions.

## 1. The Quantum Threat to Financial Stability
The financial sector relies heavily on Public Key Infrastructure (PKI) for secure transactions and data integrity. Quantum computing introduces two primary threats:
- **Shor's Algorithm:** Capable of efficiently factoring large integers and solving discrete logarithms, rendering RSA, Diffie-Hellman, and Elliptic Curve Cryptography (ECC) obsolete.
- **Grover's Algorithm:** Reduces the effective security of symmetric encryption (AES) and hash functions, necessitating longer key lengths (e.g., migrating from AES-128 to AES-256).
- **"Harvest Now, Decrypt Later" (HNDL):** Adversaries are currently collecting encrypted financial data and long-term secrets to decrypt them once a CRQC becomes available. This is a critical risk for long-dated financial instruments and sovereign secrets.

## 2. Technical Foundations: NIST PQC Standards (2024-2026)
The transition to PQC-FI is anchored by the standards released by the National Institute of Standards and Technology (NIST) in August 2024:
- **ML-KEM (FIPS 203):** A Module-Lattice-Based Key-Encapsulation Mechanism used for secure key exchange. It replaces DH and ECDH.
- **ML-DSA (FIPS 204):** A Module-Lattice-Based Digital Signature Standard used for identity verification and transaction signing. It replaces RSA and ECDSA.
- **SLH-DSA (FIPS 205):** A Stateless Hash-Based Digital Signature Standard. While slower than ML-DSA, it provides a robust backup based on different mathematical assumptions (hash functions rather than lattices).

## 3. Quantum-Resistant Settlement Systems
Financial settlement systems (RTGS, SWIFT, FedWire) must migrate to PQC to prevent fraudulent transactions and systemic collapse.
- **Messaging Security:** Transitioning interbank messaging protocols to use hybrid key exchanges (e.g., X25519 + ML-KEM) to ensure that if one algorithm is compromised, the other remains secure.
- **Settlement Finality:** Ensuring that digital signatures on high-value settlement instructions are quantum-resistant to prevent "quantum forgery" of payments.
- **Hybrid PKI:** Implementation of dual-certificate chains where a single identity is bound to both a classical (ECC) and a quantum-resistant (ML-DSA) key, allowing for a gradual rollout across diverse global jurisdictions.

## 4. PQC-Secured Blockchain and DLT
Distributed Ledger Technology (DLT) faces unique challenges due to the immutable nature of the chain and the way public keys are handled.
- **The "Public Key Leak" Problem:** In many blockchains (e.g., Bitcoin), the public key is only revealed when a transaction is sent. However, once revealed, a quantum computer could derive the private key and steal funds before the transaction is mined.
- **Migration Strategies:**
    - **Account Migration:** Users must move funds from legacy (ECDSA) addresses to new PQC addresses (using ML-DSA).
    - **Quantum-Resistant Signatures:** Integration of lattice-based or hash-based signatures into the consensus layer.
- **Hard Forks:** The necessity of network-wide upgrades to support larger PQC signature sizes, which may increase block sizes and impact latency.

## 5. Migration Risks and Implementation Challenges
The path to PQC-FI is fraught with operational and technical risks:
- **Crypto-Agility:** The ability of a system to switch cryptographic algorithms without requiring significant changes to the underlying infrastructure. Most legacy financial systems lack this agility.
- **Performance Overheads:** PQC keys and signatures are typically larger than their classical counterparts. This requires updates to packet sizes in network protocols and database schemas for storing keys.
- **Legacy Dependencies:** Many core banking systems run on COBOL or other legacy languages where updating cryptographic libraries is complex and carries high regression risk.
- **Coordination Failure:** Because financial infrastructure is global, a "weak link" (e.g., a small but critical clearing house) that fails to migrate could expose the entire network to risk.

## 6. Global Standard Shifts and Regulatory Landscape
- **NIST (USA):** Setting the primary technical standards (FIPS 203/204/205).
- **BIS (Bank for International Settlements):** Coordinating central bank efforts to ensure the resilience of the global financial core.
- **ISO/IEC:** Standardizing the integration of PQC into broader IT security frameworks.
- **Regulatory Mandates:** Expectation of mandates by 2027-2030 requiring systemic financial institutions (SIFIs) to provide a "Quantum Migration Roadmap" as part of their operational resilience filings.

## 7. Roadmap to 2035
- **2024-2026:** Inventory of vulnerable assets; adoption of hybrid modes; pilot testing of ML-KEM/ML-DSA in non-critical paths.
- **2027-2030:** Mass migration of high-value settlement systems; mandatory transition of root CAs to PQC.
- **2031-2035:** Phase-out and deprecation of RSA and ECC; full operationalization of PQC-FI.

---
*Last Updated: June 2026*
*Classification: Research Wiki / Financial Infrastructure*
