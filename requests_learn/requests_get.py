# 携带参数的 get 请求

import requests

url = 'https://httpbin.org/get'

# 开始设计请求的时候携带的参数设置,然后使用我们的params实现接收我们的参数设置
data = {
    "username": "<username>",
    "password": "<password>",
}

response = requests.get(url, params=data)

# 直接实现获取响应内容
print(response.text)