# 通过标签选择器获取获取文本内容

from bs4 import BeautifulSoup

html_doc = "<html><head><title>My Title</title></head><body><p>Hello, BeautifulSoup4!</p></body></html>"

# 实例化对象
# 基本语法: BeautifulSoup("需要解析的对象", "需要使用的解析器")
soup = BeautifulSoup(html_doc, 'lxml')

# 实现获取文本中的 p 整个标签
print(soup.p, soup.title)

# 实现获取 标签 中的内容
print(soup.p.string, soup.title.string)