
import time as pytime

from PIL import Image
import numpy as np
from pygame import time

from aes_functions import aes_encrypt_ecb, aes_decrypt_ecb, aes_encrypt_cbc, aes_decrypt_cbc, aes_encrypt_ctr, \
    aes_decrypt_ctr
import math


def image_to_bytearray(path):
    img = Image.open(path)
    img = img.convert("RGB")
    width, height = img.size
    mode = img.mode

    img_array = np.array(img)
    img_bytes = img_array.tobytes()

    return img_bytes, width, height, mode


def bytearray_to_image(img_bytes, width, height, mode):
    channels = 3 if mode == "RGB" else 1
    img_array = np.frombuffer(img_bytes, dtype=np.uint8)
    img_array = img_array.reshape((height, width, channels))
    img = Image.fromarray(img_array, mode)
    return img

# --------------------------------------------------------
# PSNR CALCULATION
# --------------------------------------------------------
def psnr(original_image, decrypted_image):
    original = np.array(original_image)
    decrypted = np.array(decrypted_image)

    mse = np.mean((original - decrypted) ** 2)
    if mse == 0:
        return 100  # perfect decryption

    max_pixel = 255.0
    return 20 * math.log10(max_pixel / math.sqrt(mse))


# --------------------------------------------------------
# TIME MEASUREMENT FUNCTION
# --------------------------------------------------------
def measure_time(function, *args):
    start = pytime.time()
    result = function(*args)
    end = pytime.time()
    return result, (end - start)

# --------------------------------------------------------
# MAIN
# --------------------------------------------------------
if __name__ == "__main__":
    image_path = "images/penguin.bmp"

    img_bytes, w, h, mode = image_to_bytearray(image_path)
    original_image = Image.open(image_path).convert("RGB")

    print("Resim başarıyla yüklendi!")
    print("Boyut:", w, h)
    print("Mod:", mode)

    # ---------- Restore Test ----------
    restored = bytearray_to_image(img_bytes, w, h, mode)
    restored.save("images/restored_penguin.bmp")
    print("Restored BMP oluşturuldu.\n")

    key = b"1234567890ABCDEF"

    # ============================================================
    #                        ECB MODE
    # ============================================================
    encrypted_ecb, enc_time_ecb = measure_time(aes_encrypt_ecb, img_bytes, key)
    decrypted_ecb, dec_time_ecb = measure_time(aes_decrypt_ecb, encrypted_ecb, key)

    trimmed = encrypted_ecb[:len(img_bytes)]
    bytearray_to_image(trimmed, w, h, mode).save("images/ECB_encrypted.bmp")
    bytearray_to_image(decrypted_ecb, w, h, mode).save("images/ECB_decrypted.bmp")

    psnr_ecb = psnr(original_image, bytearray_to_image(decrypted_ecb, w, h, mode))

    print("---- ECB MODE ----")
    print("Encrypt time:", enc_time_ecb)
    print("Decrypt time:", dec_time_ecb)
    print("PSNR:", psnr_ecb)
    print("-------------------\n")

    # ============================================================
    #                        CBC MODE
    # ============================================================
    encrypted_cbc, enc_time_cbc = measure_time(aes_encrypt_cbc, img_bytes, key)
    decrypted_cbc, dec_time_cbc = measure_time(aes_decrypt_cbc, encrypted_cbc, key)

    trimmed = encrypted_cbc[16:16+len(img_bytes)]
    bytearray_to_image(trimmed, w, h, mode).save("images/CBC_encrypted.bmp")
    bytearray_to_image(decrypted_cbc, w, h, mode).save("images/CBC_decrypted.bmp")

    psnr_cbc = psnr(original_image, bytearray_to_image(decrypted_cbc, w, h, mode))

    print("---- CBC MODE ----")
    print("Encrypt time:", enc_time_cbc)
    print("Decrypt time:", dec_time_cbc)
    print("PSNR:", psnr_cbc)
    print("-------------------\n")

    # ============================================================
    #                        CTR MODE
    # ============================================================
    encrypted_ctr, enc_time_ctr = measure_time(aes_encrypt_ctr, img_bytes, key)
    decrypted_ctr, dec_time_ctr = measure_time(aes_decrypt_ctr, encrypted_ctr, key)

    trimmed = encrypted_ctr[:len(img_bytes)]
    bytearray_to_image(trimmed, w, h, mode).save("images/CTR_encrypted.bmp")
    bytearray_to_image(decrypted_ctr, w, h, mode).save("images/CTR_decrypted.bmp")

    psnr_ctr = psnr(original_image, bytearray_to_image(decrypted_ctr, w, h, mode))

    print("---- CTR MODE ----")
    print("Encrypt time:", enc_time_ctr)
    print("Decrypt time:", dec_time_ctr)
    print("PSNR:", psnr_ctr)
    print("-------------------\n")

    print("TÜM AES MODLARI TAMAMLANDI!")