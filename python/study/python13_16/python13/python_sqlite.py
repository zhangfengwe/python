# SQLite python自带小型数据库引擎

from python.study.python13_16.python13 import sqlite3


def con():

    sqlite3.paramstyle = 'numeric'
    conn = sqlite3.connect('sqlite_test.db')
    curs = conn.cursor()

    return conn, curs


def create_table(conn, curs, sqls=[]):
    '''
    创建表格，可同时执行多条建表语句，多条建表语句存放在列表中
    :param conn:
    :param curs:
    :param sqls:
    :return:
    '''
    if len(sqls) == 0:
        raise ValueError('SQL is null')
    else:
        for sql in sqls:
            curs.execute(sql)
        conn.commit()


def insert_table(conn, curs, sqls=[]):
    '''
    插入
    :param conn:
    :param curs:
    :param sqls: 列表每一项为一个元组，第一个元素为SQL，第二个元素为值
    :return:
    '''
    if len(sqls) == 0:
        raise ValueError('SQL is null')
    else:
        for sql, value in sqls:
            # print(sql)
            # print(value)
            curs.executemany(sql, value)
        conn.commit()


def select(curs, sql=''):
    if sql is '':
        raise ValueError('SQL is null')
    else:
        curs.execute(sql)
        return curs.fetchall()


def main():
    conn, curs = con()
    # create_table(conn, curs, ['CREATE TABLE test_table_2 ( id TEXT PRIMARY KEY, desc TEXT)'])
    insert_sqls = []
    insert_sql_1 = 'insert into test_table VALUES (:1, :2)'
    insert_value_1 = ('3', '一')
    insert_value_2 = ('4', '二')
    insert_values = []
    insert_values.append(insert_value_1)
    insert_values.append(insert_value_2)
    insert_sqls.append((insert_sql_1, insert_values))
    # insert_sqls.append((insert_sql_1, insert_value_2))
    insert_table(conn, curs, insert_sqls)
    result = select(curs, 'select * from test_table')
    for line in result:
        print(line)

if __name__ == '__main__':
    main()
