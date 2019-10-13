# 爬虫练习
import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
import matplotlib
import python.study.other.util.fileutil as fileutil
import python.study.other.util.strutil as strutil
from python.study.other.config.logger import Logger
import os
from time import sleep, time

matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


logger = Logger().get_logger()


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


def get_data(urls):

    with open('matplot_data/wuhan_weather.csv', 'w') as file:
        for url in urls:
            soup = get_response_soup(url)
            weather_list = soup.select('div[class="tqtongji2"]')

            for weather in weather_list:
                ul_list = weather.select('ul')
                i = 0
                for ul in ul_list:
                    li_list = ul.select('li')
                    str2 = ""
                    for li in li_list:
                        str2 += li.string + ','
                    if i != 0:
                        file.write(str2 + '\n')
                    i += 1


def get_city_url(url):
    file_path = 'matplot_data/city_url/citys_url_'
    if fileutil.is_dir_live(file_path, True):
        soup = get_response_soup(url)
        city_div = soup.select_one('div[style="padding:10px 15px 20px 15px"]')
        ul_list = city_div.select('ul')
        for ul in ul_list:
            first = ul.attrs.get('id')[-1:]
            with open(file_path + first.upper() + '.csv', 'w', encoding='GBK') as file:
                li_list = ul.select('li')

                for li in li_list:
                    a = li.select_one('a')
                    str2 = ''
                    if a.attrs['href'] is '#':
                        logger.warning('跳过#超链接，href为{}'.format(a.attrs['href']))
                        continue
                    str2 += a.attrs['href'] + ',' + a.string + '\n'
                    logger.debug('str2 is {}'.format(str2))
                    file.write(str2)


def get_city_month_url(path):
    # 爬取指定文件内的城市
    if os.path.isfile(path):
        check_city_url_csv(path)
    # 爬取指定文件夹
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            logger.info('{}, {}, {}'.format(root, dirs, files))
            for file in files:
                if fileutil.get_file_name(root + file, False)[1] != '.csv':
                    continue
                check_city_url_csv(root + file)
    else:
        logger.error('{} is error'.format(path))


def check_city_url_csv(path):
    '''解析单个csv文件'''
    all_time = []
    with open(path, 'r', encoding='gbk') as file:
        reader = csv.reader(file)
        for row in reader:
            soup = get_response_soup(row[0])
            city_start = time()
            file_path = 'matplot_data/city_url_month/' + fileutil.get_file_name(path, False)[0][-1:] + '/'
            fileutil.is_dir_live(file_path, True)

            # 存储历史天气路劲的文件名为 matplot_data/city_url_month/城市的首字母大写/城市中文名.csv
            file_path += row[1] + '.csv'
            select_label = soup.select_one('select[name=select]')
            # 截取onchange中的url
            url_month = strutil.split_str(select_label.attrs.get('onchange'), start='http://', end="';")
            options = select_label.select('option')
            with open(file_path, 'w') as result_file:
                for option in options:
                    strs = ''
                    # 跳过默认option选项
                    if not option.attrs['value']:
                        continue
                    month = option.attrs['value']
                    strs += url_month.replace("' + this.value + '", month) + ',' + option.string + '\n'
                    result_file.write(strs)
            # 读取一个城市后，睡眠2秒
            city_end = time()
            all_time.append(city_end - city_start)
            logger.info('{}数据爬取完毕，耗时{}，线程睡眠1秒'.format(row[1], city_end - city_start))
            sleep(1)
    sumtime = sum(all_time)
    avetime = sumtime / len(all_time)
    logger.info('爬取{}文件共耗时{}，平均耗时{} '.format(path, sumtime, avetime))


def plt_show():
    # 最高温
    highs = []
    # 最低温
    lows = []
    dates = []
    with open('matplot_data/wuhan_weather.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            highs.append(int(row[1]))
            lows.append(int(row[2]))
            dates.append(row[0][-2:])

    fig, ax = plt.subplots()
    ax.plot(dates, highs, color='red', label='最高温', marker='s')
    ax.plot(dates, lows, color='blue', label='最低温', marker='^')
    ax.set_xlabel('日期')
    ax.set_ylabel('气温')
    ax.set_title('武汉2017年7月气温走势图')
    ax.legend(loc='best')
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))
    fig.savefig('matplot/武汉2017年7月份气温走势图')
    plt.show()


def test_os():
    print(os.path.isfile('matplot_data/wuhan_weather2.csv'))


if __name__ == '__main__':
    # get_data(['http://lishi.tianqi.com/wuhan/201707.html'])
    # plt_show()
    # get_city_url('https://lishi.tianqi.com/')
    # test_os()
    get_city_month_url('matplot_data/city_url/')
