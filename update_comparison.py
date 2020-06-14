from __future__ import print_function
from yahoo_finance_data import yahoo_finance_data
from sheets_client import sheets_client
from sheet_utils import *
from yf_data_utils import *

SPREADSHEET_ID = '1xkagdDVgoacqYoUw_7yQ7rJUTDj8YOAFN8TRavh_sCU'
SHEET_NAME = 'Tech Giants'


def report_batch(shm, page_name, tickers):
    shm.page_name = page_name
    write_row_names(shm)
    write_data(shm, tickers)


def write_row_names(shm):
    rows = list(map(lambda a: [a], ROW_FUNCTIONS))
    write_batch(shm, 'A2', 'A' + str(len(ROW_FUNCTIONS)+1), rows)


def write_data(shm, tickers):
    infos = []
    for ticker in tickers:
        infos.append(yahoo_finance_data(ticker))

    rows = [tickers]
    functions = ROW_FUNCTIONS.values()
    for f in functions:
        rows.append(get_row(infos, f))

    col_start = 1
    row_start = 1
    cell_from = col_to_let(col_start) + str(row_start)
    cell_to = col_to_let(col_start + len(tickers)) + str(row_start + len(functions))

    write_batch(shm, cell_from, cell_to, rows)


def get_row(infos, func):
    row = []
    for info in infos:
        row.append(func(info))
    return row


def main():
    sheet = sheets_client()
    shm = SheetMeta(sheet, SPREADSHEET_ID, SHEET_NAME)

    report_batch(shm, 'Tech Giants', ['MSFT', 'GOOG', 'AMZN'])
    exit()
    report_batch(shm, 'Food', ['PEP'])
    # report_batch(shm, 'Food', ['PEP', 'KO', 'GIS', 'CPB', 'DANOY', 'NSRGY', 'KDP'])
    exit()
    report_batch(shm, 'Household', ['JNJ', 'KMB', 'CLX', 'PG', 'UL', 'CL'])

    report_batch(shm, 'Restaurants', ['MCD', 'SBUX'])

    report_batch(shm, 'Healthcare', ['JNJ', 'PFE', 'ABBV'])

    report_batch(shm, 'Sin stocks', ['MO', 'BTI', 'PM', 'UVV'])

    report_batch(shm, 'Tech', ['IBM', 'APPL', 'MSFT'])

    report_batch(shm, 'My portfolio', ['JNJ', 'PEP', 'MMM', 'IBM', 'ABBV', 'MO'])

if __name__ == '__main__':
    main()
