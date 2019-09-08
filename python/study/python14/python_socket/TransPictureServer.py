# 多线程Socket服务器
# 向客户端发送一张图片

from threading import Thread
from socket import socket
from json import dumps
from base64 import b64encode
from time import sleep

class TransPictureServer(Thread):

    def __init__(self, cclient):
        super().__init__()
        self._client = cclient

    def run(self):
        my_dict = {}
        my_dict['filename'] = self._client.recv(1024).decode('gbk')
        file = open(my_dict['filename'],'rb')
        data = b64encode(file.read()).decode('gbk')
        my_dict['filedata'] = data
        json_str = dumps(my_dict)
        self._client.send(json_str.encode('gbk'))
        sleep(10)
        print('睡眠10秒，模拟存在其他操作')
        self._client.close()


def main():

    server = socket()
    server.bind(('127.0.0.1', 9002))
    server.listen(512)
    print('服务器启动开始监听。。。。')


    while True:
        client, addr = server.accept()
        print(str(client) + '连接到了服务器')
        TransPictureServer(client).start()

if __name__ == '__main__':
    main()

