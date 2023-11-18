# DOCS here https://docs.alpaca.markets/


import requests
import os
from dotenv import load_dotenv

from alpaca.data.live import StockDataStream
from alpaca.data.requests import StockLatestQuoteRequest
from alpaca.data.requests import NewsRequest

# set api key and secret key from .env file
load_dotenv()
KEY = os.getenv('KEY')
SECRET = os.getenv('SECRET')

stock_stream = StockDataStream(KEY, SECRET)

#NewsRequest('AAPL', KEY, SECRET).get_news()
newsReq = NewsRequest()
newsReq.start

url = "https://data.alpaca.markets/v1beta1/news?sort=desc"
headers = {"accept": "application/json"}


#look into these corporate anouncement takes
#https://docs.alpaca.markets/reference/corporateactions


# Get the top market movers
# Could I just buy into the ones that just started moving?
