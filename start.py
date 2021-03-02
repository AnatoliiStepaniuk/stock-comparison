from sheet_utils import create_spread_sheet
from sheets_client import sheets_client
from write import write

client = sheets_client()
spreadsheet_id = create_spread_sheet(client, 'Food/Drinks Test3')
u = (client, spreadsheet_id)

write(u, 'Food', ['PEP', 'KO', 'GIS', 'CPB', 'DANOY', 'NSRGY', 'KDP'])
write(u, 'Household', ['JNJ', 'KMB', 'CLX', 'PG', 'UL', 'CL'])
write(u, 'Restaurants', ['MCD', 'SBUX'])
write(u, 'Healthcare', ['JNJ', 'PFE', 'ABBV'])
write(u, 'Sin stocks', ['MO', 'BTI', 'PM', 'UVV'])
write(u, 'Tech', ['IBM', 'AAPL', 'MSFT'])
write(u, 'My portfolio', ['JNJ', 'PEP', 'MMM', 'IBM', 'ABBV', 'MO'])


