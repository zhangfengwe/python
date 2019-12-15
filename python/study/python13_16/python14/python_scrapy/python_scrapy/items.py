# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PythonScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city_name = scrapy.Field()
    pass


class BookItem(scrapy.Item):

    # 章节号
    chapter_no = scrapy.Field()
    # 章节名
    chapter_name = scrapy.Field()
    # 章节内容
    chapter_content = scrapy.Field()

