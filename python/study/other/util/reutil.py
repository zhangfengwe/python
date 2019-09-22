# 常用正则表达式工具方法

from python.study.other.config import reconfig,logger
import re
import traceback

loger = logger.FinalLogger.getLogger()

def check_phone(phone):
    '''
    检查手机号是否合法
    :param phone:
    :return:
    '''
    loger.info('load phone:{}'.format(phone))
    try:
        if re.match(reconfig.PHONE_COM, phone):
            return True
        else:
            return False
    except Exception:
        loger.error(traceback.format_exc())
        return False