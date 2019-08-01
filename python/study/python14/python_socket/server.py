# Socket 服务端

import socket

def server():
    s = socket.socket()
    host = '127.0.0.1'
    port = 12345
    s.bind((host,port))
    s.listen(5)
    try:
        c, addr = s.accept()
        while True:

            # print('get connection from {}'.format(addr))
            recv = c.recv(1024)
            print(recv.decode('gbk'))
            c.send('thank you for connect'.encode(encoding='gbk'))
            # c.close()
    except Exception as e:
        print(e)
    finally:
        # c.close()
        s.close()


def main():
    server()

if __name__ == '__main__':
    main()