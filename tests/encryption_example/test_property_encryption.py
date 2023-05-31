import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import re
import string
import unittest

import pytest
from hypothesis import given
from hypothesis import strategies as st

from property_testing.encryption_example.encrypt import EncryptionHandler

load_dotenv()
key = os.getenv("ENCRYPT_KEY")


# [\u0000-\u007F] for ASCII characters, so this test beyond this chars
non_ascii_regex = re.compile(r"[\u0080-\u07FF]|[\u0800-\uFFFF]+")
non_ascii_text = st.from_regex(non_ascii_regex)


ascii_text = st.text(alphabet=st.characters(min_codepoint=0, max_codepoint=127)).filter(
    lambda x: all(ord(c) < 128 for c in x)
)

encrypted_text = ascii_text.map(
    lambda text: (text, Fernet(key).encrypt(text.encode("ascii")))
)


class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.encription_client = EncryptionHandler(key)

    @given(non_ascii_text)
    def test_encrypt_decrypt_functions_raise_error_when_not_ascii_string(self, text):
        with pytest.raises(ValueError) as except_info:
            self.encription_client.encrypt_string(text)
        assert str(except_info.value) == "Input must be an ASCII string"

    @given(st.text(alphabet=string.ascii_letters))
    def test_roundtrip_encrypt_decrypt_functions_with_ascii_letters(self, text):
        assert (
            self.encription_client.decrypt_string(
                self.encription_client.encrypt_string(text)
            )
            == text
        )

    @given(encrypted_text)
    def test_decrypt_returns_original_text(self, encrypted_data):
        original_text, encrypted_text = encrypted_data
        assert original_text == self.encription_client.decrypt_string(encrypted_text)
