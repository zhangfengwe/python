# 循环语句
'''
    循环语句
        1、while 条件：
        2、for   in  可迭代对象：   类似于foreach,for循环可以使用序列解包
        range(start,end,step) 范围类
    并行迭代 zip方法，将两个序列缝合起来，返回一个由元组组成的序列，当两个序列的长度不同时，zip将在最短的序列用完后停止
    迭代时获取元素的索引，使用enumerate()，能够让你迭代索引-值对，索引自动提供
    反向迭代reversed(),返回可迭代对象，不改变原对象
    排序后迭代sorted(),返回一个列表，不修改原对象
    跳出循环：
        break，continue与java相同
    循环后增加一个else语句，仅在在break不调用的情况下执行
'''
num1 = []
num2 = []
num3 = [3,4,7,1,9]
for a in range(0,100,5):
    num1.append(a)
for a in range(0,100,10):
    num2.append(a)
print(num1,num2)
for key,value in zip(num1,num2):
    print('{} 是 {}的2倍'.format(value,key))
for index,value in enumerate(num1):
    if value % 10 == 0:
        print('{}值为{}'.format(index,value))
for num in sorted(num3):
    print(num)
num4 = []
for num in reversed(num1):
    num4.append(num)
print(num4)
flag = input('请输入一个整数： ')
for num in sorted(num3):
    if num > int(flag):
        break
    else:
        print(num / 2)
else:
    print('都小于{}'.format(flag))
