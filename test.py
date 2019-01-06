from tweetfeels import TweetFeels
from tweetfeels import (TweetFeels, Tweet, TweetData, Sentiment)
from threading import Thread
import time
import nltk
import json


with open("SECRET.json","r") as j : keys = json.load(j)
consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]
login = [consumer_key, consumer_secret, access_token, access_token_secret]

apple_feels = TweetFeels(login, tracking=['$AAPL', 'Apple', 'Iphone', 'Mac', 'iOS'])
cocacola_feels = TweetFeels(login, tracking=['$KO', 'Coca Cola', 'Coca-Cola', 'Coke', 'Diet Coke', 'Fanta'], db = 'sqlites\\cocacola.sqlite')
waltDisney_feels = TweetFeels(login, tracking=['$DIS', 'Disney', 'Disney World'], db = 'sqlites\\waltDisney.sqlite')
microsoft_feels = TweetFeels(login, tracking=['$MSFT', 'Microsoft', 'Windows', 'Xbox'], db = 'sqlites\\microsoft.sqlite')
nike_feels = TweetFeels(login, tracking=['$NKE', 'Nike'], db = 'sqlites\\nike.sqlite')
verizon_feels = TweetFeels(login, tracking=['VZ', '$VZ', 'Verizon'], db = 'sqlites\\verizon.sqlite')
amazon_feels = TweetFeels(login, tracking=['AMZN','$AMZN','Alexa','AWS'], db='splites\\amazon.sqlite')

sentiment_list = [apple_feels, cocacola_feels, waltDisney_feels, microsoft_feels,
                  nike_feels, verizon_feels, amazon_feels]

names_list = ['Apple', 'Coca_Cola', 'Walt_Disney', 'Microsoft', 'Nike',
              'Verizon', 'Amazon']

def print_feels(seconds,feels) :
    count = 0
    feels.start()
    while count < 5 :
        with open('Output.txt','a') as f:
            time.sleep(seconds)
            f.write(f'[{time.ctime()}] Sentiment Score: {feels.sentiment.value}')
            count+=1
    print("Done.")
    feels.stop()
# t = Thread(target=print_feels)
# apple_feels.start()
# t.start()
# time.sleep(30)
# apple_feels.stop()
print_feels(seconds=5,feels=apple_feels)
