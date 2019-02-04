import sentiment
import stock
import threading

def runner() :
    sentiment_thread = threading.Thread(target=sentiment.print_feels(30,sentiment.sentiment_list,sentiment.names_list))
    stock_thread = threading.Thread(target=stock.pull_stocks())
    sentiment_thread.start()
    stock_thread.start()
    sentiment_thread.join()
    stock_thread.join()

if __name__ == '__main__':
    runner()
