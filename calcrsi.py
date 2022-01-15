from wrapper import *
from BBlibrary import *
from values import *

reusedict = {}

def calchistoricalcng(closedict):
    for key, value in closedict.items():
        chngup = []
        chngdown = []
        for x in range(len(value[0])):
            current = x + 1
            if current < len(value[0]):
                if float(value[0][current]) > float(value[0][x]):
                    chngup.append(float(value[0][current]) - float(value[0][x]))
                    chngdown.append(0)
                elif float(value[0][current]) < float(value[0][x]):
                    chngdown.append(float(value[0][current]) - float(value[0][x]))
                    chngup.append(0)

        avggain = sum(chngup) / rsiperiod[0]
        avgloss = sum(chngdown) / rsiperiod[0]

        lastprice = closedict[key][0][-1]

        reusedict[key] = [avggain, avgloss, lastprice, 0]

def calcrsi(livedict):
    for key, value in livedict.items():
        preavggain = reusedict[key][0]
        preavgloss = reusedict[key][1]
        chngup = None
        chngdown = None

        if value > float(reusedict[key][2]):
            chngup = float(value) - float(reusedict[key][2])
            chngdown = 0
        elif value < float(reusedict[key][2]):
            chngup = 0
            chngdown = float(value) - float(reusedict[key][2])

        if chngup is None:
            chngup = 0
        elif chngdown is None:
            chngdown = 0

        print(f"current fregain: {preavggain}")
        print(f"current chngup {chngup}")

        avgrsiup = ((int(rsiperiod[0] - 1) * preavggain) + chngup) / int(rsiperiod[0])

        avgrsidown = ((int(rsiperiod[0] - 1) * preavgloss) + chngdown) / int(rsiperiod[0])

        reusedict[key][0] = avgrsiup
        reusedict[key][1] = avgrsidown
        reusedict[key][2] = value

        ratio = avgrsiup / abs(avgrsidown)

        rsi = int(100.0 - (100.0 / (1.0 + ratio)))

        print(f"current rsi for {key} is: {rsi}")

        reusedict[key][3] = rsi


def checkvalues():

    for key, value in reusedict.items():
        if checkprofit(key) == True:
            qnt = checkportfolio(key)[0]
            if qnt:
                sell(key, qnt)
                print("P&L reached. Start selling instrument")

        elif any((int(rsiuservalue) == int(value[3]) for rsiuservalue in rsivaluebuylist)):
            print(f"RSI value is {value[3]}")
            print(f"start buying {quantityticker[0]} of {key}")
            buy(key)