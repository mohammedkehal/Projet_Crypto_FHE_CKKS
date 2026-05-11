# 🛡️ Zero-Trust Financial Scoring Architecture (FHE CKKS)

This project implements a fully functional Zero-Trust architecture for financial credit scoring using **Fully Homomorphic Encryption (FHE)**. It allows a Cloud FinTech to evaluate an AI model on encrypted client data without ever decrypting it, strictly preserving banking secrecy.

## 🚀 Features
* **Post-Quantum Cryptography:** Utilizes the RLWE (Ring Learning With Errors) problem.
* **CKKS Scheme:** Natively handles floating-point real numbers, crucial for financial ratios.
* **End-to-End Encryption:** Strict separation between the Trusted Banking Enclave and the Untrusted Cloud.
* **SOC Command Center:** A real-time, interactive dashboard built with Streamlit to monitor cryptographic telemetry and 3D polynomial noise.

## 🛠️ Tech Stack
* **Language:** Python
* **Cryptography:** TenSEAL (Microsoft SEAL wrapper)
* **Frontend/SOC:** Streamlit, Plotly (for 3D data visualization)
* **Infrastructure:** Docker (Containerized for absolute environment isolation)

## 🏗️ Architecture Flow
1. **Bank Client (Local):** Encodes financial data (Revenues, Debts) and encrypts it using the public key.
2. **Cloud FinTech (Untrusted):** Performs blind AI inference (dot products) directly on the ciphertexts.
3. **Bank Client (Local):** Decrypts the output using the secret key to reveal the final credit score.

## 👨‍💻 Author
**Mohammed KEHAL** |
**Zineb CHAFIK** |
**Ossama EL KHALFI**

*Project developed within the Master's program in Computer Engineering and Systems Security (2I2S).*
