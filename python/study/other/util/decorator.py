# 装饰器

from functools import wraps
from time import time


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

