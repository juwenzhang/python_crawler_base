# 便尊选择器： 通过标签名实现查找内容

from bs4 import BeautifulSoup

html_doc = "<html><head><title>My Title</title></head><body><p>Hello, BeautifulSoup4!</p></body></html>"

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.find_all("p")[0].getText())
print(soup.find_all("p")[0].string)
print(soup.find_all("p")[0].name)