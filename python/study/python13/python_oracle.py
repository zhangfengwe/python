# python连接Oracle数据库

import cx_Oracle

def con():
    conn = cx_Oracle.connect('xlink/xlink@127.0.0.1:1521/HKXLINK')
    curs = conn.cursor()
    return conn,curs

def select(curs,sql=''):
    if sql is '':
        raise ValueError('SQL语句不可为空')
    else:
        curs.execute(sql)
        # fetchall() 取出所有数据
        # fetchone() 取出单条数据
        return curs.fetchall()

def insert(conn,curs,value,sql=''):
    '''
    SQL插入，现在只能插入一条数据
    :param conn:
    :param curs:
    :param sql:
    :param value:
    :return:
    '''
    if sql is '':
        raise ValueError('SQL语句不能为空')
    else:
        # try:
            # print(list(value))
            curs.execute(sql,value)
            conn.commit()#不提交,无法插入
        # except Exception as e:
        #     # print(e)
        #     conn.rollback()

def main():
    try:
        conn,curs = con()
        # result = select(curs,'''''')
        # for line in result:
        #     print(result)
        insertSql = 'insert into respcode_map(respcode_transmit,channel_transmit,respcode,txstatus,message,flag)' \
                    'VALUES (%s,%s, %s, %s, %s, %s)'
        insert(conn,curs,('123','ESB','a','b','11','1'),insertSql)
    # except (ValueError,Exception) as e:
    #     print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
