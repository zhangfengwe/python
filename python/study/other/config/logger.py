# 日志打印

import logging.handlers
# from python.study.other.config.readconfig import MyConfig
from os import path, makedirs
import configparser


class FinalLogger:

    logger = None
    levels = {
        'notset': logging.NOTSET,
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warn': logging.WARN,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }
    MyConfig = configparser.ConfigParser()
    MyConfig.read('config.ini')
    filename = '/log/Python_Study.log'
    # filename = MyConfig.get('logger', 'log_file')
    # 根据完整文件路径获取文件目录
    # path.dirname 获取文件目录
    # path.basename 获取文件名
    file_path = path.dirname(filename)
    if not path.exists(file_path):
        makedirs(file_path)
    # level = levels.get(MyConfig.get('logger', 'log_level'))
    # max_size = int(MyConfig.get('logger', 'log_max_size'))
    # backup_count = int(MyConfig.get('logger', 'log_backup_count'))
    log_format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: <%(message)s>'

    @staticmethod
    def getLogger():
        if FinalLogger.logger is not None:
            return FinalLogger.logger
        FinalLogger.logger = logging.Logger('FinalLogger')
        log_handler = logging.handlers.TimedRotatingFileHandler(filename=FinalLogger.filename,
                                                         backupCount= 5, when='D')
        log_handler.setFormatter(logging.Formatter(FinalLogger.log_format))
        FinalLogger.logger.addHandler(log_handler)
        FinalLogger.logger.setLevel(FinalLogger.levels.get('info'))

        return FinalLogger.logger

if __name__ == '__main__':
    logger = FinalLogger.getLogger()
    logger.info("the first python log--info")
    logger.debug('the first python log--debug')
    logger.warning('the first python log--warn')