# 常用正则表达式工具方法

from python.study.other.config import reconfig,logger
import re
import traceback
import time

loger = logger.Logger().get_logger()

area = {"11": "北京", "12": "天津", "13": "河北", "14": "山西", "15": "内蒙古", "21": "辽宁", "22": "吉林", "23": "黑龙江", "31": "上海",
        "32": "江苏", "33": "浙江", "34": "安徽", "35": "福建", "36": "江西", "37": "山东", "41": "河南", "42": "湖北", "43": "湖南",
        "44": "广东", "45": "广西", "46": "海南", "50": "重庆", "51": "四川", "52": "贵州", "53": "云南", "54": "西藏", "61": "陕西",
        "62": "甘肃", "63": "青海", "64": "宁夏", "65": "新疆", "71": "台湾", "81": "香港", "82": "澳门", "91": "国外"}


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


def check_id_no(idNo):
    '''
    检查身份证号是否合法
    :param id:
    :type str
    :return:
    :rtype:bool
    '''
    loger.info('load id:{}'.format(idNo))
    try:
        loger.info('id length is {}'.format(len(idNo)))
        match_result = re.match(reconfig.ID_COM, idNo)
        if match_result:
            return True
        else:
            return False
    except Exception:
        loger.error(traceback.format_exc())
        return False


def split_id(idNo):
    '''
    首先验证证件号格式是否合法
    然后拆分证件号，并做相应逻辑判断
    最后返回结果字典
    :param idNo:
    :return:result_dict
    :rtype:dict
    '''
    try:
        if check_id_no(idNo):
            # split_result = {}
            # 拆分身份证号
            if len(idNo) == 18:
                # 正则表达式带有注释，search方法需要使用re.X模式
                split_result = re.search(reconfig.ID_18_COM_X, idNo, flags=re.X).groupdict()
            else:
                split_result = re.search(reconfig.ID_15_COM_X, idNo, flags=re.X).groupdict()
            loger.info('split id result is {}'.format(split_result))
            # 判断出生日期和省份
            # 后期可优化为判断省市县
            if check_date(split_result.get('birthday')) and split_result.get('province') in area:
                split_result['result'] = True
                return split_result
            else:
                return dict(result=False)
        else:
            return dict(result=False)
    except Exception:
        loger.error(traceback.format_exc())
        return dict(result=False)


def check_date(date):
    '''
    检查日期是否合法
    :param date:YYYYMMDD/19YYMMDD
    :return:
    '''
    try:
        if len(date) == 6:
            date = '19' + date
        time.strptime(date, '%Y%m%d')
        return True
    except ValueError:
        return False
