# urllib模块

# import urllib
from urllib.request import urlopen
import python_file as fil


def open_url(url, file):
    data = urlopen(url)
    for line in data.readlines():
        fil.writeFile(file, line)


def main():
    open_url('http://www.baidu.com', 'test1.txt')

if __name__ == '__main__':
    main()