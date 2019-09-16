# test工具
# 使用unittest模块


import unittest
from python.study.practice.python02 import my_math


class ProductTest(unittest.TestCase):

    def test_add(self):
        print(my_math.add(13, '24'))

if __name__ == '__main__':
    # unittest.main()自动执行所有子类中以test开头的方法
    # 类似于java中junit
    # 进行单元测试
    unittest.main()
