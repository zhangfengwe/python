# 图片爬虫

import scrapy


class ImageSpider(scrapy.Spider):

    name = 'image'
    allowed_domains = ['image.baidu.com']
    start_urls = ['']

    def parse(self, response):
        pass
