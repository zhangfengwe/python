# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from python.study.other.config.logger import Logger
from python.study.other.util import reutil
from pymongo import MongoClient
import traceback

logger = Logger().get_logger()


class PythonScrapyPipeline(object):

    def __init__(self):
        dbclient = MongoClient(host='localhost', port=27017)
        self.db = dbclient.book
        self.content_coll = self.db.content
        self.book_coll = self.db.book

    def process_item(self, item, spider):
        # print('处理item')
        try:
            chapter_content_list = item['chapter_content']
            chapter_content = ''
            for chapter in chapter_content_list:
                chapter = reutil.reject_unicode('\t\r\n', reutil.reject_unicode('\u3000', chapter))
                chapter.replace(' ', '')
                if not reutil.check_chinese(chapter):
                    continue
                chapter_content += chapter
            logger.info('result  {}'.format(chapter_content.strip()))
            item['chapter_content'] = chapter_content.strip()
            self.book_coll.insert_one(dict(item))
        except Exception:
            logger.error(traceback.format_exc())
