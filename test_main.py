import datetime

from EarningsCalendar.earnings_calendar import get_companies_with_positive_eps
from BackTesting.backtest_tradercli import buy_stock_at_time, get_all_positions

# TODO: Will probably need to move out a lot of these sections / decouple
if __name__ == "__main__":
    start_time = datetime.datetime(2022, 2, 1, 8, 0) 
    end_time = datetime.datetime(2022, 2, 1, 19, 0)  
    time_difference = datetime.timedelta(hours=1)

    # TODO: Might need to download the Yahoo data for faster testing, this is too slow

    # need to keep track of how long a stock has been held, and autoSell
    # create a sell order right away once it reaches > 5% profit?
    # need to mock limit sell
    while start_time < end_time:          
        comps = get_companies_with_positive_eps(start_time)

        positions = get_all_positions()

        for comp in comps:
            if comp.symbol not in positions:
                buy_stock_at_time(comp.symbol, start_time)
                #get_stock_price_at_time("GOOGL", start_time)

        start_time += time_difference

    print(positions)