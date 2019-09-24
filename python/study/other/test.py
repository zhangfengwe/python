# test工具
# 使用unittest模块
# 单元测试方法可单独执行
# timeit测试方法效率， number代表执行多少次方法，默认为1000000
# repeat比timeit多了一个次数参数 timer代表重复执行次数，默认为3


import unittest
from python.study.practice.python02 import my_math
from timeit import timeit
from python.study.other.config.logger import Logger


class ProductTest(unittest.TestCase):

    logger = Logger().get_logger()

    def test_add(self):
        self.logger.info('start test_add')
        print(my_math.add(13, '24'))
        self.logger.info('finish test_add')

    def test_add_time(self):
        print(timeit(stmt='my_math.add(a, b)', setup='from python.study.practice.python02 import my_math;a=2;b=3'))

if __name__ == '__main__':
    # unittest.main()自动执行所有子类中以test开头的方法
    # 类似于java中junit
    # 进行单元测试
    unittest.main()
