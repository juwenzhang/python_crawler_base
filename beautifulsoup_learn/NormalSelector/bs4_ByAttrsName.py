from bs4 import BeautifulSoup

html_doc = "<html><head><title>My Title</title></head><body><p class='element'>Hello, BeautifulSoup4!</p></body></html>"

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.find_all("p", {"class": "element"})[0].getText())
print(soup.find_all("p", {"class": "element"})[0].name)
print(soup.find_all("p", {"class": "element"})[0].text)
print(soup.find_all("p", {"class": "element"})[0].string)