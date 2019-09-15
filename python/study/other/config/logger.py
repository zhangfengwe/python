# 日志打印

import logging.handlers
from python.study.other.config.readconfig import MyConfig

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


    filename = MyConfig.get_value('logger','log_file')
    level = levels.get(MyConfig.get_value('logger', 'log_level'))
    max_size = int(MyConfig.get_value('logger', 'log_max_size'))
    backup_count = int(MyConfig.get_value('logger', 'log_backup_count'))
    log_format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'

    @staticmethod
    def getLogger():
        if FinalLogger.logger is not None:
            return FinalLogger.logger
        FinalLogger.logger = logging.Logger('FinalLogger')
        log_handler = logging.handlers.RotatingFileHandler(filename=FinalLogger.filename, maxBytes=FinalLogger.max_size,
                                                         backupCount=FinalLogger.backup_count)
        log_handler.setFormatter(logging.Formatter(FinalLogger.log_format))
        FinalLogger.logger.addHandler(log_handler)
        FinalLogger.logger.setLevel(FinalLogger.level)

        return FinalLogger.logger

if __name__ == '__main__':
    logger = FinalLogger.getLogger()
    logger.info("the first python log--info")
    logger.debug('the first python log--debug')
    logger.warning('the first python log--warn')