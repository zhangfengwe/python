# 常用正则表达式

# .点号为通配符，匹配任意字符，一个点号只匹配一个字符
# ^表示字符串的开头，也用于表示非
# $表示字符串末尾
# *表示对前面的正则表达式0到任意次重复,ab* 可以匹配a,ab,abbbb;
# +表示对前面的正则表达式1到任意次重复,ab+ 可以匹配 ab,abbbbbb;
# ？表示对前面的正则表达式0到1次重复,ab?可以匹配a,ab
# 对于*，+，？来说，他们是贪婪的，会尽可能匹配更多的字符，如<.*>找到‘<a>b<c>’,我们希望找到<a>，实际结果是<a>b<c>,在修饰符后增加？（非贪婪）
#   或者使用‘:dfn:’最小方式匹配
# {m}指定重复次数，可用于指定长度
# {m,n} 逗号不可缺失，匹配m到n次，{m,n}为贪婪模式，{m,n}?非贪婪模式，m缺失时，默认为0，n缺失时，默认为无限大
# []表示字符集合，在集合内特殊字符失效（*,+,）
# | 或者
# (组合)匹配括号内的任意正则表达式，并标识出组合的开头和结尾，在匹配后，组合的内容可以获取，可用于拆解字符串
# (?P<name>....)匹配到的子字符串可以在外部通过定义的name获取
# (?P=name)他匹配前面那个叫name的命名组匹配到的同样的字符串。两者组合可用于匹配xml,html中闭合标签的内容
# (?#..)注释
# \A 只匹配字符串开始；\b匹配空字符串，但只出现在单词开始或结尾位置；\B 为前者的取反，同样是匹配空字符串，但是不能在开头或结尾
# \d = [0-9],\D = [^0-9];  \s 匹配任意空白字符（换行等）[\n\t\f\r\v], \S:\s的取非
# \w = [a-zA-Z0-9]; \W = [^a-zA-Z0-9]; \Z 只匹配字符串尾

# 手机号正则表达式
PHONE_COM = r'^1[0-9]{2}\d{8}$'

# 18/15位身份证号正则表达式
ID_COM = r'(^[1-9]\d{5}(18|19|([2-9]\d))\d{2}([0][1-9]|[1][0-2])(0[1-9]|[12]\d|3[01])\d{3}[0-9xX]$)|' \
         r'(^[1-9]\d{5}\d{2}([0][1-9]|[1][0-2])(0[1-9]|[12]\d|3[01])\d{3}$)'

# 15位身份证号正则表达式
# ID_15_COM = r'^[1-9]\d{5}\d{2}([0][1-9]|[1][0-2])(0[1-9]|[12]\d|3[01])\d{3}$'

# 拆分18位身份证号正则表达式
# 使用注释需要使用'''(3引号)
ID_18_COM_X = r'''^(?P<province>\d{2}) # 省份
                  (?P<city>\d{2}) # 市
                  (?P<town>\d{2}) # 城镇
                  (?P<birthday>\d{8}) #出生日期
                  (?P<seq>\d{3}) # 序列号
                  (?P<check>[0-9Xx])$ # 校验码'''

# 拆分15位身份证号正则表达式
ID_15_COM_X = r'''^(?P<province>\d{2}) # 省份
                  (?P<city>\d{2}) # 市
                  (?P<town>\d{2}) # 城镇
                  (?P<birthday>\d{6}) #出生日期
                  (?P<seq>\d{3})$ # 序列号'''

# 汉字正则表达式
CHINESE_COM = u'[\u4e00-\u9fa5]'



