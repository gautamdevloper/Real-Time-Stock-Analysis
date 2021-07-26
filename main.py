import datetime
from nsetools import Nse
import pandas as pd


def func(stock_code):
    nse = Nse()
    q = nse.get_quote(stock_code)
    return q['lastPrice']


stock_code_list=['INFY','ZODIACLOTH','ZUARI','A2ZINFRA']

for step in range(1,101):
    price=[]
    col=[]
    time_stamp=datetime.datetime.now()
    time_stamp=time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    for stock_code in stock_code_list:
        price.append(func(stock_code))
    col=[time_stamp]
    col.extend(price)
    df=pd.DataFrame(col)
    df=df.T
    df.to_csv('real time stock data.csv',mode='a',header=False,index=False)
    print(col)

