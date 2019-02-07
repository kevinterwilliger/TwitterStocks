from tweetfeels import TweetFeels
from tweetfeels import (TweetFeels, Tweet, TweetData, Sentiment)
from threading import Thread
import time
import nltk
import json
import sys
import os
import stock
import sqlite3



class DevNull :
    def write(self,msg) :
        pass

with open("SECRET.json","r") as j : keys = json.load(j)
consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]
login = [consumer_key, consumer_secret, access_token, access_token_secret]

names_list = ['Apple', 'Coca_Cola', 'Walt_Disney', 'Microsoft', 'Nike',
              'Verizon', 'Amazon', 'Tesla']

def establish_dbs(names_list) :
    try :
        os.remove("tweets.db")
    except :
        pass
    conn = sqlite3.connect("tweets.db")
    c = conn.cursor()
    for name in names_list :
        string = "CREATE TABLE " + name + " (date text, sentiment real)"
        c.execute(string)


# rewrite to make my own tables, and have them just include date and sentiment score
def get_feels(seconds, names, login) :
    apple_feels = TweetFeels(login, tracking=['$AAPL', 'Apple'])
    cocacola_feels = TweetFeels(login, tracking=['$KO', 'Coca Cola', 'Coca-Cola', 'Coke', 'Diet Coke', 'Fanta'])
    waltDisney_feels = TweetFeels(login, tracking=['$DIS', 'Disney', 'Disney World'])
    microsoft_feels = TweetFeels(login, tracking=['$MSFT', 'Microsoft'])
    nike_feels = TweetFeels(login, tracking=['$NKE', 'Nike'])
    verizon_feels = TweetFeels(login, tracking=['VZ', '$VZ', 'Verizon'])
    amazon_feels = TweetFeels(login, tracking=['AMZN','$AMZN','Alexa','AWS'])
    tesla_feels = TweetFeels(login, tracking=['TSLA','$TSLA','Elon','Musk'])
    sentiment_list = [apple_feels, cocacola_feels, waltDisney_feels, microsoft_feels,
                  nike_feels, verizon_feels, amazon_feels, tesla_feels]
    establish_dbs(names)
    count = 0
    while True :
        while stock.is_trading() :
            print("starting cycle " + str(count) + " at " + str(time.ctime()))
            conn = sqlite3.connect("tweets.db")
            c = conn.cursor()
            for name,feel in zip(names,sentiment_list) :
                feel.start(seconds)
                time.sleep(seconds)
                score = feel.sentiment.value
                date = str(time.ctime())
                string = 'INSERT INTO ' + name + ' VALUES (?,?)'
                print("recording " + name + "\'s sentiment at " + date)
                c.execute(string,(date,score))
                conn.commit()
            time.sleep(120)
            count+=1
        stock.wait()
    print(f'end: {time.ctime()}')
