from PyXTBClient.client import XTBClient
from PyXTBClient.settings import XTB_USER, XTB_PASS


class TestBasicFunctionality:
    client = None

    @classmethod
    def setup_class(cls):
        print('Setting up')
        cls.client = XTBClient()
        logged_in_msg = cls.client.login(XTB_USER, XTB_PASS)
        assert logged_in_msg.get('status') is True

    def test_get_symbols(self):
        symbols = self.client.get_all_symbols()
        assert isinstance(symbols, list)

    def test_get_balance(self):
        balance = self.client.get_balance()
        assert balance.get('balance') is not None

    @classmethod
    def teardown_class(cls):
        print("tearing down")
        response = cls.client.logout()
        assert response
