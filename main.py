from PIL import Image
from cryptosteganography import CryptoSteganography
from utils.hasher import hash_creator_id
from config import CREATOR_ID, SECRET_KEY
import os

input_image_path = "assets/original/test_image.png"
output_image_path = "assets/watermarked/test_image_watermarked.png"

def embed_watermark():
    print("[*] Starting watermark embed process...")

    if not os.path.exists(input_image_path):
        print(f"[-] Error: Input image not found at {input_image_path}")
        return

    print("[+] Input image found.")

    watermark_hash = hash_creator_id(CREATOR_ID)
    print(f"[+] Watermark hash: {watermark_hash}")

    crypto_stego = CryptoSteganography(SECRET_KEY)

    try:
        crypto_stego.hide(input_image_path, output_image_path, watermark_hash)
        print(f"[+] Watermark embedded successfully!")
        print(f"[+] Output saved to: {output_image_path}")
    except Exception as e:
        print(f"[-] Failed to embed watermark: {e}")

if __name__ == "__main__":
    print("[*] Running main.py directly...")
    embed_watermark()
