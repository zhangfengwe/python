# 测试使用

from python.study.other.config.logger import Logger as log
from python.study.other.util.decorator import timit
from python.study.other.util import fileutil
from time import sleep
import logging

from functools import wraps
import traceback

logger = log().get_logger()


@timit(logger)
def add(a, b):
    sleep(2)
    return int(a) + int(b)


@timit(logger)
# @errlog(logger)
def sub(a, b):
    sleep(1)
    print(fileutil.get_file_dir('D://python//善心\\'))
    # return a / b


def errlog(func):
    '''
    打印Exception信息
    :param logger:
    :return:
    '''
    # def errlog_decorator(func):
    @wraps(func)
    def logerr(*args, **kwargs):
        for arg in args:
            if isinstance(arg, logging.Logger):
                logger = arg
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(traceback.format_exc())
            # raise e
    return logerr
    # return errlog_decorator


@errlog
def ts(a, logger):
    print(a)
    raise KeyError('参数错误')


if __name__ == '__main__':
    # print(add(3, 4))
    # sub(3, 4)
    # citys = []
    # city = "{:0>6}".format(str(len(citys) + 1))
    # print(city)
    # print(sub(5, 2))
    # logger = Logger().get_logger()
    # logger.info('add start')
    # logger.info('result is {}'.format(add(23, 41)))
    # logger.info('add finish')
    # st = 'http://lishi.tianqi.com/dabancheng/201808.html'
    # print(st[st.find('com/') + 4:st.rfind('/')])

    ts(1, logger)
