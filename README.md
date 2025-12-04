 AES Image Encryption Project
COMP453 – Cryptography Course

This project demonstrates the encryption and decryption of BMP images using the AES algorithm in three different modes of operation:

ECB (Electronic Codebook)

CBC (Cipher Block Chaining)

CTR (Counter Mode)

The goal is to observe visual differences, analyze security properties, measure performance, and compute reconstruction quality using PSNR.

🚀 Features

🔄 Convert BMP image → byte array → BMP image

🔐 Encrypt image data using AES (ECB/CBC/CTR)

🔓 Decrypt ciphertext back into the original image

🧮 Calculate PSNR (Peak Signal-to-Noise Ratio)

⏱️ Measure encryption/decryption time for each mode

📊 Compare visual results of encrypted images

📁 Project Structure
📦 Cryptography_Project
 ├── Main.py
 ├── aes_functions.py
 ├── images/
 │     ├── penguin.bmp
 │     ├── restored_penguin.bmp
 │     ├── ECB_encrypted.bmp
 │     ├── CBC_encrypted.bmp
 │     ├── CTR_encrypted.bmp
 │     ├── ECB_decrypted.bmp
 │     ├── CBC_decrypted.bmp
 │     └── CTR_decrypted.bmp
 └── README.md

🛠️ Technologies Used

Python 3

PyCryptodome (AES encryption)

NumPy

Pillow (PIL) for image handling

📌 AES Modes Summary
🔹 ECB Mode

Each block encrypted independently

Fast, but leaks image patterns

Not suitable for image encryption

🔹 CBC Mode

Introduces chaining and IV

Patterns completely removed

More secure, slightly slower

🔹 CTR Mode

Stream-like operation using counter

Best performance

Highly secure, no visible artifacts

▶️ How to Run

Install dependencies:

pip install pycryptodome pillow numpy


Run the main script:

python Main.py


Output images will be generated in the images/ folder.

📊 Outputs Generated

Encrypted BMP images (ECB, CBC, CTR)

Decrypted BMP images for all modes

Restored original image

Console output with:

Encryption time

Decryption time

PSNR values

🧪 Example Results (Sample)
Mode	Encrypt Time	Decrypt Time	PSNR
ECB	~0.002s	~0.000s	100
CBC	~0.003s	~0.000s	100
CTR	~0.002s	~0.001s	100
📝 Conclusion

This project demonstrates that:

ECB is insecure due to pattern leakage

CBC eliminates visual patterns, offering strong security

CTR is the fastest mode while maintaining security

AES encryption/decryption is lossless, confirmed by PSNR = 100

Overall, CBC and CTR are well-suited for image encryption, while ECB should be avoided.
