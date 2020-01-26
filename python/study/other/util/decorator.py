# 装饰器

from functools import wraps
from time import time
import traceback


def timit(logger):
    '''
    计算函数运行耗时装饰器,日志打印输出
    :param logger:
    :return:
    '''
    def timit_decorator(func):
        @wraps(func)
        def cost(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            end = time()
            logger.info('{} cost {}'.format(func.__name__, end - start))
            return result
        return cost
    return timit_decorator


def errlog(logger):
    '''
    打印Exception信息
    :param logger:
    :return:
    '''
    def errlog_decorator(func):
        @wraps(func)
        def logerr(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(traceback.format_exc())
                raise e
        return logerr
    return errlog_decorator


def singleton(cls):
    '''
    单例模式的装饰器函数
    :param cls:
    :return:
    '''
    instances = {}

    def getInstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getInstance
