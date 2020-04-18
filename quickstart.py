from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dividend import dividend
from sheets_client import sheets_client

SPREADSHEET_ID = '1iIbyyHFvqU7AS_x1kp1aOuzKg-WKW4SRpFreFQ8dk8A'

def write_cell_value(sheet, cell, value):
    body = {'values': [[value]]}
    sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=cell, valueInputOption='RAW', body=body).execute()


def main():
    sheet = sheets_client()
    # result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Sheet1!A2:C').execute()
    # values = result.get('values', [])
    #
    # if not values:
    #     print('No data found.')
    # else:
    #     print('Stock, Number, Dividend:')
    #     for row in values:
    #         print('%s, %s, %s' % (row[0], row[1], row[2]))

    ticker = 'MMM'
    div = dividend(ticker)
    write_cell_value(sheet, 'Dividends!D16:D16', div)


if __name__ == '__main__':
    main()
