import unittest
import cryptography
from cryptography.fernet import Fernet
from property_testing.encryption_example.encrypt import encrypt_string, decrypt_string

import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("ENCRYPT_KEY")


class TestUnitEncrypt(unittest.TestCase):
    def setUp(self):
        self.key = os.getenv("ENCRYPT_KEY")
        self.f = Fernet(self.key)
        self.text = "Hello, World!"

    def test_encrypt_string(self):
        encrypted_text = encrypt_string(self.text)
        decrypted_text = self.f.decrypt(encrypted_text)
        self.assertEqual(decrypted_text.decode("ascii"), self.text)

    def test_decrypt_string(self):
        encrypted_text = self.f.encrypt(self.text.encode("ascii"))
        decrypted_text = decrypt_string(encrypted_text)
        self.assertEqual(decrypted_text, self.text)

    def test_encrypt_string_with_special_characters(self):
        text = "Hello, World! @#$%"
        encrypted_text = encrypt_string(text)
        decrypted_text = self.f.decrypt(encrypted_text)
        self.assertEqual(decrypted_text.decode("ascii"), text)

    def test_decrypt_string_with_invalid_encrypted_text(self):
        with self.assertRaises(cryptography.fernet.InvalidToken):
            decrypt_string(b"invalid_encrypted_text")

    def test_encrypt_string_with_non_ascii_text(self):
        text = "你好，世界！"
        with self.assertRaises(ValueError):
            encrypt_string(text)
