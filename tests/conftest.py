from client import XTBClient
from settings import XTB_USER, XTB_PASS

import pytest


@pytest.fixture(scope="session")
def xtb_client():
    client = XTBClient()
    logged_in_msg = client.login(XTB_USER, XTB_PASS)
    assert logged_in_msg.get('status') is True
    yield client
    response = client.logout()
    print('logging out info {}'.format(response))
    assert response.get('status') is True
