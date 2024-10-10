# 实现获取 二进制 encode 数据

import requests

# 图片就是我们的二进制数据
url = ('https://gimg4.baidu.com/poster/src=http%3A%2F%2Ft15.baidu.com%2Fit'
       '%2Fu%3D1195008779%2C96541030%26fm%3D225%26app%3D113%26f%3DJPEG%3Fw%'
       '3D2281%26h%3D1440%26s%3DFD9'
       '3CA1A18308FC802133E950300808C&refer=http%3A%2F%2F'
       'www.baidu.com&app=2004&size=f242,182&n=0&g=0n&q=100?sec=1728673928&'
       't=8d0e84d9d9293c6f41c31e59619397d2')

response = requests.get(url)

encode_data = response.content


# 开始实现存储 二进制 数据
def save_encode_data(encode_data, route_name: str):
    with open(route_name, 'wb') as f:
        f.write(encode_data)


save_encode_data(encode_data, 'route.png')
