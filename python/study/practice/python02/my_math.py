# 测试使用

from python.study.other.config.logger import Logger
from python.study.other.util.decorator import timit
from time import sleep

logger = Logger().get_logger()


@timit(logger)
def add(a, b):
    sleep(2)
    return int(a)+int(b)


if __name__ == '__main__':
    print(add(3, 4))
    # logger = Logger().get_logger()
    # logger.info('add start')
    # logger.info('result is {}'.format(add(23, 41)))
    # logger.info('add finish')

