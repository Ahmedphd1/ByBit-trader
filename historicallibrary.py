from datetime import datetime
from binance.client import Client
import datetime
from values import *

# authenticate
binance_api_key = 'oNFZzG6tXvWWBA6ADIwZsKucZGQ0WvuzHZYAf6TWNTpEqAQnV2LHxDhPezekF16G'
binance_api_secret = 'lQQvIC9V3GW2ZK93auQi6BfTifoagZeYLW1HUa1y4aRXsqzU1CXj6lPPxb79YEYO'
binance_client = Client(api_key=binance_api_key, api_secret=binance_api_secret)

closedict = {}

def gethictorical():
    today = datetime.date.today()
    start_delta = datetime.timedelta(days=int(rsiperiod[0] + 1))
    startdate = today - start_delta

    for tickers in symbollist:
        print(tickers)
        hd = binance_client.get_historical_klines(tickers + "T", Client.KLINE_INTERVAL_3MINUTE, str(startdate).strip(), str(today).strip())
        close = []
        for data in hd:
            close.append(data[4])
        closedict[tickers] = [close]



