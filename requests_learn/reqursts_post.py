# 携带参数的 post 请求

import requests

url = 'https://httpbin.org/post'

data = {
    "username": "<username>",
    "password": "<PASSWORD>",
}

params = {
    "name": "<name>"
}

response = requests.post(url, params=params, data=data)

print(response.text)