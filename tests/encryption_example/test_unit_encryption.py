import pytest

from property_testing.encryption_example.encrypt import decrypt_string, encrypt_string


class TestUnitEncrypt:
    test_text = "nxt.yzn3wnr-tdc2RWA"

    def test_encrypt_return_bytes(self):
        assert type(encrypt_string(self.test_text)) is bytes

    def test_decrypt_return_original_text(self):
        assert decrypt_string(encrypt_string(self.test_text)) == self.test_text
