import json
import requests


def yahoo_finance_data(ticker):
    resp = requests.get('https://finance.yahoo.com/quote/' + ticker)
    js = json.loads(get_json(resp.text))
    return {
        "dividend": get_dividend(js)
    }


def get_json(input):
    start_str = 'root.App.main = '
    finish_str = '}(this))'
    index_from = input.index(start_str) + len(start_str)
    index_to = input.index(finish_str)-2
    return input[index_from: index_to]


def get_dividend(js):
    return js['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['dividendRate']['raw']
