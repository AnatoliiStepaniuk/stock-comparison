from __future__ import print_function
from yahoo_finance_data import yahoo_finance_data
from sheets_client import sheets_client
from sheet_utils import write_cell_value
from sheet_utils import SheetMeta

SPREADSHEET_ID = '1xkagdDVgoacqYoUw_7yQ7rJUTDj8YOAFN8TRavh_sCU'
SHEET_NAME = 'Sin stocks'

STARTING_YIELD_ROW = 3
MARKET_CAP_ROW = 4
SALES_GROWTH_ROW = 5
NET_INCOME_GROWTH_ROW = 6
PROFIT_MARGIN_ROW = 8
PAYOUT_RATIO_ROW = 9

def main():
    sheet = sheets_client()

    shm = SheetMeta(sheet, SPREADSHEET_ID, SHEET_NAME)
    col = 'D'
    yf_data = yahoo_finance_data('MO')
    write_cell_value(shm, col, STARTING_YIELD_ROW, yf_data['dividend_return'])
    write_cell_value(shm, col, MARKET_CAP_ROW, yf_data['market_cap'])
    write_cell_value(shm, col, SALES_GROWTH_ROW, yf_data['sales_growth'])
    write_cell_value(shm, col, NET_INCOME_GROWTH_ROW, yf_data['net_income_growth'])
    write_cell_value(shm, col, PROFIT_MARGIN_ROW, yf_data['profit_margin'])
    write_cell_value(shm, col, PAYOUT_RATIO_ROW, yf_data['payout_ratio'])



if __name__ == '__main__':
    main()
