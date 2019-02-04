from tweetfeels import TweetFeels
from tweetfeels import (TweetFeels, Tweet, TweetData, Sentiment)
from threading import Thread
import time
import nltk
import json
import sys
import os
import stock



class DevNull :
    def write(self,msg) :
        pass

with open("SECRET.json","r") as j : keys = json.load(j)
consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]
login = [consumer_key, consumer_secret, access_token, access_token_secret]


apple_feels = TweetFeels(login, tracking=['$AAPL', 'Apple'], db='sqlites\\Apple.sqlite')
cocacola_feels = TweetFeels(login, tracking=['$KO', 'Coca Cola', 'Coca-Cola', 'Coke', 'Diet Coke', 'Fanta'], db = 'sqlites\\Coca_Cola.sqlite')
waltDisney_feels = TweetFeels(login, tracking=['$DIS', 'Disney', 'Disney World'], db = 'sqlites\\Walt_Disney.sqlite')
microsoft_feels = TweetFeels(login, tracking=['$MSFT', 'Microsoft'], db = 'sqlites\\Microsoft.sqlite')
nike_feels = TweetFeels(login, tracking=['$NKE', 'Nike'], db = 'sqlites\\Nike.sqlite')
verizon_feels = TweetFeels(login, tracking=['VZ', '$VZ', 'Verizon'], db = 'sqlites\\Verizon.sqlite')
amazon_feels = TweetFeels(login, tracking=['AMZN','$AMZN','Alexa','AWS'], db='sqlites\\Amazon.sqlite')
tesla_feels = TweetFeels(login, tracking=['TSLA','$TSLA','Elon','Musk'], db='sqlites\\Tesla.sqlite')

sentiment_list = [apple_feels, cocacola_feels, waltDisney_feels, microsoft_feels,
                  nike_feels, verizon_feels, amazon_feels, tesla_feels]

names_list = ['Apple', 'Coca_Cola', 'Walt_Disney', 'Microsoft', 'Nike',
              'Verizon', 'Amazon', 'Tesla']

def clear_dbs(names_list) :
    for name in names_list :
        db = "sqlites\\"+ name + '.sqlite'
        os.remove(db)


def print_feels(seconds, feels_list, names) :
    clear_dbs(names)
    count = 0
    print(f'start: {time.ctime()}')
    while True :
        while stock.is_trading() :
            print("starting cycle " + str(count))
            for name,feel in zip(names,feels_list) :
                feel.start()
                time.sleep(seconds)
                print("recording " + name + "\'s sentiment")
                time.sleep(seconds)
                feel.stop()
            time.sleep(60)
            count+=1
        stock.wait()
    print(f'end: {time.ctime()}')
