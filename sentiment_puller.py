from tweetfeels import TweetFeels
from tweetfeels import (TweetFeels, Tweet, TweetData, Sentiment)
from threading import Thread
import time
import nltk
import json
import sys
import os



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
    # sys.stderr = DevNull()
    count = 0
    # repeat = 0
    print(f'start: {time.ctime()}')
    while count < 2 :
        print("starting cycle " + str(count))
        for name,feel in zip(names,feels_list) :
            feel.start()
            time.sleep(seconds)
            print("recording " + name + "\'s sentiment")
            time.sleep(seconds)
            feel.stop()
        count+=1
    print(f'end: {time.ctime()}')

def test_multi() :
    count = 0
    apple_feels = TweetFeels(login, tracking=['$AAPL', 'Apple', 'Iphone', 'Mac', 'iOS'])#, db='sqlites\\apple.sqlite'
    tesla_feels = TweetFeels(login, tracking=['TSLA','$TSLA','Elon','Musk'])#, db='sqlites\\tesla.sqlite'
    waltDisney_feels = TweetFeels(login, tracking=['$DIS', 'Disney', 'Disney World'])#, db = 'sqlites\\waltDisney.sqlite'
    microsoft_feels = TweetFeels(login, tracking=['$MSFT', 'Microsoft', 'Windows', 'Xbox'])#, db = 'sqlites\\microsoft.sqlite'
    nike_feels = TweetFeels(login, tracking=['$NKE', 'Nike'])#, db = 'sqlites\\nike.sqlite'

    test = [apple_feels, tesla_feels,waltDisney_feels,microsoft_feels,nike_feels]
    names = ['Apple', 'Tesla','Walt_Disney','Microsoft','Nike']
    while count < 1 :
        for feel in test :
            feel.start()
        time.sleep(60)
        for name,feel in zip(names,test) :
            print(name + ': ' + f'[{time.ctime()}] Sentiment Score: {feel.sentiment.value} \n')
        count+=1
        for feel in test :
            feel.stop()

if __name__ == '__main__':
    print_feels(30,sentiment_list,names_list)
