# Socket客户端，向服务端请求下在指定图片


from socket import socket
from base64 import b64decode
from json import loads
from os import path, makedirs

def main():
    filepath = input('请输入文件路径')
    filename = input('请输入文件名')
    client = socket()
    client.connect(('127.0.0.1',9002))
    client.send(filename.encode('gbk'))
    in_data = bytes()
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)

    my_dict = loads(in_data.decode('gbk'))
    filedata = my_dict['filedata'].encode('gbk')

    if not path.exists(filepath+'/'):
        makedirs(filepath+'/')

    with open(filepath+'/'+filename, 'wb') as f:
        f.write(b64decode(filedata))

    print('图片已保存')

if __name__ == '__main__':
    main()
