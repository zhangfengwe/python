# 爬取小说

import requests
from bs4 import BeautifulSoup
from python.study.other.config.logger import Logger
import os
from time import sleep, time
from python.study.other.config.readconfig import MyConfig
import python.study.other.util.fileutil as fileutil

logger = Logger().get_logger()


def get_response(url):
    start = time()
    header = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
    kv = {'user-agent': header}
    response = requests.get(url, headers=kv)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    end = time()
    logger.info('request获取{}网页耗时{}'.format(url, end - start))
    return soup


def prase_char(soup, baseurl):
    base_path = MyConfig.get_value('path', 'base_path') + 'book/'
    ul = soup.select_one('ul[id="chapters-list"]')
    li_list = ul.select('li')
    filepath = base_path
    # with open('bookurl.csv', 'w', encoding='GBK') as file:
    for li in li_list:
        strurl = ''

        a = li.select_one('a')
        if not a:
            filepath = base_path
            filepath += li.string.replace(' ', '')
            logger.info('书部路径{}'.format(filepath))
            # os.makedirs(base_path + li.string)
            continue
        logger.info('fffff{}'.format(filepath))
        get_content(baseurl + a.attrs['href'], filepath + '/' + a.string + '.txt')
        strurl += baseurl + a.attrs['href'] + ',' + a.string + '\n'
        # file.write(strurl)
    sleep(0.05)


def get_content(url, file_path):
    soup = get_response(url)
    logger.info('true file path is {}'.format(file_path))
    fileutil.is_dir_live(file_path, True)
    with open(file_path, 'w', encoding='utf-8') as file:
        content = ''
        h1 = soup.select_one('h1')
        logger.info('h1{}'.format(h1.string))
        content += h1.string

        div = soup.select_one('div[id="txtContent"]')
        content += div.text.strip(' ').replace('<br/>', '\n')
        file.write(content)


if __name__ == '__main__':
    prase_char(get_response('https://www.boquge.com/book/71607/'), 'https://www.boquge.com')

