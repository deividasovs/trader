# get earnings from yahoo finance on a certain day
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://finance.yahoo.com/calendar/earnings"
RATE_LIMIT = 2000.0
SLEEP_BETWEEN_REQUESTS_IN_SECONDS = 60 * 60 / RATE_LIMIT
OFFSET_STEP = 100


class companyRevenueEps:
    def __init__(self, symbol, eps_estimate, reported_eps, surprise):
        self.symbol = symbol
        self.eps_estimate = eps_estimate
        self.reported_eps = reported_eps
        self.surprise = surprise

    def __str__(self):
        return f"{self.symbol} {self.eps_estimate} {self.reported_eps} {self.surprise}"
        

def scrape_earnings_on(date_str, offset=0):
    dated_url = "{0}?day={1}&offset={2}&size={3}".format(
        BASE_URL, date_str, offset, OFFSET_STEP
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    time.sleep(SLEEP_BETWEEN_REQUESTS_IN_SECONDS)
    print(f"Downloading {dated_url} with offset {offset}")
    page = requests.get(dated_url, headers=headers)
    page_content = page.content.decode(encoding="utf-8", errors="strict")
    soup = BeautifulSoup(page_content, "lxml")

    # Any way to verify that these would be on the same line?

    symbols = [
        td.get_text(strip=True) for td in soup.find_all("td", {"aria-label": "Symbol"})
    ]
    eps_estimates=[
        td.get_text(strip=True) for td in soup.find_all("td", {"aria-label": "EPS Estimate"})
    ]

    reported_eps=[
        td.get_text(strip=True) for td in soup.find_all("td", {"aria-label": "Reported EPS"})
    ]

    surprises = [
        td.get_text(strip=True) for td in soup.find_all("td", {"aria-label": "Surprise(%)"})
    ]
        
    company_revenues = []  

    for i in range(len(symbols)):
        comp = companyRevenueEps(symbols[i], eps_estimates[i], reported_eps[i], surprises[i])
        company_revenues.append(comp)  

    return company_revenues
