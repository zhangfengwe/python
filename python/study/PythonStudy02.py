#序列
'''
    1、元组
        a、不可修改
    2、列表
        a、可修改
        基础列表操作：
            1、根据索引修改列表
            2、删除列表元素 del
            3、切边赋值，可以同时给多个元素赋值，通过切片赋值，可以将切片替换为与其长度不同的序列
    序列索引：
        从左向右，0-n
        从右向左，-n-0
    截取：
        [start:end:step] 包前不包后[开始索引:结束索引:步长（默认为1）]
        截取始于开头可简写为 [:end]
        截取始于末尾可简写为 [start:]
        复制序列 [:]
        步长不可为0，可为负数，从右向左
    序列相加
        使用加法拼接序列
    序列相乘
        序列 * x 将重复x次的序列拼接为一个序列
    创建长度为10的空列表
        [None] * 10
    检查特定的值是否在序列中
        特定值 in 序列
    内置函数：
        len() 序列长度
        max() 序列最大值
        min() 序列最小值
        list(字符串) 将字符串转换为对应列表
    列表方法
        append()追加，修改原序列
        clear()清空列表内容
        copy()复制列表，使用=复制，只是将b关联到a的副本，copy()则创建新的列表
        count()计算指定的元素在列表中出现的次数
        extend()将多个值同时添加到列表末尾，就地修改,直接打印，输出None，无返回值
        index()查找指定值第一次出现的索引
        insert(索引,对象)将对象插入列表中   直接输出 输出None ??
        pop(index)删除列表中的一个元素，并返回该元素，参数为空时，默认为最后一个元素
        remove()删除第一个为指定值的元素
        sort()就地排序，无返回值
            为达到原序列不变，获取排序后的序列
            1、y=x.copy()
               sort(y)
            2、y=sorted(x)
        sort()存在两个可选参数，key和reverse(True和False)

        append(),remove(),insert(),extend(),reverse(),sort()   print()直接打印，打印None，就地修改无返回值，打印None
'''
str = 'Hello'
str2 = ['H', 'e', 'l', 'l', 'o']
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = [1, 3, 5, 7, 9]
str3 = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
str4 = ['3','2','5','4','9','7']
'''
列表切片
print(str[1])
print(str[-1])
print(str[1:4])
print(str[:3])
print(str[4:])
print(number[::2])
'''
'''
创建长度为10的空列表
sequence = [None] * 10
print(sequence)
'''
'''
序列相加
print(str2 + number)
'''
'''
序列相乘
num = num * 4
print(num)
'''
'''
判断元素是否在序列中
print(2 in num)
'''
'''
内置函数
print(min(str2))
print(max(str2))
print(max(str))
print(len(str))
'''
'''
将字符串转换为列表
将列表转换为字符串
print(list(str))
print(''.join(list(str)))
'''
'''删除列表中的某个元素
del str2[1]
print(str2)
'''
'''切片赋值
实现序列插入
number[5:5] = list(str)
print(number)
实现序列删除
number[2:5] = []
print(number)
'''
'''
列表方法
append()只能添加一个元素
clear()清空列表内容
copy()复制列表
append(),remove(),insert(),extend(),reverse(),sort()就地修改，无返回值
number.append(str2)
print(number)
# print(number.clear())
print(number.copy())
print(str2.count('l'))
number.extend(str2)
print(number)
print(number.index('H'))
number.insert(3,str2)
print(number)
print(number.pop(3))
print(number)
number.remove(str2)
print(number)
num.reverse()
print(num)
str4.sort()
print(str4)
str3.sort(key=len)
print(str3)
'''


