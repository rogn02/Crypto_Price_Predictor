from Modules import *
from GRU_model import *
from LSTM_model import *
from general import *

choice=0
while True:
    choice=int(input("1.) Train a model \n 2.) To exit\n:"))
    if choice==1:
        print("\n")
        try:
            train_model(input("Coin name[ETH,BNB,BTC,USDT]:"))
        except Exception as e:
            print("Training error:",e)
    elif choice==2:
        break
    else:
        print("Enter valid input!")
    print("\n\n")