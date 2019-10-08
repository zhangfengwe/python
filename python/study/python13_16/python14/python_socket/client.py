# Socket客户端

import socket

def client():
    s = socket.socket()
    try:
        host = '127.0.0.1'
        port = 12345
        # s.bind((host, port))
        s.connect((host, port))
        while True:
            content = input('请输入：')
            # print(content)
            if content == 'exit':
                break
            s.send(content.encode(encoding='gbk'))
            recv = s.recv(1024)
            print(recv.decode('gbk'))

    except Exception as e:
        print(e)
    finally:
        s.close()


def main():
    client()

if __name__ == '__main__':
    main()