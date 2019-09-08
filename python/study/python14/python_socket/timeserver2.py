# 实现多线程时间服务器

from threading import Thread
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


class TimeServer(Thread):

    def __init__(self, client, addr):
        '''
        :param client:
        :param addr:
        '''
        super().__init__()
        self._client = client
        self._addr = addr



    # @staticmethod
    # def create_server(self):
    #
    #     self.server.bind(('127.0.0.1', 9001))
    #     self.server.listen(512)

    def run(self):

        print(str(self._client) + '连接到了服务器')
        self._client.send(str(datetime.now()).encode('utf-8'))
        # client.close()

def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.1', 9001))
    server.listen(512)
    client, addr = server.accept()
    time_server = TimeServer(client, addr)

    while True:
        time_server.start()

if __name__ == '__main__':
    main()
