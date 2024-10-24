import json
import sys
import requests
from lxml import etree
from pymysql import connect

class Spider(object):
    # 先实现书写我们的构造函数 (初始化方法: 就是我们的一个类实现的时候，初始化方法里面的内容自动完成)
    def __init__(self, *args, **kwargs):
        """
        构造函数(初始化方法)
        """
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "upgrade-insecure-requests": "1",
        }  # 实现的是爬虫的伪装(实例属性)

        # 连接数据库的操作
        self.conn = connect(
            user='root',
            password='451674',
            host='127.0.0.1',
            database='python_crawler',
            port=3306,
            charset='utf8mb4'
        )
        # 通过我们的连接对象来实现获取游标对象
        self.cursor = self.conn.cursor()


    def get_data(self, url, *args, **kwargs):
        """
        获取数据
        :param url:
        :return: xml_doc
        """
        try:
            res = requests.get(url, headers=self.headers).text
            xml_doc = etree.HTML(res)  # 实现将我们的html代码转化为xml语法
            return xml_doc
        except Exception as e:
            print(f"error: {e}")


    def parse_data(self, xml_doc, *args, **kwargs):
        """
        解析数据
        :param xml_doc:
        :return: title_docker
        """
        try:
            title_links = xml_doc.xpath('//ul[@class="list2"]/li/h3/a/@href')  # 实现获取的是链接 title_links
            titles = xml_doc.xpath('//ul[@class="list2"]/li/h3/a/text()')  # 实现获取的是我们的标题 titles
            title_discs = xml_doc.xpath('//ul[@class="list2"]/li/p/text()')  # 实现获取的文章描述信息 title_descs
            # print(len(titles), len(title_links))  # 25 25

            title_docker = []
            for title, title_link, title_desc in zip(titles, title_links, title_discs):
                title_content = self.parse_detail_data(title_link)
                title_docker.append([title, title_link, title_desc, title_content])
            return title_docker
        except Exception as e:
            print(f"error: {e}")


    def remove_char(self, sep, content, remove_char, replace_char, *args, **kwargs):
        """
        用来实现清除不需要的字符,同时转化为 json 格式的数据
        :param sep:
        :param content:
        :param remove_char:
        :param replace_char:
        :param args:
        :param kwargs:
        :return:
        """
        content_str =  sep.join(map(str, content)).replace(remove_char, replace_char)
        content_json = json.dumps(content_str)
        return content_json


    def parse_detail_data(self, title_link, *args, **kwargs):
        """
        解析详情页数据
        :param title_link:
        :return: content
        """
        try:
            xml_doc = self.get_data(title_link)
            # 实现匹配数据
            contents_base = xml_doc.xpath('//div[@class="con"]/div//text()')
            # 初步解析数据
            content = self.remove_char(" ", contents_base, "s3(); ", "")
            # 进一步解析数据
            content = self.remove_char("", json.loads(content),
                                       "【www.hnbitebi.com--情话】 ", "")
            # 需要反序列化取数据
            return content
        except Exception as e:
            print(f"error: {e}")


    def save_data(self, data: list, *args, **kwargs):
        """
        保存数据
        :param data:
        :param args:
        :param kwargs:
        :return:
        """
        sql = ("insert into article_data "
               "(title, title_link, title_desc, title_content) "
               "values (%s, %s, %s, %s)")

        try:
            self.cursor.executemany(sql, data)  # 执行语句， 通过游标来实现执行语句
            self.conn.commit()  # 提交事务
            print("数据存储成功")

        except Exception as e:
            print(f'error: {e}')
            self.conn.rollback()  # 实现数据库的回滚
            # 实现设置递归深度
            sys.setrecursionlimit(10)
            self.save_data(data)


    def run(self, *args, **kwargs):
        """
        启动项目的入口
        :param args:
        :param kwargs:
        :return:
        """
        for page in range(1, 44):  # [1, 44)
            self.url = "http://hnbitebi.com/hlist-7-{}.html".format(page)  # 我们实现发送请求的网址(实例属性)
            print(f"当前爬取网页是: {self.url}")
            xml_data = self.get_data(self.url)
            data = self.parse_data(xml_data)
            self.save_data(data)

        self.cursor.close()
        self.conn.close()  # 最后关闭数据库


if __name__ == "__main__":
    spider = Spider()
    spider.run()

# 为了降低时间复杂度，我们是可以直接将保存数据的操作在 parse_data 中实现操作的
# 我们当前的情况是实现了两次 for 循环，这个时候时间复杂度就直接上来了