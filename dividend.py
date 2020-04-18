import json
import requests

def dividend(ticker):
    resp = requests.get('https://finance.yahoo.com/quote/' + ticker)
    return get_dividend(resp.text)

def parse(input):
    start_str = 'root.App.main = '
    finish_str = '}(this))'
    index_from = input.index(start_str) + len(start_str)
    index_to = input.index(finish_str)-2
    return input[index_from: index_to]

def get_dividend(content):
    js = json.loads(parse(content))
    return js['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['dividendRate']['raw']
