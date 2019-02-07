import sentiment
import stock
import threading

def runner() :
    stock_thread = threading.Thread(target=stock.pull_stocks)
    sentiment_thread = threading.Thread(target=sentiment.get_feels,args=(120,sentiment.names_list,sentiment.login))
    stock_thread.start()
    sentiment_thread.start()
    sentiment_thread.join()
    stock_thread.join()

if __name__ == '__main__':
    runner()
