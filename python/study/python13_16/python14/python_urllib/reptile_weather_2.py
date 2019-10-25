# 获取城市每月天气数据

import requests
from bs4 import BeautifulSoup
from python.study.other.util import fileutil, oracledb
from python.study.other.config.logger import Logger
from python.study.other.config.readconfig import MyConfig
from time import sleep, time
import traceback
from python.study.python13_16.python14.python_urllib.file_to_db import read_file
from os import path

logger = Logger().get_logger()
base_path = MyConfig.get_value('path', 'base_path')
# 获取城市名语句
getcityssql = '''select distinct(city_name) from city_weather_url'''
# 获取城市数据语句
getcityurlsql = '''select city_name, city_weather_month, city_weather_url from city_weather_url where city_name = :1'''


def get_response_soup(url):
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


def get_data_to_file(urldata):
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
            soup = get_response_soup(urldata[2])
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


def get_data(curs, city=None):
    try:
        parm_geturl = [getcityurlsql]
        parm_getcity = [getcityssql]
        if city:
            start = time()
            parm_geturl.append([city])
            urldatas = oracledb.select(curs, parm_geturl)
            for urldata in urldatas:
                get_data_to_file(urldata)
            end = time()
            logger.info('{} 数据获取完毕，耗时{}'.format(city, end - start))
        else:
            citys = oracledb.select(curs, parm_getcity)
            for city in citys:
                get_data(curs, city)
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e


def getdata_main(city):
    try:
        coon, curs = oracledb.con()
        start = time()
        get_data(curs, city)
        end = time()
        logger.info('此次任务共耗时{}'.format(end - start))
    except:
        logger.error(traceback.format_exc())
    finally:
        coon.close()


def getdata_file():
    allfiles = fileutil.get_all_file(path.join(base_path, 'data/weather/matplot_data/city_url_month'))
    start = time()
    for file in allfiles:
        logger.info('start trans data from {} to db'.format(file))
        filedatas = read_file(file)
        for filedata in filedatas:
            get_data_to_file(filedata)
    end = time()
    logger.info('共耗时{}'.format(end - start))


if __name__ == '__main__':
    # getdata_main('单县')
    getdata_file()



