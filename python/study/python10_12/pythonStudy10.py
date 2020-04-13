# 常用标准库

import sys
import fileinput as fli
# 堆模块
import heapq as head
from random import shuffle
from collections import deque
import time
import os
import json

from python.study.other.config.logger import Logger

logger = Logger().get_logger()


def sys_moudle():
    # 输出脚本路径及脚本名
    print(sys.argv)
    print(sys.platform)


# os模块主要是对操作系统进行操作
def os_moudle():
    logger.info('获取环境变量： os.environ: {}'.format(os.environ))
    logger.info('获取当前工作目录： os.getcwd(): {}'.format(os.getcwd()))
    logger.info('创建文件夹：os.mkdir(./test/), {}  创建多级文件夹： os.makedirs(./test1/a/b/c) {}'
                .format(os.mkdir('./test'), os.makedirs('./test1/a/b/c')))
    # 与创建文件夹相反
    logger.info('删除空文件夹： os.rmdir(./test),{}  递归删除多级空文件夹： os.removedirs(./test1/a/b/c) {}'
                .format(os.rmdir('./test'), os.removedirs('./test1/a/b/c')))
    logger.info('文件或文件夹重命名： os.rename(old, new)')
    logger.info('获取文件或文件夹信息： os.stat(.)  {}'.format(os.stat('.')))


def file_input_moudle():
    try:
        for line in fli.input(['./testfile/testfile_1', './testfile/testfile_2', './testfile/testfile_3']):
            print('{}文件内容 #{} {}'.format(fli.filename(), fli.filelineno(), line.rstrip()))
    except Exception as e:
        print(e)
    finally:
        # print(fli.filename())
        fli.close()


def set_moudle():
    se = set(range(10))
    print(se)
    set2 = set(range(5, 15))
    print(se.union(set2))
    print(se & set2)
    print(se.intersection(set2))
    se.add(frozenset(set(range(100, 117, 2))))
    print(se)


def head_moudle():
    # 堆
    hea = []
    data = list(range(10))
    # 随机排序列表
    shuffle(data)
    print(data)
    for n in data:
        head.heappush(hea, n)
    print(hea)
    print(head.heappop(hea))
    print(head.heappushpop(hea, 11))
    print(head.heapreplace(hea, 10))
    print(hea)


def quen_moudle():
    '''
    双端队列
    :return:
    '''
    q = deque(range(3, 17, 3))
    q.append(2)
    q.appendleft(1)
    print(q)
    q.extendleft(range(3))
    print(q)
    q.rotate(-2)
    print(q)
    '''向右旋转n步，n为负数时，向左旋转'''
    q.rotate(3)
    print(q)


def time_moudle():
    timestamp = time.time()
    logger.info('获取当前时间戳 time.time(), {}'.format(timestamp))
    struct_time = time.gmtime(timestamp)
    logger.info('时间戳转换为struct_time，time.localtime(): {}, time.gmtime(): {}'
                .format(time.localtime(timestamp), struct_time))
    logger.info('struct_time转换为时间戳， time.mktime(): {}'.format(time.mktime(struct_time)))
    format_time = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
    logger.info('struct_time转换为format_time, time.strftime(): {}'.format(format_time))
    # time.strptime()方法第二个参数为时间字符串的格式，需要赋值，默认使用%a %b %d %H:%M:%S %Y格式
    logger.info('format_time转换为struct_time， time.strptime(): {}'.format(time.strptime(format_time, '%Y-%m-%d %H:%M:%S')))
    logger.info('struct_time转换为%a %b %d %H:%M:%S %Y格式时间字符串, time.asctime(): {}'.format(time.asctime(struct_time)))
    logger.info('时间戳转换为%a %b %d %H:%M:%S %Y格式时间字符串, time.ctime(): {}'.format(time.ctime(timestamp)))


def json_moudle():
    # json.
    pass


def main():
    # sysMoudle()
    # fileinputMoudle()
    # setMoudle()
    head_moudle()
    # quenMoudle()
    # time_moudle()
    # osMoudle()


if __name__ == '__main__':
    main()
