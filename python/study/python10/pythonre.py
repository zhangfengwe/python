# python正则表达式

import re
from python.study.other.config.logger import FinalLogger
from python.study.other.util import reutil

def main():
    # 获取日志
    logger = FinalLogger.getLogger()
    logger.info('start repython')
    phone = input('please input your phone number:')
    if reutil.check_phone(phone):
        logger.info('check phone success')
    else:
        logger.info('check phone fail, the phone is {}'.format(phone))

if __name__ == '__main__':
    main()

