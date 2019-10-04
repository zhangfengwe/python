

from timeit import timeit
from python.study.other.config.logger import Logger
import re
import time
from time import  sleep

def main():
    logger = Logger().get_logger()
    while True:
        logger.info('当前时间{}, 睡眠{}'.format(time.strftime('%Y%m%d', time.localtime()), 10))
        sleep(10)
        if time.strftime('%Y%m%d', time.localtime()) == '20190928':
            logger.info('当前时间{}'.format(time.strftime('%Y%m%d', time.localtime())))
            break

if __name__ == '__main__':
    main()