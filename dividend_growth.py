import yfinance as yf
from scipy.optimize import curve_fit

from growth import exp_growth
from sheets_client import sheets_client


def dividend_growth(year_from, year_to):
    dividends, years = yearly_real_dividend(year_from, year_to)
    return exp_growth(dividends)


def yearly_real_dividend(year_from, year_to):
    company = yf.Ticker("MO")
    split_dates = company.splits.axes[0].date
    split_values = company.splits.values

    div_this_year = 0
    this_year = company.dividends.axes[0].date[0].year
    yearly_dividends = []
    years = []
    for i, div_date in enumerate(company.dividends.axes[0].date):
        if div_date.year > this_year:
            if year_from <= this_year <= year_to:
                yearly_dividends.append(div_this_year)
                years.append(this_year)
            this_year = div_date.year
            div_this_year = 0
        mult = _find_multiplier(split_dates, split_values, div_date)
        div_this_year += company.dividends.values[i] * mult
    if year_from <= this_year <= year_to:
        yearly_dividends.append(div_this_year)
        years.append(this_year)

    return yearly_dividends, years


def _find_multiplier(split_dates, split_values, current_date):
    mult = 1
    for i, split_date in enumerate(split_dates):
        if split_date > current_date:
            break
        mult *= split_values[i]
    return mult


def write_real_dividends(sheet_id, page_name):
    dividends, years = yearly_real_dividend(0, 2120)

    page = page_name
    col_from = 'A'
    col_to = 'B'
    row_from = 1
    row_to = row_from + len(dividends)
    cell_range = page + "!" + col_from + str(row_from) + ":" + col_to + str(row_to)

    body = {'values': []}
    for i, div in enumerate(dividends):
        body['values'].append([years[i], div])

    sheets_client().values().update(spreadsheetId=sheet_id, range=cell_range,
                                    valueInputOption='RAW', body=body).execute()


# write_real_dividends('1xkagdDVgoacqYoUw_7yQ7rJUTDj8YOAFN8TRavh_sCU', 'Sheet8')
print(dividend_growth(1962, 2006))
