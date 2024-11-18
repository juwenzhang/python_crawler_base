import scrapy


class BaiduScrapySpider(scrapy.Spider):
    name = "baidu_scrapy"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com/"]

    def parse(self, response, **kwargs):
        print(response.text)
