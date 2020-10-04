import requests
import time
import datetime
from growth import exp_growth


def _adjust_dividend(div, splits):
    adjusted = div[1]

    for split in splits:
        if div[0] >= split[0]:
            adjusted *= int(split[1][0])
            adjusted /= int(split[1][1])
        else:
            break

    return div[0], adjusted


def div_years_and_growth(ticker, last_years):
    from_ = -2208996124 # 1900 year
    to_ = int(time.time_ns()/1000000000)

    div_url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_}&period2={to_}&interval=1d&events=div"
    dividends_raw = requests.get(div_url).text.split('\n')[1:]
    dividends = [(l.split(',')[0], float(l.split(',')[1].strip())) for l in dividends_raw]
    dividends.sort(key=lambda t: t[0])

    split_url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_}&period2={to_}&interval=1d&events=split"
    splits_raw = requests.get(split_url).text.split('\n')[1:]
    splits = [(l.split(',')[0], (l.split(',')[1].split(':')[0], l.split(',')[1].split(':')[1])) for l in splits_raw]
    splits.sort(key=lambda t: t[0])

    adjusted_dividends = [_adjust_dividend(div, splits) for div in dividends]

    yearly_dividends = {}
    for date, div in adjusted_dividends:
        year = int(date.split('-')[0])
        if year == datetime.date.today().year: # Avoiding not finished year
            continue
        if year not in yearly_dividends:
            yearly_dividends[year] = 0
        yearly_dividends[year] += div

    # growth = exp_growth(list(yearly_dividends.values())[-last_years:])
    growth = exp_growth(list(yearly_dividends.values()))
    growth = growth - 1 if growth != "N/A" else "N/A"
    years = len(yearly_dividends)
    return years, growth
