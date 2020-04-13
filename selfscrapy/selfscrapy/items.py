# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Compose
from python.study.other.util import reutil


def book_author_process(value):
    return value.split('：')[1].strip()


def book_name_process(value):
    return reutil.reject_unicode('\u3000', value)


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
    # 书籍编号
    book_no = scrapy.Field()


class BookInf(scrapy.Item):

    book_name = scrapy.Field(
        input_processor=TakeFirst(),
        output_processor=Compose(book_name_process)
    )

    book_author = scrapy.Field(
        input_processor=TakeFirst(),
        output_processor=MapCompose(book_author_process)
    )

    book_no = scrapy.Field()


