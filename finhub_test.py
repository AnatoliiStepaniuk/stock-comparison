import requests
token = 'btsu7a748v6tmsg6lddg'
ticker = 'ABBV'

def _to_net_income(entry):
    net_income = list(filter(lambda x: x['concept'] == 'NetIncomeLoss', entry['report']['ic']))
    if len(net_income) == 0:
        net_income = list(filter(lambda x: x['concept'] == 'ProfitLoss', entry['report']['ic']))

    return net_income[0]['value'] if len(net_income) != 0 else 'N/A'


def _to_revenue(entry):
    revenue = list(filter(lambda x: x['concept'] == 'Revenues', entry['report']['ic']))
    if len(revenue) == 0:
        revenue = list(filter(lambda x: x['concept'] == 'SalesRevenueNet', entry['report']['ic']))

    return revenue[0]['value'] if len(revenue) != 0 else 'N/A'


print(ticker)
r = requests.get(f'https://finnhub.io/api/v1/stock/financials-reported?symbol={ticker}&token={token}')
net_income = list(map(_to_net_income, r.json()['data']))
print("Net Income")
for ni in reversed(net_income):
    print(ni)
# print(net_income)

# revenue = list(map(_to_revenue, r.json()['data']))
# print("Revenue")
# print(revenue)
