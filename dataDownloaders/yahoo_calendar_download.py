import datetime
import csv


from EarningsCalendar.earnings_calc_scraper import scrape_earnings_on
from EarningsCalendar.earnings_calendar import get_companies_with_positive_eps
from BackTesting.backtest_tradercli import buy_stock_at_time, get_all_positions


### From what source are they getting it from? Yahoo get data from NYSE but is 15 mins delayed. Would need to get it from NYSE directly

# TODO: Will probably need to move out a lot of these sections / decouple

#start_time = datetime.datetime(2021, 1, 1, 0, 0) 
start_time = datetime.datetime(2023, 11, 10, 0, 0) 
end_time = datetime.datetime(2023, 11, 13, 0, 0)  
time_difference = datetime.timedelta(days=1)

comps = []

## TODO: what the hell is going on here?
while start_time < end_time:          
    company_revenues = scrape_earnings_on(start_time)
    print(company_revenues[0].symbol)
    comps.extend(company_revenues)

    start_time += time_difference


with open('earnings.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Symbol','EPS Estimate', 'EPS Actual', 'Surprise %'])

    for comp in comps:
        print(comp)
        writer.writerow([comp.symbol, comp.eps_estimate, comp.reported_eps, comp.surprise])


