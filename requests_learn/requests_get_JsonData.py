# 实现获取 json 数据格式的请求
import json

import requests

url = 'https://httpbin.org/get'

response = requests.get(url)

print(response.text)  # 获取的是字符串数据
print(response.json())  # 获取 json 格式的数据

response = response.json()


# 或者说这个还可以抽离一个函数
# 这个时候，我们就提高了代码的复用
def get_User_Agent(response: json, fieldNameOne: str, fieldNameTwo: str, *args, **kwargs) -> str:
    if response:
        if response[fieldNameOne]:
            if response[fieldNameOne][fieldNameTwo]:
                return response[fieldNameOne][fieldNameTwo]
            return f" { fieldNameTwo } 不存在"
        return f" { fieldNameOne } 不存在"
    return f" { response } 不存在"


print(get_User_Agent(response, "headers", "User-Agent"))
