# 测试使用

from python.study.other.config.logger import Logger


def add(a, b):
    return int(a)+int(b)


if __name__ == '__main__':
    logger = Logger().get_logger()
    logger.info('add start')
    logger.info('result is {}'.format(add(23, 41)))
    logger.info('add finish')

