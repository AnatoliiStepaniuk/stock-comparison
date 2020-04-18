class SheetMeta:
    def __init__(self, sheet_client, document_id, page_name):
        self.sheet_client = sheet_client
        self.document_id = document_id
        self.page_name = page_name


def write_cell_value(sheet_meta, column, row, value):
    cell = column + str(row)
    cell_full = sheet_meta.page_name + "!" + cell + ":" + cell
    body = {'values': [[value]]}
    sheet_meta.sheet_client.values().update(spreadsheetId=sheet_meta.document_id, range=cell_full, valueInputOption='RAW', body=body).execute()
