import pprint
import requests

API_KEY = 'ttbpjhch10092341001'
params = {
    'TTBKey': API_KEY,
    'QueryType': 'ItemNewAll',
    # 'MaxResults' : 10,
    # 'start' : 1,
    'SearchTarget':'Book',
    'output': 'js',
    'Version' : '20131101'
}
response = requests.get('http://www.aladin.co.kr/ttb/api/ItemList.aspx', params=params)
data = response.json()
for item in data['item']:
    book = {
        'isbn': item['isbn'],
        'title': item['title'],
        'pubDate': item['pubDate'],
        'author': item['author']
    }
    pprint.pprint(item)