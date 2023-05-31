import unittest
import cryptography
from cryptography.fernet import Fernet
from property_testing.encryption_example.encrypt import EncryptionHandler

import os
from dotenv import load_dotenv


class TestUnitEncrypt(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        key = os.getenv("ENCRYPT_KEY")
        self.encryption_client = EncryptionHandler(key)
        self.f = Fernet(key)
        self.text = "Hello, World!"

    def test_encrypt_string(self):
        encrypted_text = self.encryption_client.encrypt_string(self.text)
        decrypted_text = self.f.decrypt(encrypted_text)
        self.assertEqual(decrypted_text.decode("ascii"), self.text)

    def test_decrypt_string(self):
        encrypted_text = self.f.encrypt(self.text.encode("ascii"))
        decrypted_text = self.encryption_client.decrypt_string(encrypted_text)
        self.assertEqual(decrypted_text, self.text)

    def test_encrypt_string_with_special_characters(self):
        text = "Hello, World! @#$%"
        encrypted_text = self.encryption_client.encrypt_string(text)
        decrypted_text = self.f.decrypt(encrypted_text)
        self.assertEqual(decrypted_text.decode("ascii"), text)

    def test_decrypt_string_with_invalid_encrypted_text(self):
        with self.assertRaises(cryptography.fernet.InvalidToken):
            self.encryption_client.decrypt_string(b"invalid_encrypted_text")

    def test_encrypt_string_with_non_ascii_text(self):
        text = "你好，世界！"
        with self.assertRaises(ValueError):
            self.encryption_client.encrypt_string(text)
