import json
import re
import sys
import requests
from jsonpath import jsonpath
from pymysql import connect


class GetDataFromWangYi(object):
    def __init__(self, *args, **kwargs):
        """
        构造函数的书写
        :param args: 可选参数
        :param kwargs: 可选参数
        :returns: None
        """
        self.url = "https://news.163.com/special/cm_yaowen20200213/?callback=data_callback"
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;'
                          ' x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/129.0.0.0 Safari/537.36',
        }

        self.conn = connect(
            user='root',
            password='451674',
            database='python_crawler',
            host='localhost',
            charset='utf8mb4',
            port=3306
        )
        self.cursor = self.conn.cursor()


    def __del__(self, *args, **kwargs):
        """
        析构函数的书写
        :param args: 可选参数
        :param kwargs: 可选参数
        :return: None
        """
        print("\n\n本次爬取任务完毕...")


    @staticmethod
    def remove_char(content, *args, **kwargs):
        """
        用来实现对返回数据的字符串实现处理的函数
        :param content: 需要改动的字符串
        :param args: 可选参数
        :param kwargs: 可选参数
        :return: re.search('data_callback\((.*?)\)', content, re.S)
        """
        # return content.replace(del_char, replace_char)
        # 在这里我们使用字符串切割也行的
        return re.search('data_callback\((.*)\)', content, re.S).group(1)


    def get_data(self, *args, **kwargs):
        """
        获取数据
        :param args: 可选参数
        :param kwargs: 可选参数
        :return: response
        """
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
        :param data: 进行解析的数据
        :param args: 可选参数
        :param kwargs: 可选参数
        :return:
        """
        result_str = self.remove_char(data)
        result_json = json.loads(result_str)

        try:
            titles = jsonpath(result_json, "$..title")
            tlinks = jsonpath(result_json, "$..tlink")
            sources = jsonpath(result_json, "$..source")
            data_docker = []
            for title, tlink, source in zip(titles, tlinks, sources):
                data_docker.append([title, tlink, source])
            self.save_data(data_docker)

        except Exception as e:
            print(f"error: {e}")
            sys.setrecursionlimit(10)
            self.parse_data(data)


    def save_data(self, data, *args, **kwargs):
        """
        保存数据
        :param data: 需要实现存储的数据
        :param args: 可选参数
        :param kwargs: 可选参数
        :return: None
        """
        sql = ("insert into getWanyiData "
               "(title, tlink, source) "
               "values (%s, %s, %s)")

        try:
            self.cursor.executemany(sql, data)
            self.conn.commit()
            print("存储数据成功...")
        except Exception as e:
            print(f"error: {e}")
            self.conn.rollback()
            sys.setrecursionlimit(10)
            self.save_data(data)


    def run(self, *args, **kwargs):
        """启动程序"""
        self.parse_data(self.get_data())
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    getDataFromWangYi = GetDataFromWangYi()
    getDataFromWangYi.run()