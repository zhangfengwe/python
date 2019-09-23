# 单例模式的logger

import logging.handlers
import logging.config
from os import path, makedirs
from python.study.other.config.readconfig import MyConfig


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


@singleton
class Logger():

    levels = {
        'notset': logging.NOTSET,
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warn': logging.WARN,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self):

        self.filename = MyConfig.get_value('logger', 'log_file')
        # 根据完整文件路径获取文件目录
        # path.dirname 获取文件目录
        # path.basename 获取文件名
        file_path = path.dirname(self.filename)
        if not path.exists(file_path):
            makedirs(file_path)
        self.level = self.levels.get(MyConfig.get_value('logger', 'log_level'))
        self.max_size = int(MyConfig.get_value('logger', 'log_max_size'))
        self.backup_count = int(MyConfig.get_value('logger', 'log_backup_count'))
        self.log_format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: <%(message)s>'

    def get_logger(self):
        logger = logging.Logger('FinalLogger')
        log_handler = logging.handlers.TimedRotatingFileHandler(filename=self.filename, when='D',backupCount=self.backup_count)
        log_handler.setFormatter(logging.Formatter(self.log_format))
        logger.addHandler(log_handler)
        logger.setLevel(self.level)

        return logger

if __name__ == '__main__':
    logger = Logger().get_logger()
    logger.info('test logger')