import json
import requests
from growth import linear_to_exp_growth


def yahoo_finance_data(ticker):
    resp = requests.get('https://finance.yahoo.com/quote/' + ticker)
    js = json.loads(_get_json(resp.text))

    bs_resp = requests.get('https://finance.yahoo.com/quote/' + ticker + '/balance-sheet?p=' + ticker)
    bs_js = json.loads(_get_json(bs_resp.text))
    return {
        "eps": _eps(js),
        "price": _price(js),
        "dividend_value": _dividend_value(js),
        "dividend_return": _dividend_return(js),
        "market_cap": _market_cap(js),
        "profit_margin": _profit_margin(js),
        "payout_ratio": _payout_ratio(js),
        "debt": _debt(js),
        "net_income": _net_income(js),
        "sales_growth": _sales_growth(js),
        "net_income_growth": _net_income_growth(js),
        "equity": _equity(bs_js),
        "equity_growth": _equity_growth(bs_js),
    }


def _get_json(inp):
    start_str = 'root.App.main = '
    finish_str = '}(this))'
    index_from = inp.index(start_str) + len(start_str)
    index_to = inp.index(finish_str) - 2
    return inp[index_from: index_to]


def _price(js):
    return js['context']['dispatcher']['stores']['QuoteSummaryStore']['price']['regularMarketPrice']['raw']


def _eps(js): #TODO improve with Consensus Estimate?
    eps = js['context']['dispatcher']['stores']['QuoteSummaryStore']['defaultKeyStatistics']['forwardEps']
    return eps['raw'] if 'raw' in eps else 'N/A'


def _dividend_value(js):
    dividend = js['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['dividendRate']
    return dividend['raw'] if 'raw' in dividend else 'N/A'


def _dividend_return(js):
    dividend_return = js['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['dividendYield']
    return dividend_return['raw'] if 'raw' in dividend_return else 'N/A'


def _market_cap(js):
    return js['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['marketCap']['raw']


def _profit_margin(js):
    return js['context']['dispatcher']['stores']['QuoteSummaryStore']['defaultKeyStatistics']['profitMargins']['raw']


def _payout_ratio(js):
    payout_ratio =  js['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['payoutRatio']
    return payout_ratio['raw'] if 'raw' in payout_ratio else 'N/A'


def _debt(js):
    debt = js['context']['dispatcher']['stores']['QuoteSummaryStore']['financialData']['totalDebt']
    return debt['raw'] if 'raw' in debt else 'N/A'


def _sales_growth(js):
    revenues = []
    for e in js['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly']:
        revenues.append(e['revenue']['raw'])
    return linear_to_exp_growth(revenues)


def _net_income_growth(js):
    earnings = []
    for e in js['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly']:
        earnings.append(e['earnings']['raw'])
    return linear_to_exp_growth(earnings)


def _equity_growth(bs_js):
    equity = []
    for e in reversed(bs_js['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements']):
        equity.append(e['totalStockholderEquity']['raw'])
    return linear_to_exp_growth(equity)


def _net_income(js):
    arr = js['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly']
    earnings = arr[len(arr)-1]['earnings']
    return earnings['raw'] if 'raw' in earnings else earnings


def _equity(bs_js):
    return bs_js['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements'][0][
        'totalStockholderEquity']['raw']