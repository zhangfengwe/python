# 抽象
'''
    callable() 判断某个变量是否可以调用
    使用def 创建函数
    函数开头的字符串为文档字符串，会存储在函数中，通过_doc_属性
    函数默认返回为None,return 跳出函数
    参数存储在局部作用域内，函数内对参数值的改变不会影响函数外该值 ** 较为重要，单独累出学习
    关键字参数，可以忽略参数位置，同时可以对参数设置默认值
    收集参数，可以定义函数一个参数可以传入多个值，类似于Java中的...,python中使用* 定义,带星号的参数可以放在其他位置，
        不一定是要在最后，但是后面的参数要使用名称来进行参数赋值
        * 不会收集关键字参数，得到一个元组
        收集关键字参数使用**，得到一个以关键字为key的字段
'''
import math

'''
测试自定义函数
'''


def test(world):
    # 文档字符串
    '''这是test函数的文档字符串'''
    print('函数test的参数{}'.format(world))


def test2(*world, str2=''):
    print(world)
    print(str2)


def test3(world, name='fwzhang'):
    # 关键字参数测试函数
    print('{},{}'.format(world, name))


x = 1
y = math.sqrt
print(callable(x))
print(callable(y))
print(test.__doc__)
print(test2.__name__)
test2('fwzhang', 'zhangfengwei', 'zhangsan', str2='942640')
test3(name='zhangfengwei', world='hello')
test3(world='hi')
