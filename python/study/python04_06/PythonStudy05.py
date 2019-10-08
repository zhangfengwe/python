#
'''
    序列解包（可迭代对象解包）：将一个序列（可迭代对象）解包，将获取的值存储到一系列变量中
    链式赋值，从后往前
    pass 语句，表示作为占位符
    del 删除对象
    exec(代码字符串，命名空间) 将字符串作为代码执行，什么都不返回
    eval(代码字符串，命名空间) 类似于exec的内置函数 计算用字符串表示的python表达式的值，并返回结果
'''
'''
序列解包,序列中元素个数和变量个数必须相同，不相同时可以使用*号运算符收集多余的元素，带*号的变量的类型为列表
'''
x, y, z, *m = list('123456789')
print(x, y, z, m)
'''
链式赋值
'''
x = y = 3
print(x, y)

if x == 3:
    pass
else:
    print(x)
del y
# print(y)
exec("print(x)")
scope = {}
exec("x=9\nprint(x)\nz=1", scope)
print(scope.keys())
print(scope['z'])
exec('x*z', scope)
print(scope.keys())
