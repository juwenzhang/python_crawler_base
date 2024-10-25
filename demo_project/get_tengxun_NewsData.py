# 开始实现我们的获取腾讯网的数据

import requests
from jsonpath import jsonpath
from openpyxl import Workbook
import sys


def get_TengXun_NewsData(page: int, *args, **kwargs) -> str:
    """获取响应"""
    # 发送请求的网址
    # 防止因为网络波动导致的请求数据失败，异常捕捉，并且再次发送请求
    try:
        url = "https://i.news.qq.com/web_feed/getHotModuleList"

        # 配置伪装信息
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8"
        }

        # 配置需要传输的数据，同时考虑最后的翻页爬取数据问题
        data = ('{"base_req":{"from":"pc"},"forward":"2","qimei36":"0_MjahR7CwtwXxx",'
                '"device_id":"0_MjahR7CwtwXxx","flush_num":%d,"channel_id":"news_news_top","item_count":20}') % page

        print("正在爬取第{}页".format(page))
        # print(requests.post(url, headers=headers, data=data).json())
        return requests.post(url, headers=headers, data=data, timeout=10).json()
    except Exception as e:
        print(e)
        # 设置递归深度
        sys.setrecursionlimit(20)
        get_TengXun_NewsData(page=page, *args, **kwargs)


def parse_TengXun_NewsData(json_data: str):
    """解析数据"""
    titles = jsonpath(json_data, "$..title")  # 获取标题
    publish_times = jsonpath(json_data, "$..publish_time")  # 获取发布时间
    # chl_names = jsonpath(json_data, "$..media_info.chl_name")  # 获取来源
    urls = jsonpath(json_data, "$..url")  # 获取链接

    # 开始判断爬取的内容是否条数一致,但是发现实际的来源条数 chl_names 不一致
    # print(len(titles), len(publish_times), len(chl_names), len(urls))
    chl_names = []
    data_media_infos = json_data["data"]
    for data_medias in data_media_infos:
        # media_info_item = data_medias["media_info"]
        # if "chl_name" in media_info_item:
        #     chl_names.append(media_info_item["chl_name"])
        # else:
        #     chl_names.append("来源丢失或者来源不存在")
        try:
            chl_names.append(data_medias["media_info"]["chl_name"])
        except KeyError:
            chl_names.append("来源丢失或者来源不存在")
    # print(len(chl_names))  这个时候就解决了数据条数的不一致的问题

    # 开始实现将数据进行分组存储处理
    for data_item in zip(titles, publish_times, urls, chl_names):
        save_TengXun_NewsData(data_item[0], data_item[1], data_item[2], data_item[3])


def save_TengXun_NewsData(title: str, publish_time: str, url: str, chl_name: str):
    """保存数据"""
    # 开始实现操作并且保存数据到 excel 表中
    ws.append([title, publish_time, url, chl_name])

    wb.save("TengXun_NewsData.xlsx")


if __name__ == '__main__':
    wb = Workbook()
    ws = wb.active
    # 注意重复的激活 excel 表 ，会导致前面的数据被覆盖
    ws.append(["新闻标题", "发布时间", "访问地址", "来源"])

    for index in range(1, 12):
        try:
            response = get_TengXun_NewsData(index)
            parse_TengXun_NewsData(response)
        except Exception as e:
            print(e)
