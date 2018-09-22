import datetime

from client.constants import Period


def test_historical_default_prices(xtb_client):
    start = int(datetime.datetime(2018, 9, 1).timestamp() * 1000)
    end = int(datetime.datetime(2018, 9, 15).timestamp() * 1000)
    symbol = 'SPA35'  # ibex
    period = Period.h4
    ibex_history = xtb_client.get_chart_range_request(symbol, start, end, period)
    assert len(ibex_history) > 0
