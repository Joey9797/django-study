from django.shortcuts import render
import requests, pprint


# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    API_URL = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"
    API_KEY = "ttbpjhch10092341001"
    params = {
        'ttbkey' : API_KEY,
        'QueryType' : 'ItemNewSpecial',
        'SearchTarget' : 'Book',
        'Start' : 1,
        'MaxResults' : 50,
        'Output' : 'JS',
        'Version' : '20131101',
    }

    res = requests.get(API_URL, params=params)
    datas = res.json()
    books = []
    for data in datas['item']:
        info = {
            '제목' : data['title'],
            '저자' : data['author'],
            '출간일' : data['pubDate'],
            '국제 표준 도서 번호' : data['isbn']
        }
        books.append(info)
    return render(request, 'recommend.html', {'books' : books})