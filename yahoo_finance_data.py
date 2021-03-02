import json
import requests
from growth import linear_to_exp_growth
from div_growth import div_years_and_growth


LAST_DIVIDEND_GROWTH_YEARS = 10


def yahoo_finance_data(ticker):
    resp = requests.get('https://finance.yahoo.com/quote/' + ticker)
    _json = _get_json(resp.text)
    if _json is None:
        print("Could not get json for " + ticker)
        return {}
    js = json.loads(_json)

    bs_resp = requests.get('https://finance.yahoo.com/quote/' + ticker + '/balance-sheet?p=' + ticker)
    _bs_json = _get_json(bs_resp.text)
    if _bs_json is None:
        print("Could not get balance sheet json for " + ticker)
        return {}
    bs_js = json.loads(_bs_json)
    div_years, div_growth = ('N/A', 'N/A') if _dividend_return(js) == 'N/A' else div_years_and_growth(ticker, LAST_DIVIDEND_GROWTH_YEARS)
    return {
        "eps": _eps(js),
        "price": _price(js),
        "dividend_value": _dividend_value(js),
        "dividend_return": _dividend_return(js),
        "dividend_growth": div_growth,
        "dividend_years": div_years,
        "market_cap": _market_cap(js),
        "profit_margin": _profit_margin(js),
        "payout_ratio": _payout_ratio(js),
        "debt": _debt(js),
        "net_income": _net_income(js),
        "sales_growth": _sales_growth(js),
        "net_income_growth": _net_income_growth(js),
        "equity": _equity(bs_js),
        "equity_growth": _equity_growth(bs_js),
        "gross_margin": _gross_margin(js),
    }


def _get_json(inp):
    start_str = 'root.App.main = '
    finish_str = '}(this))'
    if not start_str in inp:
        return
    index_from = inp.index(start_str) + len(start_str)
    index_to = inp.index(finish_str) - 2
    return inp[index_from: index_to]


def _price(js):
    regular_price = js['context']['dispatcher']['stores']['QuoteSummaryStore']['price']['regularMarketPrice']
    return regular_price['raw'] if 'raw' in regular_price else 'N/A'


def _eps(js): #TODO improve with Consensus Estimate?
    return _trailingEps(js) if _forwardEps(js) == 'N/A' else _forwardEps(js)


def _forwardEps(js):
    default_key_statistics = js['context']['dispatcher']['stores']['QuoteSummaryStore']['defaultKeyStatistics']
    if 'forwardEps' not in default_key_statistics:
        return 'N/A'
    eps = default_key_statistics['forwardEps']
    return eps['raw'] if 'raw' in eps else 'N/A'


def _trailingEps(js):
    default_key_statistics = js['context']['dispatcher']['stores']['QuoteSummaryStore']['defaultKeyStatistics']
    if 'trailingEps' not in default_key_statistics:
        return 'N/A'
    eps = default_key_statistics['trailingEps']
    return eps['raw'] if 'raw' in eps else 'N/A'


def _dividend_value(js):
    summary = js['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']
    if 'dividendRate' not in summary:
        return 'N/A'
    dividend = summary['dividendRate']
    return dividend['raw'] if 'raw' in dividend else 'N/A'


def _dividend_return(js):
    summary = js['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']
    if 'dividendYield' not in summary:
        return 'N/A'
    dividend_return = summary['dividendYield']
    return dividend_return['raw'] if 'raw' in dividend_return else 'N/A'


def _market_cap(js):
    summary = js['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']
    if 'marketCap' not in summary:
        return 'N/A'
    market_cap = summary['marketCap']
    return market_cap['raw'] if 'raw' in market_cap else 'N/A'


def _profit_margin(js):
    default_key_stats = js['context']['dispatcher']['stores']['QuoteSummaryStore']['defaultKeyStatistics']
    if 'profitMargins' not in default_key_stats:
        return 'N/A'
    profit_margins = default_key_stats['profitMargins']
    return profit_margins['raw'] if 'raw' in profit_margins else 'N/A'


def _gross_margin(js):
    financial_data = js['context']['dispatcher']['stores']['QuoteSummaryStore']['financialData']
    if 'grossMargins' not in financial_data:
        return 'N/A'
    gross_margins = financial_data['grossMargins']
    return gross_margins['raw'] if 'raw' in gross_margins else 'N/A'


def _payout_ratio(js):
    summary = js['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']
    if 'payoutRatio' not in summary:
        return 'N/A'
    payout_ratio = summary['payoutRatio']
    payout = payout_ratio['raw'] if 'raw' in payout_ratio else 'N/A'
    return 'N/A' if payout == 0 else payout


def _debt(js):
    debt = js['context']['dispatcher']['stores']['QuoteSummaryStore']['financialData']['totalDebt']
    return debt['raw'] if 'raw' in debt else 'N/A'


def _sales_growth(js):
    revenues = []
    if 'financialsChart' not in js['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']:
        return "N/A"
    for e in js['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly']:
        revenues.append(e['revenue']['raw'])
    return linear_to_exp_growth(revenues)


def _net_income_growth(js):
    earnings = []
    if 'financialsChart' not in js['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']:
        return "N/A"
    for e in js['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly']:
        earnings.append(e['earnings']['raw'])
    return linear_to_exp_growth(earnings)


def _equity_growth(bs_js):
    equity = []
    for e in reversed(bs_js['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements']):
        if 'totalStockholderEquity' not in e:
            return "N/A"
        equity.append(e['totalStockholderEquity']['raw'])
    return linear_to_exp_growth(equity)


def _net_income(js):
    if 'financialsChart' not in js['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']:
        return "N/A"
    arr = js['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly']
    earnings = arr[len(arr)-1]['earnings']
    return earnings['raw'] if 'raw' in earnings else earnings


def _equity(bs_js):
    return bs_js['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements'][0][
        'totalStockholderEquity']['raw']