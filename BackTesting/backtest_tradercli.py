import os
from dotenv import load_dotenv

from setups.trade_strat_consts import MAX_PRICE_PER_TRADE

from BackTesting.test_trading_client import TestTradingClient

from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

from alpaca.data.requests import StockQuotesRequest
from alpaca.data.historical import StockHistoricalDataClient

load_dotenv()
KEY = os.getenv('KEY')
SECRET = os.getenv('SECRET')

trading_client = TestTradingClient([])
client = StockHistoricalDataClient(KEY, SECRET)

search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

def get_stock_price_at_time(symbol, time):
    multisymbol_request_params = StockQuotesRequest(symbol_or_symbols=[symbol], start=time, limit=1)
    # set limit=2 and get the higher end price of the stock?

    latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)

    latest_ask_price = latest_multisymbol_quotes[symbol].ask_price
    
    return latest_ask_price


# TODO: Don't like re-using time here, move outside / turn into a class
def get_quantity_to_buy_using_max_price(symbol, time):
    return MAX_PRICE_PER_TRADE / get_stock_price_at_time(symbol, time)

def buy_stock_at_market(symbol, time):    
    qty_to_buy = get_quantity_to_buy_using_max_price(symbol, time)
    
    market_order = trading_client.submit_order(
                    order_data=market_order_data
                )

    print("Buy submitted")
    print(market_order)

def sell_all_stock_qty(symbol, time):
    positions = get_all_positions()
    qty_to_sell = next((position.qty for position in positions if position.symbol == symbol), None)
    
    market_order_data = MarketOrderRequest(
                    symbol=symbol,
                    qty=qty_to_sell,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY
                    )
    
    market_order = trading_client.submit_order(
                    order_data=market_order_data
                )

    print("Sale submitted")
    print(market_order)


def get_all_positions():
    return trading_client.get_all_positions()
