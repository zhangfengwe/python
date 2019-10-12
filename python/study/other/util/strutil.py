# 字符串相关工具类


def split_str(old_str, start, end):
    '''
    根据开始，结束标志截取字符串
    :param old_str:
    :param start: 开始标志
    :param end: 结束标志
    :return:
    '''
    if old_str.find(start) != -1 and old_str.find(end) != -1:
        new_str = old_str[old_str.find(start):]
        new_str = new_str[:new_str.rfind(end)]
        return new_str
    else:
        raise ValueError('args are not in str')
