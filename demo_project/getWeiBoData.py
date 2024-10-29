import requests
from jsonpath import jsonpath
import sys

# 这个的规则还没有发现，过几天再来
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
            "cookie": "XSRF-TOKEN=BT1IN_ZYnAX5cV3uikTcjNt9; _s_tentry="
                      "passport.weibo.com; appkey=; Apache=181887480269.689"
                      "03.1730143572653; SINAGLOBAL=181887480269.68903.1730143572653;"
                      " ULV=1730143572655:1:1:1:181887480269.68903.1730143572653:; "
                      "SCF=AscUSQaLBzDj6RSMLIuUweC-pPmALjHIq0_mRuAJlXOh7PQyfJ-FigH0H1R"
                      "sZctHvkVunQH1sDGno3b7PkhbR04.; SUB=_2A25KG5X8DeRhGeFG7lIW8i7JyT2I"
                      "HXVpWJc0rDV8PUNbmtAbLWrRkW9NeU1ZCB89nOP4Amc9O1qBcTKACa9ctFtj; SUB"
                      "P=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFGOMgoG4y-cV7rpooYoBll5NHD95QN"
                      "1h-7S0z7SKzpWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0nfehMEeh-EeBtt; ALF="
                      "02_1732735660; WBPSESS=rJkN6sDiPkCY6OwmtgSdSFD4IfWKWLNfpCV1n8-iaLfszzcE"
                      "hS7-VUO32sA_3znMEhtTsXkW39gB32kWK2KV9hRc7-ItQlsSPMtNaCsJhCU2"
                      "l4uizkQLcYpScrSw3lmfmFSUaV2j4lwdSUMe1j9W9A==",
            "referer": "https://weibo.com/5143998400/ODKBPhecW",
            "x-xsrf-token": "BT1IN_ZYnAX5cV3uikTcjNt9"
        }
        # 初始化一级评论参数
        self.first_comment = {
            "flow": "0",
            "is_reload": "1",
            "id": "5094739614106194",
            "is_show_bulletin": "2",
            "is_mix": "0",
            "max_id": "143415038223436",
            "count": "20",
            "uid": "5143998400",
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
        :return: response_json
        """
        try:
            response_str = requests.get(self.first_url, headers=self.header, params=self.first_comment)
            response_json = response_str.json()
            return response_json
        except Exception as e:
            print(f"error: {e}")
            sys.setrecursionlimit(10)
            self.get_one_data()

    def parse_data(self, json_data, *args, **kwargs):
        """
        解析数据
        :param json_data: 需要解析的数据
        :param args: 可选参数
        :param kwargs: 可选参数
        :return: None
        """
        print(json_data)
        try:
            text_one_raws = jsonpath(json_data, "$..data.*.text_raw")
            one_authors = jsonpath(json_data, "$..data.*.screen_name")
            for text_one_raw, one_author in zip(text_one_raws, one_authors):
                print(text_one_raw, one_author)
        except Exception as e:
            print(f"error: {e}")
            sys.setrecursionlimit(10)
            self.parse_data(json_data)

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
        self.parse_data(self.get_one_data())

if __name__ == "__main__":
    getWeiBoComments = GetWeiBoComments()
    getWeiBoComments.run()