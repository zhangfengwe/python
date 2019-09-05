# python线程
# 使用threading模块

from threading import Thread
from python.study.python15.process import down_file
from time import time


def main():
    start = time()
    t1 = Thread(target=down_file, args=('python_100_days.pdf',))
    t1.start()
    t2 = Thread(target=down_file, args=('python从入门到入土.pdf',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('共耗时{:.2f}秒'.format(end-start))

if __name__ == '__main__':
    main()
