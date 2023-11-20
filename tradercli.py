import os
from dotenv import load_dotenv

from trader_consts import MAX_PRICE_PER_TRADE

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

from alpaca.data.requests import StockLatestQuoteRequest
from alpaca.data.historical import StockHistoricalDataClient


load_dotenv()
KEY = os.getenv('KEY')
SECRET = os.getenv('SECRET')

trading_client = TradingClient(KEY, SECRET, paper=True)
client = StockHistoricalDataClient(KEY, SECRET)

account = trading_client.get_account()

search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
assets = trading_client.get_all_assets(search_params)

def get_latest_stock_price(symbol):
    multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=[symbol])

    latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)

    latest_ask_price = latest_multisymbol_quotes[symbol].ask_price
    
    return latest_ask_price


def get_quantity_to_buy_using_max_price(symbol):
    return MAX_PRICE_PER_TRADE / get_latest_stock_price(symbol)


def buy_stock_at_market(symbol):    
    qty_to_buy = get_quantity_to_buy_using_max_price(symbol)

    market_order_data = MarketOrderRequest(
                    symbol=symbol,
                    qty=qty_to_buy,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )
    
    market_order = trading_client.submit_order(
                    order_data=market_order_data
                )

    print("Buy submitted")
    print(market_order)


def sell_all_stock_qty(symbol):
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
