# -*- coding: utf-8 -*-
import scrapy
from python.study.python13_16.python14.python_scrapy.python_scrapy.items import BookItem
from python.study.other.config.logger import Logger


logger = Logger().get_logger()


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['www.boquge.com']
    start_urls = ['https://www.boquge.com/book/71607/']

    def parse(self, response):
        a_list = response.xpath('//ul[@id="chapters-list"]/li/a')[:6]
        # print(a_list.xpath('@href').get())
        i = 1
        for a in a_list:
            item = BookItem()
            item['chapter_name'] = a.xpath('text()').get()
            item['chapter_no'] = i
            yield scrapy.Request('https://www.boquge.com' + a.xpath('@href').get(),
                                 meta={'item': item}, callback=self.prase_content)
            i += 1

    def prase_content(self, response):
        # print('内容获取')
        content = response.xpath('//div[@id="txtContent"]/text()').getall()
        item = response.meta['item']
        item['chapter_content'] = content
        yield item
