import requests

headers = { # <- маскируем наши запрос под запрос браузера
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
}

response = requests.get(url='http://httpbin.org/user-agent', headers=headers)
print(response.text) # <- В ответе на наш запрос мы увидим переданный нами user-agent