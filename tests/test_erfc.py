import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.erfc import encrypt, decrypt

def test_roundtrip():
    plaintext = "Hello123"
    key = "mySecretKey"
    ciphertext, msg_hash = encrypt(plaintext, key)
    recovered = decrypt(ciphertext, key, msg_hash)
    assert recovered == plaintext
    print("✔️  Round‑trip encryption/decryption works!")

if __name__ == "__main__":
    test_roundtrip()