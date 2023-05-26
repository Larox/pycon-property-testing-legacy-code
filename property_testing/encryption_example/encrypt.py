import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

key = os.getenv("ENCRYPT_KEY")

f = Fernet(key)


def encrypt_string(text: str) -> bytes:
    if not text.isascii():
        raise ValueError("Input must be an ASCII string")
    bytes_text = text.encode("ascii")
    return f.encrypt(bytes_text)


def decrypt_string(encrypted_text: bytes) -> str:
    text = f.decrypt(encrypted_text)
    return str(text, "ascii")
