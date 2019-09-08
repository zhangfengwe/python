# 多线程，联网下载图片

from threading import Thread
import requests

class DownLoadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        filename = self._url[self._url.rfind('/')+1]
