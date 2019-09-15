# python连接Oracle数据库
'''
    参数：可以是元组或字典
    元组，按照位置进行赋值，SQL中使用:1进行定位
    字典，按照名称进行赋值，SQL中使用:no进行定位（no为字典中的key）
'''

# import cx_Oracle
# import os
from python.study.python13 import *
from python.study.other.config.readconfig import MyConfig

# 设置Oracle字符编码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'


def con():
    # 设置SQL语句的参数风格
    # 参数格式有：format 即‘%s’标准字符串格式设置方式
    #            pyformat 扩展的格式编码
    #            qmark  使用问号
    #            numeric 使用:1的形式
    #            named 使用:no的形式
    user = MyConfig.get_value('database', 'user')
    password = MyConfig.get_value('database', 'password')
    server = MyConfig.get_value('database', 'host')
    port = MyConfig.get_value('database', 'port')
    dbname = MyConfig.get_value('database', 'dbname')
    cx_Oracle.paramstyle = 'numeric'
    # 使用tns连接
    oracle_tns = cx_Oracle.makedsn(server, int(port), dbname)
    conn = cx_Oracle.connect(user, password, oracle_tns)
    # conn = cx_Oracle.connect('xlink/942640@127.0.0.1:1521/HKXLINK')
    curs = conn.cursor()

    return conn, curs


def select(curs, para=['',[]]):
    '''
    查询
    :param curs:
    :param para: 元组，（SQL,(values)）
    :type para:tuple
    :return:
    '''
    sql, values = para
    if not sql:
        raise ValueError('SQL语句不可为空')
    else:
        if not values:
            curs.execute(sql)
        else:
            curs.execute(sql,values)
        # fetchall() 取出所有数据
        # fetchone() 取出单条数据
        return curs.fetchall()


def insert(conn, curs, values = [], sql=''):
    '''
    SQL插入，
    :param conn:
    :param curs:
    :param values:类型为列表，每条数据使用列表存放
    :type values:list
    :param sql:
    :return:
    '''
    if not sql:
        raise ValueError('SQL语句不能为空')
    else:
        if not values:
            raise ValueError('SQL value is error')
        else:
            try:
                if type(values[0]) is list:
                    curs.executemany(sql,values)
                else:
                    curs.execute(sql, values)
                conn.commit()#不提交,无法插入
            except Exception as e:
                conn.rollback()
                traceback.print_exc()


def update(conn, curs, value=[], sql=''):
    '''
    更新数据
    :param conn:
    :param curs:
    :param value:
    :type value:list
    :param sql:
    :return:
    '''
    if not sql:
        raise ValueError('SQL语句不能为空')
    else:
        if not value:
            raise ValueError('SQL value is error')
        else:
            try:
                curs.execute(sql, value)
                conn.commit()
            except Exception as e:
                conn.rollback()
                traceback.print_exc()


def delete(conn, curs, value=[], sql=''):
    '''
    :param conn:
    :param curs:
    :param value:
    :type value: list
    :param sql:
    :return:
    '''
    if not sql:
        raise ValueError('SQL语句不能为空')
    else:
        if not value:
            raise ValueError('SQL value is error')
        else:
            try:
                curs.execute(sql, value)
                conn.commit()
            except Exception as e:
                conn.rollback()
                traceback.print_exc()


def main():
    try:
        conn, curs = con()
        # 查询
        # result = select(curs,'''''')
        # for line in result:
        #     print(result)
        # 插入
        insert_sql = 'insert into respcode_map(respcode_transmit,channel_transmit,respcode,txstatus,message,flag)' \
                    'values(:1, :2, :3, :4, :5, :6)'
        values = []
        values.append(('123', 'ESB', 'a', 'b', '11', '1'))
        # values.append(('124', 'ESB', 'a', 'b', '11', '1'))
        insert(conn, curs, ['123', 'ESB', 'a', 'b', '11', '1'], insert_sql)
        # 修改
        # update_sql = 'update respcode_map set respcode = :1 WHERE respcode_transmit = :2'
        # rows = update(conn,curs,('错误', '123'),update_sql)
        # 删除
        # delete_sql = 'delete from respcode_map WHERE respcode_transmit = :1'
        # delete(conn,curs,('123',), delete_sql)
    except (ValueError,Exception) as e:
        traceback.print_exc()
    finally:
        conn.close()

if __name__ == '__main__':
    main()
