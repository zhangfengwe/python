# 单例模式的logger

import logging.handlers
import logging.config
from datetime import datetime
from os import path, makedirs, name
from python.study.other.config.readconfig import MyConfig
from python.study.other.util.decorator import singleton


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

        today = datetime.now()
        base_path = MyConfig.get_value('path', 'win_base_path')
        if name is 'posix':
            base_path = MyConfig.get_value('path', 'linux_base_path')
        self.filename = base_path + MyConfig.get_value('logger', 'log_file').format(today.year, today.month, today.day)
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
        # MIDNIGHT每天凌晨切换文件
        """
        由于TimedRotatingFileHandler日志不能有效按天轮转，且问题原因不明
        修改为使用按文件大小切换方式，按日轮转通过文件名来实现
        日志按照大小轮转时，仍然会报“PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。”
        """
        log_handler = logging.handlers.RotatingFileHandler(filename=self.filename,
                                                           maxBytes=self.max_size, backupCount=self.backup_count)
        log_handler.setFormatter(logging.Formatter(self.log_format))
        logger.addHandler(log_handler)
        logger.setLevel(self.level)

        return logger


if __name__ == '__main__':
    logger = Logger().get_logger()
    logger.info('test logger')
