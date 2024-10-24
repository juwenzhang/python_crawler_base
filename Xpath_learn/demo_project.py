import json
import requests
from lxml import etree

class Spider(object):
    # 先实现书写我们的构造函数 (初始化方法: 就是我们的一个类实现的时候，初始化方法里面的内容自动完成)
    def __init__(self, *args, **kwargs):
        """
        构造函数(初始化方法)
        """
        self.url = "http://hnbitebi.com/hlist-7-1.html"  # 我们实现发送请求的网址(实例属性)
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "upgrade-insecure-requests": "1",
        }  # 实现的是爬虫的伪装(实例属性)


    def get_data(self, url, *args, **kwargs):
        """
        获取数据
        :param url:
        :return: xml_doc
        """
        res = requests.get(url, headers=self.headers).text
        xml_doc = etree.HTML(res)  # 实现将我们的html代码转化为xml语法
        return xml_doc


    def parse_data(self, xml_doc, *args, **kwargs):
        """
        解析数据
        :param xml_doc:
        :return:
        """
        title_links = xml_doc.xpath('//ul[@class="list2"]/li/h3/a/@href')  # 实现获取的是链接 title_links
        titles = xml_doc.xpath('//ul[@class="list2"]/li/h3/a/text()')  # 实现获取的是我们的标题 titles
        title_discs = xml_doc.xpath('//ul[@class="list2"]/li/p/text()')  # 实现获取的文章描述信息 title_descs
        # print(len(titles), len(title_links))  # 25 25

        for title, title_link, title_desc in zip(titles, title_links, title_discs):
            print(title)
            print(title_link)
            print(title_desc)
            self.parse_detail_data(title_link)
            print("===================================")


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
        :return:
        """
        xml_doc = self.get_data(title_link)
        contents_base = xml_doc.xpath('//div[@class="con"]/div//text()')
        content = self.remove_char(" ", contents_base, "s3(); ", " ")
        print(json.loads(content))


    def save_data(self, *args, **kwargs):
        """保存数据"""
        pass


    def run(self, *args, **kwargs):
        """启动项目的入口"""
        xml_data = self.get_data(self.url)
        self.parse_data(xml_data)


if __name__ == "__main__":
    spider = Spider()
    spider.run()