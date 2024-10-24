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


    def get_data(self):
        """获取数据"""
        pass


    def parse_data(self):
        """解析数据"""
        pass


    def save_data(self):
        """保存数据"""
        pass


    def run(self):
        """运行程序"""
        pass


if __name__ == "__main__":
    getDataFromWangYi = GetDataFromWangYi()

    getDataFromWangYi.run()