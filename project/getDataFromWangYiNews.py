import sys
from pkgutil import get_data

import requests


class GetDataFromWangYi(object):
    def __init__(self):
        """
        构造函数的书写
        """
        self.url = "https://news.163.com/special/cm_yaowen20200213/?callback=data_callback"
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;'
                          ' x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/129.0.0.0 Safari/537.36',
        }

    def __del__(self):
        """
        析构函数的书写
        :return:
        """
        print("本次爬取任务完毕...")


    def remove_char(self, content, del_char, replace_char, *args, **kwargs) -> str:
        """
        用来实现对返回数据的字符串实现处理的函数
        :param content:
        :param del_char:
        :param replace_char:
        :param args:
        :param kwargs:
        :return: content.replace(del_char, replace_char)
        """
        return content.replace(del_char, replace_char)


    def get_data(self, *args, **kwargs):
        """获取数据"""
        try:
            response = requests.get(self.url, headers=self.headers).text
            return response

        except Exception as e:
            print(f"error: {e}")
            # 实现设置递归深度
            sys.setrecursionlimit(20)
            self.get_data()



    def parse_data(self, data, *args, **kwargs):
        """
        解析数据: 将响应报文中的数据实现处理成 json 数据
        :param data:
        :param args:
        :param kwargs:
        :return:
        """
        first_data = self.remove_char(data, 'data_callback(', "")
        finally_data = self.remove_char(first_data, ')', "")
        print(finally_data)


    def save_data(self, *args, **kwargs):
        """保存数据"""
        pass


    def run(self, *args, **kwargs):
        """启动程序"""
        self.parse_data(self.get_data())


if __name__ == "__main__":
    getDataFromWangYi = GetDataFromWangYi()
    getDataFromWangYi.run()