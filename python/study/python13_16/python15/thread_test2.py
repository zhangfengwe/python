# python多线程
# 继承Thread类

from threading import Thread
from os import getpid
from random import randint
from time import time, sleep


class DownLoadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    def run(self):
        print('启动下载进程，进程号[{:d}]'.format(getpid()))
        print('开始下载{}'.format(self.filename))
        time_of_download = randint(5, 10)
        sleep(time_of_download)
        print('{0}下载完成！共耗费了{1:d}秒'.format(self.filename, time_of_download))


def main():
    start = time()
    task1 = DownLoadTask('python_100_days.pdf')
    task2 = DownLoadTask('python从入门到入土.pdf')
    task1.start()
    task2.start()
    task1.join()
    task2.join()
    end = time()
    print('共耗时{:.2f}'.format(end-start))


if __name__ == '__main__':
    main()