import re
import string
import unittest

import pytest
from hypothesis import given
from hypothesis import strategies as st

from property_testing.encryption_example.encrypt import decrypt_string, encrypt_string

# [\u0000-\u007F] for ASCII characters, so this test beyond this chars
non_ascii_regex = re.compile(r"[\u0080-\u07FF]|[\u0800-\uFFFF]+")
non_ascii_text = st.from_regex(non_ascii_regex)


class TestEncryption(unittest.TestCase):
    @given(non_ascii_text)
    def test_encrypt_decrypt_functions_raise_error_when_not_ascii_string(self, text):
        with pytest.raises(ValueError) as except_info:
            encrypt_string(text)
        assert str(except_info.value) == "Input must be an ASCII string"

    @given(st.text(alphabet=string.ascii_letters))
    def test_roundtrip_encrypt_decrypt_functions_with_ascii_letters(self, text):
        assert decrypt_string(encrypt_string(text)) == text
