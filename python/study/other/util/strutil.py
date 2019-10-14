# 字符串相关工具类


def split_str(old_str, start, end, startflag=True):
    '''
    根据开始，结束标志截取字符串
    :param old_str:
    :param start: 开始标志
    :param end: 结束标志
    :param startflag: 包含开始标志
    :return:
    '''
    if old_str.find(start) != -1 and old_str.find(end) != -1:
        if startflag:
            old_str = old_str[old_str.find(start):]
        else:
            old_str = old_str[old_str.find(start) + len(start):]
        new_str = old_str[:old_str.rfind(end)]
        return new_str
    else:
        raise ValueError('args are not in str')
