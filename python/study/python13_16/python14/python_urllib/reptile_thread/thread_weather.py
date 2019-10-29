# 多线程爬取城市天气数据

import requests
from threading import Thread, Lock
from queue import Queue, Empty
from bs4 import BeautifulSoup
from time import time, sleep
from python.study.other.config.logger import Logger
from python.study.other.config.readconfig import MyConfig
from python.study.other.util import fileutil, requestutil
import traceback
from python.study.python13_16.python14.python_urllib.file_to_db import read_file
from os import path

logger = Logger().get_logger()

CRAWL_EXIT = False
PARSE_EXIT = False
base_path = MyConfig.get_value('path', 'base_path')


class FindData(Thread):

    def __init__(self, thread_name, url_queue, data_queue):
        super().__init__()
        # 线程名
        self.thread_name = thread_name
        # 数据队列
        self.data_queue = data_queue
        # url队列
        self.url_queue = url_queue

    def run(self):
        logger.info('{} is start'.format(self.thread_name))
        global CRAWL_EXIT
        while not CRAWL_EXIT:
            try:
                if self.url_queue.empty():
                    CRAWL_EXIT = True
                    continue
                urldata = self.url_queue.get(False)
                soup = BeautifulSoup(requestutil.get_response(urldata[2], timeout=3), 'html.parser')
                # soup = self.get_data(urldata[2])
                urldata.append(soup)
                sleep(0.05)
                self.data_queue.put(urldata)
            except:
                logger.error(traceback.format_exc())
        logger.info('{} is end'.format(self.thread_name))


class ParseData(Thread):

    def __init__(self, thread_name, data_queue):
        super().__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue

    def run(self):
        logger.info('解析进程 {} is start'.format(self.thread_name))
        global PARSE_EXIT
        while not PARSE_EXIT:
            try:
                urldata = self.data_queue.get(True, timeout=300)
                # if self.data_queue.empty():
                #     PARSE_EXIT = True
                #     continue
                self.data_to_file(urldata)
            except Empty:
                # if self.data_queue.empty():
                PARSE_EXIT = True
                logger.error('Queue is empty')
            except:
                logger.error(traceback.format_exc())
        logger.info('解析进程 {} is end'.format(self.thread_name))

    def data_to_file(self, urldata):
        '''
        :param urldata:
        :type urldata list
        :return:
        '''
        # 文件名 城市拼音 + ‘_’ + 月份
        # 文件路径 base_path + '/data/weather/matplot_data/city_weather_data/' + 城市名汉字/
        filename = base_path + '/data/weather/matplot_data/city_weather_data/' + urldata[0] + \
                   '/' + urldata[2][24:-12] + '_' + urldata[1] + '.csv'
        if fileutil.is_dir_live(filename, create=True):
            with open(filename, 'w') as file:
                # for url in urls:
                # soup = get_response_soup(urldata[2])
                soup = urldata[-1]
                weather_list = soup.select('div[class="tqtongji2"]')
                for weather in weather_list:
                    ul_list = weather.select('ul')
                    i = 0
                    for ul in ul_list:
                        li_list = ul.select('li')
                        str2 = ""
                        for li in li_list:
                            str2 += (li.string if li.string else '') + ','
                        if i != 0:
                            file.write(str2 + '\n')
                        i += 1
            sleep(0.05)


def getdata_file():
    allfiles = fileutil.get_all_file(path.join(base_path, 'data/weather/matplot_data/city_url_month'))
    urldatas = []
    start = time()
    for file in allfiles:
        # logger.info('start trans data from {} to db'.format(file))
        filedatas = read_file(file)
        # for filedata in filedatas:
        #     get_data_to_file(filedata)
        urldatas.extend(filedatas)
    end = time()
    logger.info('获取所有数据，共耗时{}'.format(end - start))
    return urldatas


def main():
    url_queue = Queue(1000000)
    urldatas = getdata_file()
    for urldata in urldatas:
        url_queue.put(urldata)

    data_queue = Queue()

    crawl_list = ['采集1号', '采集2号', '采集3号', '采集4号', '采集5号']
    thread_crawl = []
    for crawl in crawl_list:
        crawl_thread = FindData(crawl, url_queue, data_queue)
        crawl_thread.start()
        thread_crawl.append(crawl_thread)

    # 三个解析线程的名字
    parse_list = ["解析线程1号", "解析线程2号", "解析线程3号"]
    # 存储三个解析线程
    # threadparse = []
    for threadName in parse_list:
        thread = ParseData(threadName, data_queue)
        thread.start()
        thread_crawl.append(thread)

    for threads in thread_crawl:
        threads.join()


if __name__ == '__main__':
    main()
