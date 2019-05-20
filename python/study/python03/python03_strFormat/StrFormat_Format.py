#使用format()方法格式化字符串
'''
    1、替换字段名，使用{}包裹，可使用字段名或者索引，指定哪个值的格式，用结果进行替换
        只是用{}，结果按照默认顺序的索引进行替换
        {0...n}，带有索引，结果按照索引进行替换，索引从0开始
        {key},带有参数名，类似于关键字参数，使用等于号
        不仅仅使用提供的值本身，还可使用其组成部分，序列中索引对应的值或者对象的属性
    2、转换标志，！感叹号后的单个字符，使用指定的函数将对象转换为字符串，现支持的字符有r(表示repr),s(表示str),a(表示ASCII)
    3、格式说明符，:冒号后面的表达式，设置字符串的格式，（字符串，精度，浮点数等）
'''
import math

str1 = 'Hello {},I am {}'
str2 = 'Hello {1},I am {0}'
str3 = 'Hello {obj},I am {name}'
print(str1.format('world','python'))
print(str2.format('python','world'))
print(str3.format(obj='world',name='python'))
'''
转换标志
'''
print('{pi!s}  {pi!r}  {pi!a}'.format(pi='π'))