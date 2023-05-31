import nacl.secret
import nacl.utils


class EncryptionHandler:
    def __init__(self, key: bytes):
        self.key = key
        self.box = nacl.secret.SecretBox(key)

    def encrypt_string(self, text: str) -> bytes:
        encoded_text = text.encode("ascii")
        nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
        encrypted_bytes = self.box.encrypt(encoded_text, nonce)
        return encrypted_bytes

    def decrypt_string(self, encrypted_text: bytes) -> str:
        decrypted_bytes = self.box.decrypt(encrypted_text)
        decrypted_text = decrypted_bytes.decode("ascii")
        return decrypted_text
