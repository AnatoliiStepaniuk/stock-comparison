def dividend_return(yfd):
    return yfd['dividend_return']


def market_cap(yfd):
    return round(yfd['market_cap']/10**9, 0)


def sales_growth(yfd):
    return float(yfd['sales_growth'])-1 if yfd['sales_growth'] != 'N/A' else 'N/A'


def net_income_growth(yfd):
    return float(yfd['net_income_growth'])-1 if yfd['net_income_growth'] != 'N/A' else 'N/A'


def net_income(yfd):
    return round(yfd['net_income']/10**9, 0)


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


market_cap_key = 'Market cap'
net_income_key = 'Net income'
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
    market_cap_key: market_cap,
    net_income_key: net_income,
    dividend_return_key: dividend_return,
    sales_growth_key: sales_growth,
    net_income_growth_key: net_income_growth,
    equity_growth_key: equity_growth,
    profit_margin_key: profit_margin,
    payout_ratio_key: payout_ratio,
    roe_key: roe,
    debt_to_equity_key: debt_to_equity,
    price_to_earnings_key: price_to_earnings,
    debt_repay_years_key: debt_repay_years
}
