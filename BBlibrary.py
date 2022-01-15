import bybit
import time
from values import *
import json

ts = time.time()

# bybit api BEPQCZ4cGRZa5V4Prp

# bybit secret KGQ2DPqCzr2ED7zh207Hu6EushF5vq13JDRq

# testnet api 2QjbrL8t0cEvAM7ZRl

#testnet secret AMw07GrMqvuhNSSrW2huwy2maZzFf8C9X3Na

def requestdata(symbol):
    client = bybit.bybit(test=True, api_key=apikey[0], api_secret=secretkey[0])

    livedict = {}

    while True:
        ts = time.time()

        data = client.Kline.Kline_get(symbol=symbol, interval=timeinterval[0], **{'from': int(ts)}).result()

        if data[0]['result']:
            print(f"this is the price: {float(data[0]['result'][0]['close'])}")
            livedict[symbol] = float(data[0]['result'][0]['close'])
            return livedict

        else:
            continue

def buy(symbol):
    client = bybit.bybit(test=True, api_key=apikey[0], api_secret=secretkey[0])

    client.Order.Order_new(side="Buy",symbol=symbol,order_type="Market",qty=int(quantityticker[0]),price=getquickprice(symbol),time_in_force="FillOrKill").result()

def sell(symbol, size):
    client = bybit.bybit(test=True, api_key=apikey[0], api_secret=secretkey[0])

    if checkprofit() == True:
        client.Order.Order_new(side="Sell",symbol=symbol,order_type="Market",qty=size,price=getquickprice(symbol),time_in_force="FillOrKill").result()

def checkportfolio(symbol):
    client = bybit.bybit(test=True, api_key=apikey[0], api_secret=secretkey[0])

    try:
        data = client.Positions.Positions_myPosition(symbol=symbol).result()

        print(data)

        if data[0]['result']:
            print("result is present")
            if data[0]['result']['side'] == "Buy":
                print(int(data[0]['result']['size']), int(data[0]['result']['entry_price']))
                return int(data[0]['result']['size']), int(data[0]['result']['entry_price'])
        else:
            print("Symbol not in portfolio")
            return None
    except:
        print("cannot get position")
        return None

def checkprofit(symbol):
    try:
        if checkportfolio(symbol) == None:
            print("P%L values not reached. proceeding....")
        else:
            print(checkportfolio(symbol)[0], checkportfolio(symbol)[1])

            # check p%l
            liveprice = int(getquickprice(symbol))
            qoutedata = checkportfolio(symbol)[1]
            increase = (liveprice - qoutedata) / qoutedata * 100
            if any((int(pnlvalue) == int(increase) for pnlvalue in pnllist)):
                return True
    except:
        print("cannot calculate P%L. proceeding..")

def getquickprice(mysymbol):
    client = bybit.bybit(test=True, api_key=apikey[0], api_secret=secretkey[0])
    try:
        data = client.Market.Market_orderbook(symbol=mysymbol).result()

        return data[0]["result"][0]["price"]
    except:
        print("Cannot get live prices")






