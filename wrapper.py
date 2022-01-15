from historicallibrary import *
from calcrsi import *
from BBlibrary import *
from values import *

def startprogram():
    gethictorical()
    calchistoricalcng(closedict)

    while True:
        for key, value in closedict.items():

            # calculating rsi
            livedict = requestdata(key)
            calcrsi(livedict)

            # checking values
            time.sleep(5)
            checkvalues()






