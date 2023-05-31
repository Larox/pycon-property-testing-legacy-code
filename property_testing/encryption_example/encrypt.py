from cryptography.fernet import Fernet


class EncryptionHandler:
    def __init__(self, key: str):
        self.key = key
        self.cipher = Fernet(key)

    def encrypt_string(self, text: str) -> bytes:
        if not text.isascii():
            raise ValueError("Input must be an ASCII string")
        encoded_text = text.encode("ascii")
        return self.cipher.encrypt(encoded_text)

    def decrypt_string(self, encrypted_text: bytes) -> str:
        decrypted_bytes = self.cipher.decrypt(encrypted_text)
        return decrypted_bytes.decode("ascii")
