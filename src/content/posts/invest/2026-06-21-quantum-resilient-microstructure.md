---
title: 'Research Report: Quantum-Resilient Financial Microstructure and PQC Impacts'
description: 'The emergence of Cryptographically Relevant Quantum Computers (CRQC) threatens the foundational security of the global financial system. Whi'
pubDate: 2026-06-21
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/2026-06-21_Quantum_Resilient_Microstructure.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Research Report: Quantum-Resilient Financial Microstructure and PQC Impacts

## 1. Executive Summary
The emergence of Cryptographically Relevant Quantum Computers (CRQC) threatens the foundational security of the global financial system. While much focus is placed on the "Quantum Apocalypse" of data breaches, the transition to Post-Quantum Cryptography (PQC) introduces immediate structural risks to financial microstructure. This report examines the "latency tax" imposed by PQC on High-Frequency Trading (HFT), the resulting degradation of market liquidity, and the systemic vulnerabilities of settlement rails.

## 2. Impacts on High-Frequency Trading (HFT)
HFT environments operate on nanosecond scales where the "tick-to-trade" latency is the primary competitive moat. The shift from Elliptic Curve Cryptography (ECC) to NIST-standardized PQC (e.g., ML-KEM, ML-DSA) introduces three critical bottlenecks:

### 2.1 Computational Latency (The CPU Tax)
PQC algorithms, particularly those based on Module-Lattice problems, are computationally more intensive than the ECC signatures they replace. 
- **Verification Overhead:** Even a 1-5 microsecond increase in the time required to verify a signed order at the exchange gateway can lead to massive queueing delays during high-volatility events.
- **Hardware Divergence:** We expect a bifurcation in the market where firms utilizing FPGA or ASIC-based PQC accelerators maintain an edge over those using software-defined PQC, increasing the barrier to entry.

### 2.2 Serialization and Bandwidth (The Payload Tax)
PQC signatures and public keys are significantly larger than classical ones.
- **Size Comparison:** An Ed25519 signature is 64 bytes; an ML-DSA (Dilithium) signature can exceed 2,400 bytes.
- **Network Jitter:** Increased payload sizes lead to higher serialization delay and a higher probability of packet fragmentation. In a microstructure sensitive to "micro-bursts," this increased bandwidth consumption can saturate exchange cross-connects, inducing non-deterministic jitter.

### 2.3 Determinism and Adverse Selection
The increased complexity of PQC processing can introduce timing variances (jitter). For market makers, this lack of determinism increases the risk of "adverse selection"—where a faster participant exploits a price move before the market maker can successfully verify and update their quotes.

## 3. Liquidity and Market Dynamics
The "Quantum Transition" will not be a synchronized event, leading to a period of cryptographic fragmentation.

### 3.1 Cost of Liquidity Provision
As the overhead of maintaining secure, quantum-resilient channels increases, the cost of providing liquidity rises. This is expected to manifest as:
- **Wider Bid-Ask Spreads:** Market makers will widen spreads to compensate for the increased technological overhead and the risk of latency-induced losses.
- **Reduced Order Book Depth:** To mitigate the risk of being "picked off" due to PQC-induced lag, firms may reduce the size of their quotes at the top of the book.

### 3.2 Structural Asymmetry
The transition creates a "Quantum Divide." Firms that can optimize PQC at the hardware level will essentially "own" the latency floor, potentially leading to a concentration of liquidity within a few ultra-fast, quantum-resilient entities, reducing overall market competitiveness.

## 4. Settlement Rails and Systemic Trust
Unlike HFT, settlement rails (RTGS, CSDs, and DLT) are less sensitive to microseconds but highly sensitive to the "Store Now, Decrypt Later" (SNDL) attack.

### 4.1 The SNDL Vulnerability
State actors are currently harvesting encrypted financial traffic. Once a CRQC is available, they can retrospectively decrypt historical settlement data, exposing sovereign debt movements, private corporate transfers, and strategic positions.

### 4.2 Trust Anchor Migration
Updating the "root of trust" across global settlement rails is a coordination nightmare. A failure in the transmission mapping (the protocol for moving from Classical $\\rightarrow$ Hybrid $\\rightarrow$ Pure PQC) could lead to:
- **Settlement Failures:** If a sender uses a PQC scheme that the receiver's gateway has not yet implemented.
- **Frozen Assets:** Inability to sign a transfer request due to key rotation mismatches.

## 5. Transmission Mapping: Quantum Risk Propagation
The following map traces how a quantum threat propagates from a theoretical capability to a microstructure failure:

**[ Quantum Threat: CRQC Capability ]**
$\downarrow$
**[ Cryptographic Collapse: ECC/RSA $\\rightarrow$ Obsolete ]**
$\downarrow$
$\\swarrow \\quad \\searrow$
**[ Path A: PQC Implementation ] $\\quad$ [ Path B: Non-Implementation ]**
$\downarrow \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\downarrow$
**[ Latency/Bandwidth Tax ] $\\quad$ [ Systemic Data Breach/SNDL ]**
$\downarrow \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\downarrow$
**[ Tick-to-Trade Delay $\\rightarrow$ Jitter ] $\\quad$ [ Loss of Settlement Integrity ]**
$\downarrow \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\downarrow$
**[ Adverse Selection $\\rightarrow$ Wider Spreads ] $\\quad$ [ Asset Theft / Market Panic ]**
$\downarrow \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\downarrow$
**[ $\\rightarrow$ Microstructure Degradation $\\leftarrow$ ]**
$\downarrow$
**[ Reduced Capital Efficiency & Increased Volatility ]**

## 6. Conclusion and Strategic Recommendations
Quantum resilience is not a software patch; it is a physical and structural reconfiguration of the financial pipeline. To mitigate these risks:
1. **Hardware Acceleration:** Exchanges and HFT firms must prioritize FPGA/ASIC implementations of ML-KEM and ML-DSA to keep the "latency tax" near zero.
2. **Hybridization:** Implement "Dual-Signature" regimes (Classical + PQC) to ensure stability during the multi-year transition period.
3. **SNDL Mitigation:** Immediate migration of long-term settlement data to PQC-encrypted tunnels to prevent retrospective decryption of systemic financial secrets.
