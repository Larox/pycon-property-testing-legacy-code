import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

key = os.getenv("ENCRYPT_KEY")

f = Fernet(key)


def encrypt_string(text: str) -> bytes:
    bytes_text = bytes(text, "ascii")
    return f.encrypt(bytes_text)


def decrypt_string(encrypted_text: bytes) -> str:
    text = f.decrypt(encrypted_text)
    return str(text, "ascii")


# def encrypt_list_tokens(text: str, times: int = 5) -> list[bytes]:
#     return [encrypt_string(text) for _ in range(times)]
