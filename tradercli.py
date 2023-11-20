# Implement simple trader to let loose and update its strategies

import os
from dotenv import load_dotenv

from trader_consts import MAX_PRICE_PER_TRADE

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

load_dotenv()
KEY = os.getenv('KEY')
SECRET = os.getenv('SECRET')

trading_client = TradingClient(KEY, SECRET, paper=True)


account = trading_client.get_account()

search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

assets = trading_client.get_all_assets(search_params)

def buy_stock_at_market(ticker):
    
    qty_to_buy = 1

    # TODO: get price of ticker and set quantity to that which equals MAX_PRICE_PER_TRADE
    

    market_order_data = MarketOrderRequest(
                    symbol=ticker,
                    qty=0.023,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )
    
    market_order = trading_client.submit_order(
                    order_data=market_order_data
                )


def sell_stock(ticker):



def get_all_positions():
    return trading_client.get_all_positions()