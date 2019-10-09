# 爬虫练习
import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
import matplotlib
import python.study.other.util.fileutil as fileutil
from python.study.other.config.logger import Logger

matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

header = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
          '(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
kv = {'user-agent': header}
logger = Logger().get_logger()


def get_data(urls):

    with open('matplot_data/wuhan_weather.csv', 'w') as file:
        for url in urls:
            # request = urllib.request.Request(url)
            response = requests.get(url, headers=kv)
            html = response.text
            html = html.encode('gbk')
            soup = BeautifulSoup(html, 'html.parser')
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
    file_path = 'matplot_data/citys_url_'
    if fileutil.is_live(file_path):
        response = requests.get(url, headers=kv)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        city_div = soup.select_one('div[style="padding:10px 15px 20px 15px"]')
        ul_list = city_div.select('ul')
        for ul in ul_list:
            first = ul.attrs.get('id')[-1:]
            with open(file_path + first.upper() + '.csv', 'w') as file:
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


if __name__ == '__main__':
    # get_data(['http://lishi.tianqi.com/wuhan/201707.html'])
    # plt_show()
    get_city_url('https://lishi.tianqi.com/')
