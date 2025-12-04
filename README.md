# AES Image Encryption Project  
### COMP453 – Cryptography Course

This project implements AES-based encryption and decryption of BMP images using three different block cipher modes: **ECB**, **CBC**, and **CTR**. The objective is to analyze the security, visual differences, performance, and reconstruction quality (PSNR) of each mode.

---

## 1. Overview

The project performs the following operations:

- Converts a BMP image to a byte array and restores it  
- Encrypts image data using AES (ECB, CBC, CTR)  
- Decrypts ciphertext to reconstruct the original image  
- Computes **PSNR (Peak Signal-to-Noise Ratio)**  
- Measures encryption/decryption time  
- Generates encrypted & decrypted BMP images  

This project highlights why some AES modes (e.g., **ECB**) are insecure for image encryption.

---

## 2. Features

- 🔄 BMP → Byte Array → BMP Reconstruction  
- 🔐 AES Encryption (ECB, CBC, CTR)  
- 🔓 AES Decryption  
- 🧮 PSNR Calculation  
- ⏱️ Performance Measurement  
- 📊 Visual comparison of encrypted images  
- 💾 Auto-generated output files in the `images/` directory  

---

## 3. Project Structure
📦 Cryptography_Project
├── Main.py
├── aes_functions.py
├── images/
│ ├── penguin.bmp
│ ├── restored_penguin.bmp
│ ├── ECB_encrypted.bmp
│ ├── CBC_encrypted.bmp
│ ├── CTR_encrypted.bmp
│ ├── ECB_decrypted.bmp
│ ├── CBC_decrypted.bmp
│ └── CTR_decrypted.bmp
└── README.md


---

## 4. Technologies Used

- Python 3  
- PyCryptodome (AES implementation)  
- Pillow (PIL) for BMP processing  
- NumPy for numerical operations  

---

## 5. AES Modes Summary

### 5.1 ECB – Electronic Codebook
- Encrypts each block independently  
- Fast but leaks visual patterns  
- **Not suitable for image encryption**

### 5.2 CBC – Cipher Block Chaining
- Uses IV and chaining  
- Eliminates image patterns  
- More secure but slightly slower  

### 5.3 CTR – Counter Mode
- Turns AES into a stream cipher  
- Best performance  
- Secure and pattern-free  
- Parallelizable  

---

## 6. How to Run

### Install Dependencies
\`\`\`bash
pip install pycryptodome pillow numpy
\`\`\`

### Run
\`\`\`bash
python Main.py
\`\`\`




