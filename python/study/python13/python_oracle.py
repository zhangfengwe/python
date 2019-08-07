# python连接Oracle数据库
'''
    参数：可以是元组或字典
    元组，按照位置进行赋值，SQL中使用:1进行定位
    字典，按照名称进行赋值，SQL中使用:no进行定位（no为字典中的key）
'''

# import cx_Oracle
# import os
from python.study.python13 import *

# 设置Oracle字符编码
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.ZHS16GBK'


def con():
    cx_Oracle.paramstyle = 'numeric'
    conn = cx_Oracle.connect('xlink/xlink@127.0.0.1:1521/HKXLINK')
    curs = conn.cursor()

    return conn, curs


def select(curs, sql=''):
    if sql is '':
        raise ValueError('SQL语句不可为空')
    else:
        curs.execute(sql)
        # fetchall() 取出所有数据
        # fetchone() 取出单条数据
        return curs.fetchall()


def insert(conn, curs, value, sql=''):
    '''
    SQL插入，现在只能插入一条数据
    :param conn:
    :param curs:
    :param value:
    :param sql:
    :return:
    '''
    if sql is '':
        raise ValueError('SQL语句不能为空')
    else:
        rows = curs.execute(sql, value)
        conn.commit()#不提交,无法插入
        return rows


def update(conn, curs, value, sql=''):
    '''
    更新数据
    :param conn:
    :param curs:
    :param value:
    :param sql:
    :return:
    '''
    if sql is '':
        raise ValueError('SQL语句不能为空')
    else:
        rows = curs.execute(sql, value)
        conn.commit()
        return rows


def delete(conn, curs, value, sql=''):
    if sql is '':
        raise ValueError('SQL语句不能为空')
    else:
        rows = curs.execute(sql, value)
        conn.commit()
        return rows


def main():
    try:
        print(cx_Oracle.paramstyle)
        conn, curs = con()
        # result = select(curs,'''''')
        # for line in result:
        #     print(result)
        insert_sql = 'insert into respcode_map(respcode_transmit,channel_transmit,respcode,txstatus,message,flag)' \
                    'values(:1, :2, :3, :4, :5, :6)'
        insert(conn, curs, ('123', 'ESB', 'a', 'b', '11', '1'), insert_sql)
    except (ValueError,Exception) as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    main()
