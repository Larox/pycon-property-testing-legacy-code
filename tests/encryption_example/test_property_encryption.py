from hypothesis import given, strategies as st

from property_testing.encryption_example.encrypt import decrypt_string, encrypt_string


class TestEncryption:
    @given(st.text())
    def test_roundtrip_encrypt_decrypt_functions_with_ascii_letters(self, text):
        assert decrypt_string(encrypt_string(text)) == text
