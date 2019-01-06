from tweetfeels import TweetFeels
from tweetfeels import (TweetFeels, Tweet, TweetData, Sentiment)
from threading import Thread
import time
import nltk

consumer_key = "5l2zJ3Sp2COoTmYYRV4sgVald"
consumer_secret = "g66DHjwKaNMu6DqI06woZW7AmWYRmBsR22lEpkLOiSIrgiJhBG"
access_token = "967557596101083137-QEenqFrakqhHHNF9aq19YDqxyDsugw4"
access_token_secret = "dIr7hWPw4orRwkjmNFziFWLEIZ4ifP70VJJrz9QO9eE9g"
login = [consumer_key, consumer_secret, access_token, access_token_secret]

#api calls
MMM_feels = TweetFeels(login, tracking=['$MMM', 'MMM', '3M', '3M Company'], db = 'sqlites\\3M.sqlite')
americanExpress_feels = TweetFeels(login, tracking=['$AXP', 'American Express'], db = 'sqlites\\americanExpress.sqlite')
apple_feels = TweetFeels(login, tracking=['$AAPL', 'Apple', 'Iphone', 'Mac', 'iOS'], db = 'sqlites\\apple.sqlite')
boeing_feels = TweetFeels(login, tracking=['$BA', 'Boeing'], db = 'sqlites\\boeing.sqlite')
caterpillar_feels = TweetFeels(login, tracking=['$CAT', 'Caterpillar'], db = 'sqlites\\caterpillar.sqlite')
chevron_feels = TweetFeels(login, tracking=['$CVX', 'Chevron'], db = 'sqlites\\chevron.sqlite')
cisco_feels = TweetFeels(login, tracking=['$CSCO', 'Cisco'], db = 'sqlites\\cisco.sqlite')
cocacola_feels = TweetFeels(login, tracking=['$KO', 'Coca Cola', 'Coca-Cola', 'Coke', 'Diet Coke', 'Fanta'], db = 'sqlites\\cocacola.sqlite')
waltDisney_feels = TweetFeels(login, tracking=['$DIS', 'Disney', 'Disney World'], db = 'sqlites\\waltDisney.sqlite')
dowdupont_feels = TweetFeels(login, tracking=['$DWDP', 'Dow DuPont'], db = 'sqlites\\dowdupont.sqlite')
exxon_feels = TweetFeels(login, tracking=['$XOM', 'Exxon', 'Exxon Mobil'], db = 'sqlites\\exxon.sqlite')
generalElectric_feels = TweetFeels(login, tracking=['$GE', 'General Electric'], db = 'sqlites\\generalElectric.sqlite')
goldmanSachs_feels = TweetFeels(login, tracking=['$GS', 'Goldman Sachs'], db = 'sqlites\\goldmachSachs.sqlite')
homeDepot_feels = TweetFeels(login, tracking=['$HD', 'Home Depot'], db = 'sqlites\\homeDepot.sqlite')
ibm_feels = TweetFeels(login, tracking=['$IBM', 'IBM'], db = 'sqlites\\ibm.sqlite')
intel_feels = TweetFeels(login, tracking=['$INTC', 'Intel'], db = 'sqlites\\intel.sqlite')
johnsonjohnson_feels = TweetFeels(login, tracking=['$JNJ', 'Johnson & Johnson'], db = 'sqlites\\johnsonjohnson.sqlite')
jpmorgan_feels = TweetFeels(login, tracking=['$JPM', 'JP Morgan', 'JPMorgan', 'Chase'], db = 'sqlites\\jpmorgan.sqlite')
mcdonalds_feels = TweetFeels(login, tracking=['$MCD', 'McDonalds'], db = 'sqlites\\mcdonalds.sqlite')
merck_feels = TweetFeels(login, tracking=['$MRK', 'Merck'], db = 'sqlites\\merck.sqlite')
microsoft_feels = TweetFeels(login, tracking=['$MSFT', 'Microsoft', 'Windows', 'Xbox'], db = 'sqlites\\microsoft.sqlite')
nike_feels = TweetFeels(login, tracking=['$NKE', 'Nike'], db = 'sqlites\\nike.sqlite')
pfizer_feels = TweetFeels(login, tracking=['$PFE', 'Pfizer'], db = 'sqlites\\pfizer.sqlite')
procter_feels = TweetFeels(login, tracking=['$PG', 'Procter and Gamble', 'Procter & Gamble'], db = 'sqlites\\procter.sqlite')
theTravelers_feels = TweetFeels(login, tracking=['TRV', '$TRV', 'Travellers Company'], db = 'sqlites\\theTravelers.sqlite')
unitedTech_feels = TweetFeels(login, tracking=['UTX', '$UTX', 'United Technology'], db = 'sqlites\\unitedTech.sqlite')
unitedHealth_feels = TweetFeels(login, tracking=['UNH', '$UNH', 'United Health'], db = 'sqlites\\unitedHealth.sqlite')
verizon_feels = TweetFeels(login, tracking=['VZ', '$VZ', 'Verizon'], db = 'sqlites\\verizon.sqlite')
visa_feels = TweetFeels(login, tracking=['$V', 'Visa'], db = 'sqlites\\visa.sqlite')
walmart_feels = TweetFeels(login, tracking=['WMT', '$WMT', 'Walmart'], db = 'sqlites\\walmart.sqlite')

sentiment_list = [MMM_feels, americanExpress_feels, apple_feels, boeing_feels, caterpillar_feels, chevron_feels, cisco_feels, cocacola_feels, waltDisney_feels, dowdupont_feels,
exxon_feels, generalElectric_feels, goldmanSachs_feels, homeDepot_feels, ibm_feels, intel_feels, johnsonjohnson_feels, jpmorgan_feels, mcdonalds_feels, merck_feels,
microsoft_feels, nike_feels, pfizer_feels, procter_feels, theTravelers_feels, unitedTech_feels, unitedHealth_feels, verizon_feels, visa_feels, walmart_feels]
#sentiment_list = ['MMM_feels','americanExpress_feels','apple_feels','boeing_feels','caterpillar_feels','chevron_feels','cisco_feels','cocacola_feels','waltDisney_feels','dowdupont_feels','exxon_feels','generalElectric_feels','goldmanSachs_feels']
names_list = ['3M_Company', 'American_Express', 'Apple', 'Boeing', 'Caterpillar', 'Chevron', 'Cisco', 'Coca_Cola', 'Walt_Disney', 'DowDuPont', 'Exxon', 'General_Electric',
'Goldman_Sachs','Home Depot', 'IBM', 'Intel', 'Johnson&Johnson', 'JPMorgan', 'McDonalds', 'Merck', 'Microsoft', 'Nike', 'Pfizer', 'Procter&Gamble', 'Travelers_Companies',
'United_Technologies','United_Health', 'Verizon', 'Visa', 'Walmart']

#calls to tweetfeels every 120 seconds, 30 times in total (i think)
def puller(sentiment_list, names_list):
    #go_on = True
    #count = 30
    def print_feels(seconds, feels_list, name_list):
        count = 1
        #print("There")
        while count > 0:
            #writes sentiment score to txt file, i could probs do this in a csv for excel
            with open('newOutput.txt', 'a') as f:
                for feels, name in zip(sentiment_list, names_list):
                    feels.start()
                    print('Calculating Sentiment Score')
                    time.sleep(seconds)
                    #print(f'[{time.ctime()}] Sentiment Score: {feels.sentiment.value}')
                    f.write(f'[{time.ctime()}] {name} Sentiment Score: {feels.sentiment.value} \n')
                    feels.stop()
                    count = count - 1
                    print("here")
                    break
                f.closed

    t = Thread(target=print_feels, args=(10, sentiment_list, names_list))
    print("here")
    t.start()
    #print_feels(seconds,sentiment_list,names_list)

puller(sentiment_list=sentiment_list,names_list=names_list)
