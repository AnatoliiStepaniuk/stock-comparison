class SheetMeta:
    def __init__(self, client, document_id, page_name):
        self.sheet_client = client
        self.document_id = document_id
        self.page_name = page_name


def write_cell(shm, column, row, value):
    cell = column + str(row)
    write_batch(shm, cell, cell, [[value]])


def write_batch(shm, cell_from, cell_to, values):
    cell_range = shm.page_name + "!" + cell_from + ":" + cell_to
    body = {'values': values}
    shm.sheet_client.values().update(spreadsheetId=shm.document_id, range=cell_range, valueInputOption='RAW', body=body).execute()


def col_to_let(index):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet[index]


def create_spread_sheet(client, spreadsheet_title, sheet_title):
    body = {
        'properties': {'title': spreadsheet_title},
        'sheets': [
            {
                'properties': {'title': sheet_title}
            }
        ]
    }

    return client.create(body=body).execute()


def make_first_row_bold(client, spreadsheet_id, sheet_id):
    body = {
        "requests": [
            {
                "repeatCell": {
                    "cell": {
                        "userEnteredFormat": {
                            "textFormat": {
                                "bold": True
                            }
                        }
                    },
                    "range": {
                        "endRowIndex": 1,
                        "sheetId": sheet_id
                    },
                    "fields": "userEnteredFormat.textFormat.bold"
                }
            }
        ]
    }

    client.batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
