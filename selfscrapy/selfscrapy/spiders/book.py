# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
import re
from selfscrapy.items import BookItem, BookInf

from python.study.other.config.logger import Logger


logger = Logger().get_logger()


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['www.boquge.com']
    start_urls = ['https://www.boquge.com/book/71607/', 'https://www.boquge.com/book/118371/']

    # def start_requests(self):
    #     pass

    def parse(self, response):

        a_list = response.xpath('//ul[@id="chapters-list"]/li/a')[:5]

        book_loader = ItemLoader(BookInf(), response=response)
        book_loader.add_xpath('book_name', '//article/div[@class="panel-body"]/ul/li/h1/text()')
        book_loader.add_xpath('book_author', '//article/div[@class="panel-body"]/ul/li/h1/small/text()')
        book_no = re.findall('^/book/(.+?)/', a_list[0].xpath('@href').get())[0]
        book_loader.add_value('book_no', book_no)
        # book_name = response.xpath('//article/div[@class="panel-body"]/ul/li/h1/text()').get()
        # book_name = reutil.reject_unicode('\u3000', book_name)
        # book_author = response.xpath('//article/div[@class="panel-body"]/ul/li/h1/small/text()').get() \
        #         .split('：')[1].strip()
        i = 1
        book_dict = {book_no: i}
        yield book_loader.load_item()
        for a in a_list:
            item = BookItem()
            item['chapter_name'] = a.xpath('text()').get()
            item['chapter_no'] = book_dict[book_no]
            item['book_no'] = book_no
            # 使用follow方法生成新的请求，参数与request一致，但是url可以是相对URL或 scrapy.link.Link 对象，而不仅仅是绝对URL
            yield response.follow(a, meta={'item': item}, callback=self.prase_content)
            # yield scrapy.Request('https://www.boquge.com' + a.xpath('@href').get(),
            #                      meta={'item': item}, callback=self.prase_content)
            book_dict[book_no] += 1

    def prase_content(self, response):
        # print('内容获取')
        content = response.xpath('//div[@id="txtContent"]/text()').getall()
        item = response.meta['item']
        item['chapter_content'] = content
        if not content:
            logger.info('{} 获取内容为空'.format(response.url))
        yield item

    @staticmethod
    def get_book(book_no, book_name, book_author):

        book_inf_item = BookInf()
        book_inf_item['book_no'] = book_no
        book_inf_item['book_name'] = book_name
        book_inf_item['book_author'] = book_author

        return book_inf_item
