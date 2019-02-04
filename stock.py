from iexfinance.stocks import Stock
import sqlite3
import os
import time
import datetime
from sentiment import clear_dbs


def pull_stocks() :
    #i want it to wait until the stock market is open, which i think i just did
    stock_list = ['AAPL', 'KO', 'DIS', 'MSFT', 'NKE',
                  'VZ', 'AMZN', 'TSLA']
    names_list = ['Apple', 'Coca_Cola', 'Walt_Disney', 'Microsoft', 'Nike',
                  'Verizon', 'Amazon', 'Tesla']
    print(f'start: {time.ctime()}')
    print("restarting databases")
    try :
        os.remove("stocks.db")
    except :
        pass
    try :
        conn = sqlite3.connect("stocks.db")
    except Error as e :
        print(e)
        return
    finally :
        c = conn.cursor()
        for name in names_list :
            string = "CREATE TABLE "+ name +" (date text, price real)"
            c.execute(string)
        now = datetime.datetime.now()
        open = now.replace(hour=8,minute=30,second=0,microsecond=0)
        close = now.replace(hour=16,minute=0,second=0,microsecond=0)
        count = 0
        while True :
            while now < close and now > open :
                print(f"starting cycle {count}")
                for i in range(len(stock_list)) :
                    s = Stock(stock_list[i])
                    price = s.get_price()
                    date = str(time.ctime())
                    string = 'INSERT INTO ' + names_list[i] + ' VALUES (?,?)'
                    c.execute(string,(date,price))
                conn.commit()
                time.sleep(60)
                count += 1
                now = datetime.datetime.now()
            if now > close :
                o = datetime.timedelta(hours=open.hour + 24, minutes=open.minute)
                n = datetime.timedelta(hours=now.hour,minutes=now.minute,seconds=now.second,microseconds=now.microsecond)
                difference = o - n
                print("Stock market closed, waiting " + str(difference.total_seconds()) + " seconds")
                time.sleep(difference.total_seconds())
            elif now < open :
                o = datetime.timedelta(hours=open.hour,minutes=open.minute)
                n = datetime.timedelta(hours=now.hour,minutes=now.minute,seconds=now.second,microseconds=now.microsecond)
                difference = o - n
                print("Stock market closed, waiting " + str(difference.total_seconds()) + " seconds")
                time.sleep(difference.total_seconds())



if __name__ == '__main__':
    pull_stocks()
