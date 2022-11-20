import urllib3
import json

url = "http://api.exchangerate.host/latest/"
http = urllib3.PoolManager()
response = http.request('GET', url)
data = response.data
curency = json.loads(data)
curency_data = curency['rates']
user = input('Enter a curency: ')
for i, j in curency_data.items():
    if i == user:
        print('Curency Value = ', j)
