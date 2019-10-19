# 常用文件工具方法

from os import path, makedirs, walk
from python.study.other.config.logger import Logger

logger = Logger().get_logger()


def is_dir_live(filename, create=False):
    '''
    判断文件目录是否存在
    :param filename:
    :param create: 默认为False，为True时，创建不存在目录
    :return:
    '''
    file_path = path.dirname(filename)
    if path.exists(file_path):
        return True
    elif create:
        logger.info('路径{}'.format(file_path))
        makedirs(file_path)
        return True
    else:
        return False


def get_file_name(filepath, endflag=True):
    '''
    获取文件名
    :param filepath: 文件路径
    :param endflag: 是否返回整个文件名，默认为返回整个
    :return: 文件不存在，返回
    '''
    if path.isfile(filepath):
        basename = path.basename(filepath)
        if endflag:
            return basename
        else:
            return path.splitext(basename)
    else:
        logger.error('{} is not exists'.format(filepath))
        return False


def get_all_file(rootpath):
    '''
    获取目录下所有文件(包括子目录)
    :param rootpath:
    :return:
    '''
    allfiles = []
    if path.exists(rootpath):
        for root, dirs, files in walk(rootpath):
            for file in files:
                allfiles.append(path.join(root, file))
            for subdir in dirs:
                get_all_file(path.join(root, subdir))
        return allfiles
    else:
        logger.error('{} is not a legal path'.format(rootpath))

