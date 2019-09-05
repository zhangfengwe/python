# python进程

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def down_file(filename):

    print('启动下载进程，进程号[{:d}]'.format(getpid()))
    print('开始下载{}'.format(filename))
    time_of_download = randint(5, 10)
    sleep(time_of_download)
    print('{0}下载完成！共耗费了{1:d}秒'.format(filename, time_of_download))


def main():
    start = time()
    # args类型为元组
    p1 = Process(target=down_file, args=('python_100_days.pdf',))
    p1.start()

    p2 = Process(target=down_file, args=('python入门到实践.pdf',))
    p2.start()

    p1.join()
    p2.join()
    end = time()
    print('共耗时{:.2f}秒'.format(end-start))

if __name__ == '__main__':
    main()