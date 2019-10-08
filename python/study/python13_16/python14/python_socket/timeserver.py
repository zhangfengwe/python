# 时间服务器
# 访问返回时间

from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime


def time_server():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)

    server.bind(('127.0.0.1', 9000))

    # 512可以理解为连接队列的大小
    server.listen(512)
    print('服务器开始监听。。。。')
    while True:
        client, addr = server.accept()
        print(str(client) + '连接到了服务器')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()


def main():
    time_server()

if __name__ == '__main__':
    main()
