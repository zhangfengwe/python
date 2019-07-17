# 常用标准库

import sys
import fileinput as fli
#堆模块
import heapq as head
from random import shuffle
from collections import deque
import time
import json

def sysMoudle():
    # 输出脚本路径及脚本名
    print(sys.argv)
    print(sys.platform)

def osMoudle():
    pass

def fileinputMoudle():
    try:
        for line in fli.input(['./testfile/testfile_1','./testfile/testfile_2','./testfile/testfile_3']):
            print('{}文件内容 #{} {}'.format(fli.filename(),fli.filelineno(),line.rstrip()))
    except Exception as e:
        print(e)
    finally:
    # print(fli.filename())
        fli.close()

def setMoudle():
    se = set(range(10))
    print(se)
    set2 = set(range(5,15))
    print(se.union(set2))
    print(se & set2)
    print(se.intersection(set2))
    se.add(frozenset(set(range(100,117,2))))
    print(se)

def headMoudle():
    hea = []
    data = list(range(10))
    #随机排序列表
    shuffle(data)
    print(data)
    for n in data:
        head.heappush(hea,n)
    print(hea)
    print(head.heappop(hea))
    print(head.heappushpop(hea,11))
    print(head.heapreplace(hea,10))
    print(hea)

def quenMoudle():
    '''
    双端队列
    :return:
    '''
    q = deque(range(3,17,3))
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

def timeMoudle():
    tup_time = time.localtime(time.time())
    print('{}年{}月{}日 {}时{}分{}秒'.format(tup_time[0],tup_time[1],tup_time[2],tup_time[3],tup_time[4],tup_time[5]))
    print(time.asctime())
    print(time.mktime(tup_time))
    print(time.strftime('%Y-%m-%d %H:%M:%S',tup_time))
    print(time.strptime(time.asctime()))

def jsonMoudle():
    # json.
    pass

def main():
    # sysMoudle()
    # fileinputMoudle()
    #setMoudle()
    # headMoudle()
    # quenMoudle()
    timeMoudle()

if __name__ == '__main__':
    main()