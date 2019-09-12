# 多线程，联网下载图片

from threading import Thread
import requests
from os import path, makedirs


class DownLoadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        filename = self._url[self._url.rfind('/')+1]
        resp = requests.get(self._url)
        if not path.exists('1/'):
            makedirs('1/')
        with open('1/'+filename, 'wb') as file:
            file.write(resp.content)


def main():
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=5b34c011e6fce3b19dac3e7d257fc828&num=10')
    data_modle = resp.json()
    for my_dict in data_modle['newslist']:
        url = my_dict['picUrl']
        DownLoadHandler(url=url).start()


if __name__ == '__main__':
    main()