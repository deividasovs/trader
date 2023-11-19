## TODO: Could turn this into a python library? Other one is out of date



### TODO: Add a threshold where if that EPS is greater than the estimate, then buy
### TODO: Set up buying in Alpaca based on that threshold. Createa  trader module
        
from argparse import ArgumentParser
from datetime import datetime, timedelta

from earnings_calc_scraper import scrape_earnings_on
from earnings_calendar_consts import MINIMUM_EPS_SURPRISE, MINIMUM_EPS


def parse_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "-d",
        "--date",
        type=str,
        default=(datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
        help="Date to download earnings for. Default is 30 days from now.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    args.date = '2023-11-16'
    earnings_date: datetime = args.date

    print(f"Downloading earnings on {earnings_date}")

    comps = scrape_earnings_on(earnings_date, 0)

    comps = [comp for comp in comps if comp.surprise != "-"]

    for comp in comps:
        if float(comp.surprise) > MINIMUM_EPS_SURPRISE and float(comp.eps_estimate) > MINIMUM_EPS:
            print(comp)