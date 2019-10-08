# Python第三章 字符串
'''
    字符串：
        不可变，所有适用于列表的方法都可适用于字符串（切片赋值，元素赋值因字符串不可变导致不可使用）
    字符串方法：
        center(长度[,填充符，默认为空格]),长度小于字符串长度时，输出原字符串
        find(substr子字符串[startIndex,endIndex]),查找子字符串是否在字符串中，返回子字符串第一个字符在字符串中的索引值，不存在返回-1，
            指定起点和终点时，包前不包后
        join()合并序列的元素，序列的每个元素必须是字符串
        lower()返回字符串的小写形式,islower()判断字符串中的字符是否都是小写
        replace()替换，返回替换结果,如果子字符串不存在，返回原字符串
        split()将字符串分割为序列
        strip()去除前后空格
        translate()替换单个字符，可同时替换多个字符，效率比replace快
            1、使用str.maketrans(old,new[,del])创建转换表,可使用第三个参数指定要删除的字符
            2、使用translate(转换表)替换字符
'''
string = "Hello world llo"
string2 = "/"
listT = ['', 'app', 'epcc', 'log']
yuZu = ('', 'app', 'epcc', 'log')
strTrim = string.center(30)
strList = string2.join(listT)
print(string.center(30, '*'))
print(strTrim)
print(string.find('llo'))
print(string.find('llo', 0, 4))
print(string.find('llo', 3, 10))
'''
join()方法，参数为序列
'''
print(string2.join(listT))
print(string.lower())
print(string.islower())
print(string.replace('llo', '222'))
print(strList.split(string2))
print(strTrim.strip())
table = str.maketrans('lo', '23', ' ')
print(string.translate(table))
