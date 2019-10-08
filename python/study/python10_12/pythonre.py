# python正则表达式

import re
from python.study.other.config.logger import Logger
from python.study.other.util import reutil


def check_id(logger):
    logger.info('start repython')
    idno = input('please input your id number:')
    logger.info('ch result is {}'.format(reutil.split_id(idno)))


def check_phone(logger):
    logger.info('start repython')
    phone = input('please input your phone number:')
    if reutil.check_phone(phone):
        logger.info('check phone success')
    else:
        logger.info('check phone fail, the phone is {}'.format(phone))


def check_time(logger):
    logger.info('check date')
    if reutil.check_date('20000229'):
        logger.info('check succ')
    else:
        logger.info('check fail')


def main():
    # 获取日志
    logger = Logger().get_logger()
    check_id(logger)
    # check_time(logger)

if __name__ == '__main__':
    main()

