import pytest

from property_testing.encryption_example.encrypt import decrypt_string, encrypt_string


class TestUnitEncrypt:
    test_text = "nxt.yzn3wnr-tdc2RWA"
    output_expected = b"gAAAAABkan4QlXGq5JOqgqd4OlTnijwS7xCu_OLLwHxz_MODb9lISwINd1Zthe2_2voTkogukEPJb_iIuxZpemQSm9ii0l6PKFksVDoa5Tr9Oo_DlsRb1So="

    def test_encrypt_return_bytes(self):
        assert type(encrypt_string(self.test_text)) is bytes

    def test_decrypt_return_original_text(self):
        assert decrypt_string(encrypt_string(self.test_text)) == self.test_text

    # @pytest.mark.parametrize("text,token", [(test_text, output_expected)])
    # def test_encrypt_return_token(self, text, token):
    #     assert encrypt_string(text) == token
