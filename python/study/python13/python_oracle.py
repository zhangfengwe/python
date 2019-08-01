# python连接Oracle数据库

import cx_Oracle
from cx_Oracle import *

def con():
    conn = cx_Oracle.connect('test/TEST@192.168.1.2/test')
    curs = conn.cursor()
    print('sss')


def main():
    con()

if __name__ == '__main__':
    main()
