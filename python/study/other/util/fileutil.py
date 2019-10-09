# 常用文件工具方法

from os import path, makedirs


def is_live(file_name, create=False):
    '''
    判断文件目录是否存在
    :param file_name:
    :param create: 默认为False，为True时，创建不存在目录
    :return:
    '''
    file_path = path.dirname(file_name)
    if path.exists(file_path):
        return True
    elif create:
        makedirs(file_path)
        return True
    else:
        return False
