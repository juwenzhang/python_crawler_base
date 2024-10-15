from bs4 import BeautifulSoup

html_doc = "<html><head><title>My Title</title></head><body><p class='element'>Hello, BeautifulSoup4!</p></body></html>"

soup = BeautifulSoup(html_doc ,"lxml")

print(soup.select(".element"))
print(soup.select(".element")[0].name)
print(soup.select(".element")[0].text)
print(soup.select(".element")[0].attrs)
print(soup.select(".element")[0].getText())