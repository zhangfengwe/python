# 抽象
'''
    callable() 判断某个变量是否可以调用
    使用def 创建函数
    函数开头的字符串为文档字符串，会存储在函数中，通过_doc_属性
    函数默认返回为None,return 跳出函数
    参数存储在局部作用域内，函数内对参数值的改变不会影响函数外该值 ** 较为重要，单独累出学习
'''
import math

'''
测试自定义函数
'''
def test(world):
    #文档字符串
    '这是test函数的文档字符串'
    print('函数test的参数{}'.format(world))
x = 1
y = math.sqrt
print(callable(x))
print(callable(y))
print(test.__doc__)


