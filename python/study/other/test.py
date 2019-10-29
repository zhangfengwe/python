# test工具
# 使用unittest模块
# 单元测试方法可单独执行
# timeit测试方法效率， number代表执行多少次方法，默认为1000000
# repeat比timeit多了一个次数参数 timer代表重复执行次数，默认为3


import unittest
from python.study.practice.python02 import my_math
from timeit import timeit
from python.study.other.config.logger import Logger
from .util import fileutil
import re
import time
from time import  sleep


class ProductTest(unittest.TestCase):

    logger = Logger().get_logger()

    def test_add(self):
        self.logger.info('start test_add')
        print(my_math.add(13, '24'))
        self.logger.info('finish test_add')

    def test_add_time(self):
        print(timeit(stmt='my_math.add(a, b)', setup='from python.study.practice.python02 import my_math;a=2;b=3'))

    def test_re(self):
        print(re.match(r'(18|19|([23]\d))[0-9]{2}', '3900'))

    def test_str(self):
        str2 = "if (this.value != '') window.location.href='http://lishi.tianqi.com/zhurihe/' + this.value + '.html';"
        str2 = str2[str2.find('http://'):]
        print(str2)
        print(str2.rfind('\';'))
        print(str2.find('\';'))
        str2 = str2[:str2.rfind('\';')]
        print(str2)
        # strlist = str2.split('+')
        # print(strlist)
        # for str_sub in strlist:
        #     if str_sub.find('=') != -1:
        #         str_sub_list = str_sub.split('=')
        #         for str_sub_s in str_sub_list:
        #             print(str_sub_s.replace('\'', '').strip())

    def test_str2(self):
        print('111')
        st = 'http://lishi.tianqi.com/dabancheng/201808.html'
        print(st[st.find('com/'):st.rfind('/')])



    def test_logger_dayli(self):
        while True:
            self.logger.info('当前时间{}, 睡眠{}'.format(time.strftime('%Y%m%d', time.localtime()), 10000))
            sleep(10000)
            if time.strftime('%Y%m%d', time.localtime()) == '20190928':
                self.logger.info('当前时间{}'.format(time.strftime('%Y%m%d', time.localtime())))
                break


if __name__ == '__main__':
    # unittest.main()自动执行所有子类中以test开头的方法
    # 类似于java中junit
    # 进行单元测试
    unittest.main()
