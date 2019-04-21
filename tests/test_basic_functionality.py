def test_get_symbols(xtb_client):
    symbols = list(xtb_client.get_all_symbols())
    assert len(symbols) > 0


def test_get_balance(xtb_client):
    balance = xtb_client.get_balance()
    assert balance.get('balance') is not None


def test_ping(xtb_client):
    response = xtb_client.ping()
    assert response
