# 文件操作

def readFile(file,len):
    '''
    读取指定长度的文件内容，长度为0时代表读取全部
    :param file:
    :param len:
    :return:
    '''
    li = []
    try:
        with open(file,encoding='utf-8') as f:
            if len == 0:
                li = f.readlines()
            else:
                li.append(f.read(len))
    except Exception as e:
        print(e)
    finally:
        return li

def writeFile(file,content):
    '''
    将文件内容写入文件中
    :param file:
    :param content:
    :return:
    '''
    num = 0
    try:
        with open(file,'w',encoding='utf-8') as f:
            for line in content:
                num += f.write(line)
                num += f.write('\n')
            return num
    except Exception as e:
        return -1

def iterFile(file):
    try:
        for line in open(file,encoding='utf-8'):
            print(line.strip())
    except Exception as e:
        print(e)


def main():
    file = '../python10/testfile/testfile_2'
    li = readFile(file,0)
    for i in range(len(li)):
        print(li[i].strip())
    content = ['hello,李四,python','the python file test','and file write']
    print(writeFile(file,content))

    iterFile(file)

if __name__ == '__main__':
    main()

