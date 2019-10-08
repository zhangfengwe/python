# 异常

from python.study.python08.MySelfException import MyException
'''
raise 引发异常
try/except 捕获异常
'''


def div(a, b):
    return a / b

try:
    # print('执行体')
    a = int(input('被除数:'))
    b = int(input('除数:'))
    print(div(a,b))
# 捕获多个异常
except (MyException,TypeError,ZeroDivisionError) as e:
    # print('get Exception name is {}'.format(MyException.__name__))
    print(e)
else:
    # 没有捕获异常时执行
    print('No Exception')
finally:
    # 最终执行
    print('End')
