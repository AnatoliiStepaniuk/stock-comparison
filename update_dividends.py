from __future__ import print_function
from yahoo_finance_data import yahoo_finance_data
from sheets_client import sheets_client
from sheet_utils import write_cell_value
from sheet_utils import SheetMeta

SPREADSHEET_ID = '1iIbyyHFvqU7AS_x1kp1aOuzKg-WKW4SRpFreFQ8dk8A'
SHEET_NAME = 'Dividends'


def main():
    sheet = sheets_client()
    rows = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SHEET_NAME + '!A2:A7').execute().get('values', [])

    sheet_meta = SheetMeta(sheet, SPREADSHEET_ID, SHEET_NAME)

    for i, row in enumerate(rows):
        yf_data = yahoo_finance_data(row[0])
        write_cell_value(sheet_meta, 'C', 2+i, yf_data['dividend_value'])


if __name__ == '__main__':
    main()
