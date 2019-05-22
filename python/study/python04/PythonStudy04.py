#字典
'''
    字典是python内置的唯一一种映射类型
    字典通过{}创建，key:value形式，key值是唯一的，每个键值对之间用“,”隔开
    检查字典是否包含指定键的效率比检查列表是否包含某个值的效率高
    可使用format_map()来进行字符串格式设置
    常用方法
        dict(),通过其他映射或者键值对序列创建字典,或者是关键字参数，类似于list,tuple,str是一个类
        类似于序列，存在len(),d[key],d[key]=value,del d[key],key in d 等操作

'''
item = [('name','fwzhang'),('age',25),('sex','男')]
str = '我叫{name},今年{age}岁，是一名{sex}生'
# 使用dict()创建字典
di = dict(item)
di2 = dict(name='fwzhang',age=25,sex='男')
print(di)
print(di2)
print(str.format_map(di))