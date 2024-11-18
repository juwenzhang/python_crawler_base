import scrapy


class MyScrapySpider(scrapy.Spider):
    name = "my_scrapy"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com/"]

    def parse(self, response):
        print(response)