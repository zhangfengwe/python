# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['qq.com']
    start_urls = ['http://qq.com/']

    def parse(self, response):
        response.xpath()
        pass

    def start_requests(self):
        pass