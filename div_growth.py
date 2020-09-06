import requests
import time
import datetime
from bisect import bisect
from growth import exp_growth


def _adjust_dividend(date, div, split_dates, split_values):
    adjusted = div
    last = bisect(split_dates, date)
    for split in split_values[0:last]:
        adjusted *= int(split[0])
        adjusted /= int(split[1])
    return date, adjusted


def div_growth(ticker, last_years):
    from_ = 0
    to_ = int(time.time_ns()/1000000000)
    div_url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_}&period2={to_}&interval=1d&events=div"
    split_url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_}&period2={to_}&interval=1d&events=split"

    dividends_raw = requests.get(div_url).text.split('\n')[1:]
    splits_raw = requests.get(split_url).text.split('\n')[1:]
    split_dates = [s.split(',')[0] for s in splits_raw]
    split_values = [(s.split(',')[1].split(':')[0], s.split(',')[1].split(':')[1]) for s in splits_raw]

    dividends = [(l.split(',')[0], float(l.split(',')[1].strip())) for l in dividends_raw]
    dividends.sort(key=lambda t: t[0])
    adjusted_dividends = [_adjust_dividend(div[0], div[1], split_dates, split_values) for div in dividends]

    yearly_dividends = {}
    for date, div in adjusted_dividends:
        year = int(date.split('-')[0])
        if year == datetime.date.today().year: # Avoiding not finished year
            continue
        if year not in yearly_dividends:
            yearly_dividends[year] = 0
        yearly_dividends[year] += div

    growth = exp_growth(list(yearly_dividends.values())[-last_years:])
    return growth - 1 if growth != "N/A" else "N/A"
