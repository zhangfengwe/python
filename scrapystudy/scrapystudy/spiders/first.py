# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapystudy.items import FirstItem
import time


class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        logging.info('{}、spider处理解析响应'.format(4))
        time.sleep(5)
        item = FirstItem()
        item['image_name'] = '美女'
        item['image_url'] = 'D://python/data/image/'
        yield item
