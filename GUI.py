from tkinter import *
from tkinter.ttk import *
import sys
from wrapper import *
from values import *
import threading

screen = Tk()
screen.title("Bybit tading bot")
canvas = Canvas(screen, width= 600, height = 500)
canvas.pack()

rsivaluesellinput = Entry(screen)
canvas.create_window(100, 190, window = rsivaluesellinput)

rsiselllabel = Label(screen, text="RSI values / SELL")
rsiselllabel.place(x=50,y=160)

rsivaluebuyinput = Entry(screen)
canvas.create_window(300, 190, window = rsivaluebuyinput)

rsibuylabel = Label(screen, text="RSI values / BUY")
rsibuylabel.place(x=250,y=160)

symbolinput = Entry(screen)
canvas.create_window(300, 50, window = symbolinput)

symbollabel = Label(screen, text="Enter Symbol")
symbollabel.place(x=260,y=20)

periodinput = Entry(screen)
canvas.create_window(100, 50, window = periodinput)

periodlabel = Label(screen, text="Enter RSI period")
periodlabel.place(x=60,y=20)

apikeyinput = Entry(screen)
canvas.create_window(100, 300, window = apikeyinput)

apikeylabel = Label(screen, text="Enter API key")
apikeylabel.place(x=60,y=270)

secretkeyinput = Entry(screen)
canvas.create_window(300, 300, window = secretkeyinput)

secretkeylabel = Label(screen, text="Enter Secret key")
secretkeylabel.place(x=260,y=270)

quantityinput = Entry(screen)
canvas.create_window(100, 400, window = quantityinput)

quantitylabel = Label(screen, text="Enter Quantity")
quantitylabel.place(x=60,y=370)

intervalinput = Entry(screen)
canvas.create_window(300, 400, window = intervalinput)

intervallabel = Label(screen, text="Enter Time interval")
intervallabel.place(x=260,y=370)

pnlinput = Entry(screen)
canvas.create_window(450, 400, window = pnlinput)

pnllabel = Label(screen, text="Enter profit values")
pnllabel.place(x=410,y=370)

def entervaluebuy():
    rsivaluebuylist.append(int(rsivaluebuyinput.get()))
    print(f"Current rsi values: {rsivaluebuylist}")

def entervaluesell():
    rsivalueselllist.append(int(rsivaluesellinput.get()))
    print(f"Current rsi values: {rsivalueselllist}")

def entersymbol():
    symbollist.append(str(symbolinput.get()))
    print(f"Current Symbol's: {symbollist}")

def enterperiod():
    if rsiperiod:
        rsiperiod[0] = int(periodinput.get())
        print(f"Current SECRET key: {rsiperiod[0]}")
    else:
        rsiperiod.append(int(periodinput.get()))
        print(f"Current rsi period: {rsiperiod[0]}")


def enterapikey():
    if apikey:
        apikey[0] = str(apikeyinput.get())
        print(f"Current SECRET key: {apikey[0]}")
    else:
        apikey.append(str(apikeyinput.get()))
        print(f"Current API key: {apikey[0]}")

def entersecretkey():
    if secretkey:
        secretkey[0] = str(secretkeyinput.get())
        print(f"Current SECRET key: {secretkey[0]}")
    else:
        secretkey.append(str(secretkeyinput.get()))
        print(f"Current SECRET key: {secretkey[0]}")

def enterinterval():
    if timeinterval:
        timeinterval[0] = str(intervalinput.get())
        print(f"Current interval: {timeinterval[0]}")
    else:
        timeinterval.append(str(intervalinput.get()))
        print(f"Current interval: {timeinterval[0]}")

def enterpnl():
    pnllist.append(str(pnlinput.get()))
    print(f"Current pnl values: {pnllist}")

def startfunc():
    print("starting program")
    t = threading.Thread(target=startprogram, daemon=True)
    t.start()

def stopfunc():
    print("exiting program")
    sys.exit()

def enterquantity():
    if quantityticker:
        quantityticker[0] = int(quantityinput.get())
        print(f"Current quantity: {quantityticker[0]}")
    else:
        quantityticker.append(int(quantityinput.get()))
        print(f"Current quantity: {quantityticker[0]}")

enterbuy = Button(screen, text="Submit", command = entervaluebuy)
canvas.create_window(300,220, window=enterbuy)

entersell = Button(screen, text="Submit", command = entervaluesell)
canvas.create_window(100,220, window=entersell)

entersymbol = Button(screen, text="Submit", command = entersymbol)
canvas.create_window(300,80, window=entersymbol)

enterperiod = Button(screen, text="Submit", command = enterperiod)
canvas.create_window(100,80, window=enterperiod)

enterapikeybutton = Button(screen, text="Submit", command = enterapikey)
canvas.create_window(100,330, window=enterapikeybutton)

entersecret = Button(screen, text="Submit", command = entersecretkey)
canvas.create_window(300,330, window=entersecret)

start = Button(screen, text="START", command = startfunc)
canvas.create_window(100,480, window=start)

stop = Button(screen, text="STOP", command = stopfunc)
canvas.create_window(300,480, window=stop)

quantity = Button(screen, text="Submit", command = enterquantity)
canvas.create_window(100,430, window=quantity)

intervalbut = Button(screen, text="Submit", command = enterinterval)
canvas.create_window(300,430, window=intervalbut)

pnlbut = Button(screen, text="Submit", command = enterpnl)
canvas.create_window(450,430, window=pnlbut)

mainloop()