from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter


# --------------------------------------------------
# AES ECB
# --------------------------------------------------
def aes_encrypt_ecb(image_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(image_data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data


def aes_decrypt_ecb(encrypted_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data


# --------------------------------------------------
# AES CBC
# --------------------------------------------------
def aes_encrypt_cbc(image_data, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(image_data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return iv + encrypted_data   # IV önce gönderilir


def aes_decrypt_cbc(encrypted_data, key):
    iv = encrypted_data[:16]              # ilk 16 byte = IV
    ciphertext = encrypted_data[16:]      # geri kalanı = gerçek şifre
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(ciphertext)
    decrypted_data = unpad(decrypted_padded, AES.block_size)
    return decrypted_data


# --------------------------------------------------
# AES CTR
# --------------------------------------------------
def aes_encrypt_ctr(image_data, key):
    ctr = Counter.new(128)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    encrypted_data = cipher.encrypt(image_data)
    return encrypted_data


def aes_decrypt_ctr(encrypted_data, key):
    ctr = Counter.new(128)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data
