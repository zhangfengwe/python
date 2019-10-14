# urllib模块

# import urllib
from urllib.request import urlopen
from urllib.request import urlretrieve
import python.study.python10_12.python_file as fil


def open_url(url, file):
    data = urlopen(url)
    print(data)
    openconf = dict(mode='ab+', breflag='N')
    num = fil.writeFile(file, data, openconf)
    return num


def open_urlretrieve(url, file):
    result = urlretrieve(url, file)
    return result


def main():
    print(open_url('https://www.boquge.com/book/71607/', 'test3.html'))
    # print(open_urlretrieve('https://blog.csdn.net/u012232730/article/details/71078284', 'test3.html'))

if __name__ == '__main__':
    main()