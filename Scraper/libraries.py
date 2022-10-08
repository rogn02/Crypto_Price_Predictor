from bs4 import BeautifulSoup
from requests import get
import time
import pandas as pd

def datareset():
    with open('main/data.csv','w') as f:
        f.write("Coin_name,Current_price,Market_Cap(USD_Billion),24H_Volume(USD_Billion),Circulating_supply(USD_Billion),24Hr High,24Hr Low\n")
        f.flush()
        pass
def value_extractor(s):
    for i in range(len(s)):
        if s[i]=='>':
            if s[i+1]=="$":
                s=s[i+2:]
            else:
                s=s[i+1:]
            break
    for i in range(len(s)):
        if s[i]==",":
            s=s[:i]+s[i+1:]
        if s[i]==" ":
            s=s[:i]
            break
        if s[i]=="<":
            s=s[:i]
            break
    """s=list(s).remove(",")
    s="".join(s)"""
    return s
def Writer(List):
    with open('main/data.csv','a') as f:
        f.write(List[0]+ ",")
        List=List[1:]
        for i in range(len(List)-2):
            f.write(value_extractor(List[i])+",")
        List=List[len(List)-2:]
        for i in range(1):
            f.write(List[i].replace(",","")+",")
        f.write((List[len(List)-1]).replace(",",""))
        f.write("\n")
        f.flush()