from __future__ import print_function
from yahoo_finance_data import yahoo_finance_data
from sheets_client import sheets_client

SPREADSHEET_ID = '1iIbyyHFvqU7AS_x1kp1aOuzKg-WKW4SRpFreFQ8dk8A'
SHEET_NAME = 'Dividends'


def write_cell_value(sheet, column, row, value):
    cell = column + str(row)
    cell_full = SHEET_NAME + "!" + cell + ":" + cell
    body = {'values': [[value]]}
    sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=cell_full, valueInputOption='RAW', body=body).execute()


def main():
    sheet = sheets_client()
    rows = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SHEET_NAME + '!A2:A7').execute().get('values', [])

    for i, row in enumerate(rows):
        yf_data = yahoo_finance_data(row[0])
        write_cell_value(sheet, 'C', 2+i, yf_data['dividend'])


if __name__ == '__main__':
    main()
