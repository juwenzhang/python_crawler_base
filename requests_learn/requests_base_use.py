# 简单的示例

import requests

# 首先先确定我们的发送请求的网址
url = "https://www.baidu.com"

# 开始发送网络请求
response = requests.get(url)

print(response.text)  # 获取响应内容
print(response.status_code)  # 获取响应状态码
