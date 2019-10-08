# urllib模块

# import urllib
from urllib.request import urlopen
from urllib.request import urlretrieve
import python.study.python11.python_file as fil


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
    print(open_url('https://www.ivsky.com/bizhi/the_angry_birds_movie_v57732/pic_904679.html#al_tit', 'test3.html'))
    # print(open_urlretrieve('https://blog.csdn.net/u012232730/article/details/71078284', 'test3.html'))

if __name__ == '__main__':
    main()