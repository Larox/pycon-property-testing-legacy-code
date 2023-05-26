import re
import string

import pytest
from hypothesis import given
from hypothesis import strategies as st

from property_testing.encryption_example.encrypt import decrypt_string, encrypt_string

# [\u0000-\u007F] for ASCII characters, so this test beyond this chars
non_ascii_regex = re.compile(r"[\u0080-\u07FF]|[\u0800-\uFFFF]+")
non_ascii_text = st.from_regex(non_ascii_regex)


ascii_text = st.text(alphabet=st.characters(min_codepoint=0, max_codepoint=127)).filter(
    lambda x: all(ord(c) < 128 for c in x)
)

encrypted_text = ascii_text.map(lambda text: (text, encrypt_string(text)))


class TestEncryption:
    @given(non_ascii_text)
    def test_encrypt_decrypt_functions_raise_error_when_not_ascii_string(self, text):
        with pytest.raises(ValueError) as except_info:
            encrypt_string(text)
        assert str(except_info.value) == "Input must be an ASCII string"

    @given(st.text(alphabet=string.ascii_letters))
    def test_roundtrip_encrypt_decrypt_functions_with_ascii_letters(self, text):
        assert decrypt_string(encrypt_string(text)) == text

    @given(encrypted_text)
    def test_decrypt_returns_original_text(self, encrypted_data):
        original_text, encrypted_text = encrypted_data
        assert original_text == decrypt_string(encrypted_text)
