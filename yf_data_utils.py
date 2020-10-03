def dividend_return(yfd):
    return yfd['dividend_return']


def dividend_growth(yfd):
    return yfd['dividend_growth']


def market_cap(yfd):
    return round(yfd['market_cap']/10**9, 0)


def sales_growth(yfd):
    return float(yfd['sales_growth'])-1 if yfd['sales_growth'] != 'N/A' else 'N/A'


def net_income_growth(yfd):
    return float(yfd['net_income_growth'])-1 if yfd['net_income_growth'] != 'N/A' else 'N/A'


def net_income(yfd):
    return round(yfd['net_income']/10**9, 2)


def equity_growth(yfd):
    return float(yfd['equity_growth'])-1 if yfd['equity_growth'] != 'N/A' else 'N/A'


def profit_margin(yfd):
    return yfd['profit_margin']


def payout_ratio(yfd):
    return yfd['payout_ratio']


def roe(yfd):
    return yfd['net_income'] / yfd['equity']


def debt_to_equity(yfd):
    return round(yfd['debt'] / yfd['equity'], 1) if yfd['debt'] != "N/A" and yfd['equity'] != "N/A" else 'N/A'


def price_to_earnings(yfd):
    return round(yfd['price'] / yfd['eps'], 1) if yfd['price'] != 'N/A' and yfd['eps'] != 'N/A' else 'N/A'


def debt_repay_years(yfd):
    return round(yfd['debt'] / yfd['net_income'], 1) if yfd['debt'] != 'N/A' and yfd['net_income'] != 'N/A' else 'N/A'


market_cap_key = 'Market cap, B'
net_income_key = 'Net income, B'
dividend_growth_key = 'Dividend growth'
dividend_return_key = 'Dividend yield'
sales_growth_key = 'Sales growth'
net_income_growth_key = 'Net income growth'
equity_growth_key = 'Total Equity growth'
profit_margin_key = 'Profit margin'
payout_ratio_key = 'Payout ratio'
roe_key = 'ROE'
debt_to_equity_key = 'Debt/Equity'
price_to_earnings_key = 'Price/Earnings'
debt_repay_years_key = 'Debt repay, yrs'

ROW_FUNCTIONS = {
    profit_margin_key: profit_margin,
    sales_growth_key: sales_growth,
    net_income_growth_key: net_income_growth,
    dividend_growth_key: dividend_growth,
    debt_repay_years_key: debt_repay_years,
    equity_growth_key: equity_growth,
    roe_key: roe,
    net_income_key: net_income,
    market_cap_key: market_cap,
    debt_to_equity_key: debt_to_equity,
    payout_ratio_key: payout_ratio,
    dividend_return_key: dividend_return,
    price_to_earnings_key: price_to_earnings
}
