# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from python.study.other.config.logger import Logger
from python.study.other.util import reutil
from selfscrapy.items import BookItem, BookInf
from pymongo import MongoClient
import traceback

logger = Logger().get_logger()


class PythonScrapyPipeline(object):

    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.mongo_db = db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get('MONGODB_HOST', 'localhost'),
            int(crawler.settings.get('MONGODB_PORT', 27017)),
            crawler.settings.get('MONGODB_DB', 'book')
        )

    def close_spider(self):
        self.client.close()

    def open_spider(self):
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):

        if isinstance(item, BookItem):
            self.process_book_content(item, spider)
        elif isinstance(item, BookInf):
            self.prcess_book_inf(item, spider)

    def process_book_content(self, item, spider):
        try:
            chapter_content_list = item['chapter_content']
            chapter_content = ''
            for chapter in chapter_content_list:
                chapter = reutil.reject_unicode('\t\r\n', reutil.reject_unicode('\u3000', chapter))
                chapter.replace(' ', '')
                if not reutil.check_chinese(chapter):
                    continue
                chapter_content += chapter
            # logger.info('result  {}'.format(chapter_content.strip()))
            item['chapter_content'] = chapter_content.strip()
            item_dict = dict(item)
            self.db[item_dict.pop('book_no')].insert_one(item_dict)
        except Exception:
            logger.error(traceback.format_exc())

    def prcess_book_inf(self, item, spider):
        try:
            logger.info(item)
            if not self.db.bookinf.find({'book_no': item['book_no']}).count():
                self.db.bookinf.insert_one(dict(item))
        except Exception:
            logger.error(traceback.format_exc())


class BookPipeline(object):

    def __init__(self):
        dbclient = MongoClient(host='localhost', port=27017)
        self.db = dbclient.book
        self.coll = self.db.bookinf

    def process_item(self, item, spider):
        if isinstance(item, BookInf):
            self.prcess_book_inf(item, spider)

    def prcess_book_inf(self, item, spider):
        try:
            if not self.coll.find({'book_no': item['book_no']}).count():
                self.coll.insert_one(dict(item))
        except Exception:
            logger.error(traceback.format_exc())
