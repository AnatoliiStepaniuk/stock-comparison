from __future__ import print_function
from yahoo_finance_data import yahoo_finance_data
from sheet_utils import *
from yf_data_utils import *

page_counter = 0


def write(u, page, tickers):
    global page_counter
    page_counter += 1
    add_sheet(u, page_counter, page)
    shm = SheetMeta(u[0], u[1], page)
    write_row_names(shm)
    write_data(shm, tickers)
    format_percent(u, page_counter, 1, 6, 1, len(tickers)+1)
    format_percent(u, page_counter, 8, 10, 1, len(tickers)+1)
    format_percent(u, page_counter, 13, 15, 1, len(tickers)+1)
    format_white_text_color(u, page_counter, 0, 1, 0, len(tickers)+1)


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

