# 开始通过标签选择器获取我们的 标签属性值

from bs4 import BeautifulSoup

html_doc = """
                <! DOCUMENT HTML>
                <html>
                    <head></head>
                    <body>
                        <a href="https://google.com">Google></a>
                    </body>
                </html    
            """

# 实例化对象
soup = BeautifulSoup(html_doc, 'lxml')

# 获取 a 标签中的 href 值
print(soup.a.attrs["href"])
print(soup.a["href"])