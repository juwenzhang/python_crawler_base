import requests
from jsonpath import jsonpath


class GetWeiBoComments(object):
    def __init__(self, *args, **kwargs):
        """
        构造函数
        :param args: 可选参数
        :param kwargs: 可选参数
        """
        self.first_url = "https://weibo.com/ajax/statuses/buildComments/"
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "cookie": "XSRF-TOKEN=BT1IN_ZYnAX5cV3uikTcjNt9; PC_TOKEN=2a3ebefad0; _s_"
                      "tentry=passport.weibo.com; appkey=; Apache=181887480269.68903."
                      "1730143572653; SINAGLOBAL=181887480269.68903.1730143572653; UL"
                      "V=1730143572655:1:1:1:181887480269.68903.1730143572653:; SCF=A"
                      "scUSQaLBzDj6RSMLIuUweC-pPmALjHIq0_mRuAJlXOh7PQyfJ-FigH0H1RsZct"
                      "HvkVunQH1sDGno3b7PkhbR04.; SUB=_2A25KG5X8DeRhGeFG7lIW8i7JyT2IH"
                      "XVpWJc0rDV8PUNbmtAbLWrRkW9NeU1ZCB89nOP4Amc9O1qBcTKACa9ctFtj; SU"
                      "BP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFGOMgoG4y-cV7rpooYoBll5NH"
                      "D95QN1h-7S0z7SKzpWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0nfehMEeh-EeB"
                      "tt; ALF=02_1732735660; WBPSESS=rJkN6sDiPkCY6OwmtgSdSFD4IfWKWLNfp"
                      "CV1n8-iaLfszzcEhS7-VUO32sA_3znM54UD4Oi0iNI9wW6EilChg8xca2Db"
                      "YwwQjitDOBbaZTv7S9TcIdLbm02JAiJRC4wgy1C0_ta1kbnbvdY4_WI4Ow==",
            "referer": "https://weibo.com/1745981242/ODxdr3Km6"
        }
        # 初始化一级评论参数
        self.first_comment = {
            "flow": "0",
            "is_reload": "1",
            "id": "5094224770893178",
            "is_show_bulletin": "3",
            "is_mix": "0",
            "max_id": "139291837783097",
            "count": "20",
            "uid": "1745981242",
            "fetch_level": "0",
            "locale": "zh-CN"
        }

    def __del__(self, *args, **kwargs):
        """
        析构函数书写
        :param args: 可选参数
        :param kwargs: 可选承诺书
        :return: None
        """
        print("此次爬取任务完毕...")

    def get_one_data(self, *args, **kwargs):
        """
        获取数据
        :param args: 可选参数
        :param kwargs: 可选参数
        :return: response
        """
        response = requests.get(self.first_url, headers=self.header, params=self.first_comment).json()
        return response

    def parse_data(self, *args, **kwargs):
        """
        解析数据
        :param args: 可选参数
        :param kwargs: 可选参数
        :return: None
        """
        pass

    def save_data(self, *args, **kwargs):
        """
        保存数据
        :param args: 可选参数
        :param kwargs: 可选参数
        :return: None
        """
        pass

    def run(self, *args, **kwargs):
        """
        运行函数
        :param args: 可选参数
        :param kwargs: 可选参数
        :return: None
        """
        print(self.get_one_data())

if __name__ == "__main__":
    getWeiBoComments = GetWeiBoComments()
    getWeiBoComments.run()