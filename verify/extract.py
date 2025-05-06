import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cryptosteganography import CryptoSteganography
from config import SECRET_KEY, CREATOR_ID
from utils.hasher import hash_creator_id

# Path to watermarked image
watermarked_image_path = "assets/watermarked/test_image_watermarked.png"

def extract_watermark():
    if not os.path.exists(watermarked_image_path):
        print(f"[-] File not found: {watermarked_image_path}")
        return

    crypto_stego = CryptoSteganography(SECRET_KEY)
    extracted = crypto_stego.retrieve(watermarked_image_path)

    if extracted:
        print(f"[+] Watermark Found:\n{extracted}")

        # Compare against actual expected hash
        expected_hash = hash_creator_id(CREATOR_ID)

        if extracted == expected_hash:
            print("[✅] Watermark is valid and matches your creator ID.")
        else:
            print("[⚠️] Watermark does NOT match your creator ID. Possible tampering.")
    else:
        print("[-] No watermark found or wrong key used.")

if __name__ == "__main__":
    extract_watermark()
