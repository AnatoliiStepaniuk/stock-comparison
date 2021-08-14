def dividend_return(yfd):
    return yfd['dividend_return']


def dividend_growth(yfd):
    return yfd['dividend_growth']


def dividend_years(yfd):
    return yfd['dividend_years']


def market_cap(yfd):
    return round(yfd['market_cap']/10**9, 0)


def sales_growth(yfd):
    return float(yfd['sales_growth'])-1 if yfd['sales_growth'] != 'N/A' else 'N/A'


def net_income_growth(yfd):
    return float(yfd['net_income_growth'])-1 if yfd['net_income_growth'] != 'N/A' else 'N/A'


def net_income(yfd):
    return round(yfd['net_income']/10**9, 2) if yfd['net_income'] != 'N/A' else 'N/A'


def equity_growth(yfd):
    return float(yfd['equity_growth'])-1 if yfd['equity_growth'] != 'N/A' else 'N/A'


def gross_profit_margin(yfd):
    return yfd['gross_profit_margin']


def operating_profit_margin(yfd):
    return yfd['operating_profit_margin']


def net_profit_margin(yfd):
    return yfd['net_profit_margin']


def payout_ratio(yfd):
    return yfd['payout_ratio']


def eps_estimate(yfd):
    return yfd['eps_estimate']


def roe(yfd):
    return yfd['net_income'] / yfd['equity'] if yfd['net_income'] != "N/A" and yfd['equity'] != "N/A" else 'N/A'


def debt_to_equity(yfd):
    return round(yfd['debt'] / yfd['equity'], 1) if yfd['debt'] != "N/A" and yfd['equity'] != "N/A" else 'N/A'


def price_to_earnings(yfd):
    return round(yfd['price'] / yfd['eps'], 1) if yfd['price'] != 'N/A' and yfd['eps'] != 'N/A' else 'N/A'

def price_to_earnings_estimate(yfd):
    return round(yfd['price'] / yfd['eps_estimate'], 1) if yfd['price'] != 'N/A' and yfd['eps_estimate'] != 'N/A' else 'N/A'

def debt_repay_years(yfd):
    return round(yfd['debt'] / yfd['net_income'], 1) if yfd['debt'] != 'N/A' and yfd['net_income'] != 'N/A' else 'N/A'


market_cap_key = 'Market cap, B'
net_income_key = 'Net income, B'
dividend_growth_key = 'Dividend growth'
dividend_years_key = 'Dividend years'
dividend_return_key = 'Dividend yield'
sales_growth_key = 'Sales growth'
net_income_growth_key = 'Net income growth'
equity_growth_key = 'Total Equity growth'
gross_profit_margin_key = 'Gross Profit margin'
operating_profit_margin_key = 'Operating Profit margin'
net_profit_margin_key = 'Net Profit margin'
payout_ratio_key = 'Payout ratio'
roe_key = 'ROE'
debt_to_equity_key = 'Debt/Equity'
price_to_earnings_key = 'Price/Earnings'
price_to_earnings_estimate_key = 'Price/Earnings(Est)'
eps_estimate_key = 'EPS(Est)'
debt_repay_years_key = 'Debt repay, yrs'

ROW_FUNCTIONS = {
    gross_profit_margin_key: [gross_profit_margin, True],
    operating_profit_margin_key: [operating_profit_margin, True],
    net_profit_margin_key: [net_profit_margin, True],
    sales_growth_key: [sales_growth, True],
    net_income_growth_key: [net_income_growth, True],
    # dividend_growth_key: [dividend_growth, True],
    # dividend_years_key: [dividend_years, True],
    debt_repay_years_key: [debt_repay_years, False],
    equity_growth_key: [equity_growth, True],
    roe_key: [roe, True],
    net_income_key: [net_income, False],
    market_cap_key: [market_cap, False],
    debt_to_equity_key: [debt_to_equity, False],
    payout_ratio_key: [payout_ratio, True],
    dividend_return_key: [dividend_return, True],
    price_to_earnings_key: [price_to_earnings, False],
    price_to_earnings_estimate_key: [price_to_earnings_estimate, False],
    eps_estimate_key: [eps_estimate, False]
}
