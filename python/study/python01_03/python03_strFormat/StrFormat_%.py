# 使用%格式转换符进行格式化字符串
'''
常见格式转换符：
    %s 以字符串str()形式输出  %10 前补空格，总长度为10
    %r 以字符串repr()形式输出（即转义字符原样打印）
    %c 单个字符
    %b 二进制整数 错误的，不存在该方式，可使用后面的format()方法来实现
    %d 十进制整数
    %i 十进制整数
    %o 八进制整数  %010,前补零，总长度为10
    %x 十六进制整数
    %e 指数，底数为e
    %E 指数，底数为E
    %f或%F 浮点数  %.3f  保留3为小数
    %g 指数（e）或浮点数（根据长度）
    %G 指数（E）或浮点数（根据长度）
'''
str = ['a', 'b']
num = 'a'
num2 = 16
num3 = 100010
strY = ('hello world\n', 'fwzhang')
format = "%s%10s"
print(format % strY)
print('%c' % num)
temp = '{num:b}' .format(num=num2)
print(temp)
temp = '%010o' % num2
print(temp)
temp = '%x' % num2
print(temp)
temp = '%e' % num3
print(temp)
temp = '%E' % num3
print(temp)
temp = '%10.3f' % num2
print(temp)
temp = '%g' % num3
print(temp)
