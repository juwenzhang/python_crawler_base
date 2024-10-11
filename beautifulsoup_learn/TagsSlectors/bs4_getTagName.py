# 实现获取标签本身名称

from bs4 import BeautifulSoup

html_doc = "<html><head><title>My Title</title></head><body><p>Hello, BeautifulSoup4!</p></body></html>"

# 实例化对象
# 基本语法: BeautifulSoup("需要解析的对象", "需要使用的解析器")
soup = BeautifulSoup(html_doc, 'lxml')

# 实现获取 标签 本身的名称
print(soup.p.name, soup.title.name)