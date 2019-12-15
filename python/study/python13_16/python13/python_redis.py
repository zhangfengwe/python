# redis

import redis


def connect():
    try:
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1)
    except Exception:
        pass
    r = redis.Redis(connection_pool=pool)
    result1 = r.sadd('url', '111')
    result2 = r.sadd('url', '222')
    result3 = r.sadd('url', '111')
    result4 = r.sadd('url', '张三')
    print('{}  {}  {}  {}'.format(result1, result2, result3, result4))
    # pass


if __name__ == '__main__':
    connect()
