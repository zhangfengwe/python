# 文件操作

import traceback


def readFile(file, lenth):
    '''
    读取指定长度的文件内容，长度为0时代表读取全部
    :param file:
    :param lenth:
    :return:
    '''
    li = []
    try:
        with open(file, encoding='utf-8') as f:
            if len == 0:
                li = f.readlines()
            else:
                li.append(f.read(lenth))
    except Exception as e:
        traceback.print_exc()
    finally:
        return li


def writeFile(file, content, openconf={'mode': 'a+', 'encoding': None, 'breflag': 'Y'}):
    '''
    将文件内容写入文件中
    :param file:
    :param content:
    :param openconf:存放打开文件参数
                {mode:'a+',encoding:'utf-8'}
    :type openconf:dict
    :return:
    '''
    num = 0
    try:
        with open(file, openconf.get('mode'), encoding=openconf.get('encoding')) as f:
            for line in content:
                num += f.write(line)
                if openconf.get('breflag') == 'Y':
                    num += f.write('\n')
            return num
    except Exception as e:
        traceback.print_exc()
        return -1


def iterFile(file):
    try:
        for line in open(file, encoding='utf-8'):
            print(line.strip())
    except Exception as e:
        print(e)


def main():
    file = '../python10_12/testfile/testfile_2'
    li = readFile(file, 0)
    for i in range(len(li)):
        print(li[i].strip())
    content = ['hello,李四,python', 'the python file test', 'and file write']
    print(writeFile(file, content, 'a'))

    iterFile(file)

if __name__ == '__main__':
    main()

