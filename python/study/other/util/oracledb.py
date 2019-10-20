# python连接Oracle数据库
'''
    参数：可以是元组或字典
    元组，按照位置进行赋值，SQL中使用:1进行定位
    字典，按照名称进行赋值，SQL中使用:no进行定位（no为字典中的key）
'''

import cx_Oracle
import os
from python.study.other.config.readconfig import MyConfig
import traceback
from python.study.other.config.logger import Logger

# 设置Oracle字符编码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

logger = Logger().get_logger()


def con():
    # 设置SQL语句的参数风格
    # 参数格式有：format 即‘%s’标准字符串格式设置方式
    #            pyformat 扩展的格式编码
    #            qmark  使用问号
    #            numeric 使用:1的形式
    #            named 使用:no的形式
    try:
        user = MyConfig.get_value('database', 'user')
        password = MyConfig.get_value('database', 'password')
        server = MyConfig.get_value('database', 'host')
        port = MyConfig.get_value('database', 'port')
        dbname = MyConfig.get_value('database', 'dbname')
        cx_Oracle.paramstyle = 'numeric'
        # 使用tns连接
        oracle_tns = cx_Oracle.makedsn(server, int(port), dbname)
        conn = cx_Oracle.connect(user, password, oracle_tns)
        # 'xlink/942640@127.0.0.1:1521/HKXLINK'
        # conn = cx_Oracle.connect(user + '/' + password + '@' + server + ':' + port + '/' + dbname)
        curs = conn.cursor()
        logger.info('connect {} use {} is success'.format(dbname, user))
        return conn, curs
    except:
        logger.error(traceback.format_exc())


def select(curs, para=['', []]):
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
            curs.execute(sql, values)
        # fetchall() 取出所有数据
        # fetchone() 取出单条数据
        return curs.fetchall()


def insert(conn, curs, values=[], sql=''):
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
                    curs.executemany(sql, values)
                else:
                    curs.execute(sql, values)
                # 不提交,无法插入
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error(traceback.format_exc())


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
                logger.error(traceback.format_exc())


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
                logger.error(traceback.format_exc())


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
        try:
            for sql in sqls:
                curs.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            logger.error(traceback.format_exc())
            raise e
