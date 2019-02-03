from iexfinance.stocks import Stock
import sqlite3
import os
# import time
import time
from sentiment_puller import clear_dbs


def pull_stocks() :
    #i want it to wait until the stock market is open
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
        # rewrite for individual stock columns
        for name in names_list :
            string = "CREATE TABLE "+ name +" (date text, price real)"
            c.execute(string)
        count = 0
        while count < 5 :
            print(f"starting cycle {count}")
            for i in range(len(stock_list)) :
                s = Stock(stock_list[i])
                price = s.get_price()
                date = str(time.ctime())
                # this should work lmao
                string = 'INSERT INTO ' + names_list[i] + ' VALUES (?,?)'
                c.execute(string,(date,price))
            conn.commit()
            time.sleep(60)
            count+=1



if __name__ == '__main__':
    pull_stocks()
