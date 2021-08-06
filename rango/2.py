import requests

url = 'https://api.cntv.cn/olympic/getOlyMedals'
params = {
    'serviceId': 'pcocean',
    'itemcode': 'GEN-------------------------------',
}

json = requests.get(url, params=params).json()

print(json)
result = json['data']['medalsList']
print(result)
for r in result:

    data = [
        r['rank'],
        r['countryname'].ljust(10),
        'gold' + r['gold'],
        'sliver' + r['silver'],
        'bronze' + r['bronze'],
        'count' + r['count']
    ]
    print(data)
    if int(r['rank']) == 5:
        break
