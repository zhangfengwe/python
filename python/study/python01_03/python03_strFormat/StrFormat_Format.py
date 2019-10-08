#使用format()方法格式化字符串
'''
    1、替换字段名，使用{}包裹，可使用字段名或者索引，指定哪个值的格式，用结果进行替换
        只是用{}，结果按照默认顺序的索引进行替换
        {0...n}，带有索引，结果按照索引进行替换，索引从0开始
        {key},带有参数名，类似于关键字参数，使用等于号
        不仅仅使用提供的值本身，还可使用其组成部分，序列中索引对应的值或者对象的属性
    2、转换标志，！感叹号后的单个字符，使用指定的函数将对象转换为字符串，现支持的字符有r(表示repr),s(表示str),a(表示ASCII)
    3、格式说明符，:冒号后面的表达式，设置字符串的格式，（字符串，精度，浮点数等）
        3.1 类型说明符
            b  整数转换为二进制数
        3.2
'''
import math

str1 = 'Hello {},I am {}'
str2 = 'Hello {1},I am {0}'
str3 = 'Hello {obj},I am {name}'
str4 = 'Hello {obj},I am {0}'
num1 = 26
num2 = 160000000000
num3 = 0.1
'''
索引，关键字参数可以混用,索引在前，关键字参数在后
'''
print(str1.format('world','python'))
print(str2.format('python','world'))
print(str3.format(obj='world',name='python'))
print(str4.format('python',obj='world'))
'''
转换标志
'''
print('{pi!s}  {pi!r}  {pi!a}'.format(pi='π'))
'''
格式说明符
'''
print('{:b}'.format(num1))
print('{:n}'.format(num2))
print('自动在浮点数和科学计数法中选择 {:g}'.format(num2))
print('{:G}'.format(num2))
print('科学计数法，小写字母e {:e}'.format(num2))
print('科学计数法，大写字母E {:E}'.format(num2))
print('8进制 {:o}'.format(num1))
print('16进制，使用大写字母 {:X}'.format(num1))
print('16进制，使用小写字母 {:x}'.format(num1))
print('百分数表示,保留两位小数 {:.2%}'.format(num3))
'''
    宽度由整数确定
    精度由点加整数确定,值默认使用浮点数
    逗号（,）为千分位分隔符
    左对齐，右对齐，居中，对应符号<,>,^;字符串前补符号，或后补符号可使用对其符号
'''
print('千分位分隔符 {:,}'.format(num2))
print('宽度为10，精度为保留两位小数 {:10.2f}'.format(num1))
print('前补*,宽度为10---- {:*>10}'.format('123'))