# 开始实现我们的爬取一个 GuShiWen 网站的数据
import os
import requests
from lxml import etree
from chaojiying_Python.chaojiying import Chaojiying_Client


class GetGuShiWenData(object):
    def __init__(self):
        self.index_url = "https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537."
                          "36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        }

    def __del__(self):
        """
        析构函数
        :return:
        """
        print("此次爬虫任务完毕...")

    def get_image_url(self):
        """
        用来实现获取我们的验证码请求链接网的处理函数
        :return: f"https://so.gushiwen.cn{response_xml}"
        """
        response_html = requests.get(self.index_url, headers=self.headers).text
        response_xml = etree.HTML(response_html).xpath('//img[@id="imgCode"]/@src')[0]
        return f"https://so.gushiwen.cn{response_xml}"

    def save_image_data(self, url):
        """
        实现的是保存我们爬取的图片连接
        :param url:
        :return: img_path
        """
        img_data = requests.get(url, headers=self.headers).content
        img_path = "../get_image/parse_guzhiwen.jpg"
        if os.path.exists(img_path):
            with open(img_path, "r+b") as f:
                f.write(img_data)
        else:
            with open(img_path, "w+b") as f:
                f.write(img_data)
        return img_path

    def get_image_data(self, path):
        """
        实现获取验证码操作
        :param path:
        :return: ChaoJiYing.PostPic(img, 1004)['pic_str']
        """
        ChaoJiYing = Chaojiying_Client("juwenzhang", "451674jh", '958562')
        img = open(path, "rb").read()
        return ChaoJiYing.PostPic(img, 1004)['pic_str']

    def parse_data(self):
        pass

    def save_dara(self):
        pass

    def run(self):
        img_url = self.get_image_url()
        img_path = self.save_image_data(img_url)
        self.get_image_data(img_path)

if __name__ == "__main__":
    getGuShiWenData = GetGuShiWenData()
    getGuShiWenData.run()