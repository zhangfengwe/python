#字典
'''
    字典是python内置的唯一一种映射类型
    字典通过{}创建，key:value形式，key值是唯一的，每个键值对之间用“,”隔开
    检查字典是否包含指定键的效率比检查列表是否包含某个值的效率高
    可使用format_map()来进行字符串格式设置
    常用方法
        dict(),通过其他映射或者键值对序列创建字典,或者是关键字参数，类似于list,tuple,str是一个类
        类似于序列，存在len(),d[key],d[key]=value,del d[key],key in d 等操作
        clear() 清空字典，就地执行，返回值为None
        copy() 浅复制，副本的值不影响原本，使用copy模块的deecopy()执行深复制，有疑惑，在DirCopy.py中解决
        fromkeys(keys[,values]) 通过keys创建一个字典，值默认为None
        get(key[,defaultValue]) 通过key获取字典中对应值，字典中无该key时，会返回默认值None(可自行设置)，
            d[key]当key不存在时，会触发异常
        items()返回一个包含所有字典项的列表，返回值为字典视图的特殊类型：实例dict_items([('name', 'fwzhang'), ('age', 25), ('sex', '男')])
        keys()返回一个包含所有key的字典视图
        values()返回一个包含所有value的字典视图
        pop(key)获取指定key相关联的value，并删除该字典项
        popitem()随机删除某字典项
        setdefault(key,value),当key值存在时，返回对应值，当key不存在时，新增一个字典项
        update(newDi) 通过一个字典更新另外一个字典，如果当前字典包含key相同的项就更新，没有就增加,返回值为None
'''
from copy import deepcopy

item = [('name','fwzhang'),('age',25),('sex','男')]
str = '我叫{name},今年{age}岁，是一名{sex}生'
item2 = [('account','942640'),('pwd','123qweasd')]
# 使用dict()创建字典
di = dict(item)
di2 = dict(name='fwzhang',age=25,sex='男')
print(di)
print(di2)
print(str.format_map(di))
di2.clear()
print(di2)
# '''
# 浅拷贝与深拷贝
# '''
# di3 = di.copy()
# di3['name'].append('942640')
# print('浅拷贝 {}'.format(di))
# di4 = deepcopy(di)
# di4['name'] = 'zhangfengwei'
# print('深拷贝 {}'.format(di))
print(dict.fromkeys(['name','age','sex'],('unknown')))
print(dict.fromkeys(['name','age','sex']))
print('get方法key存在 {} \nget方法key不存在 {}'.format(di.get('name','who'),di.get('account','the account not found')))
print(di.items())
print(di.keys())
'''
pop,popitem
print(di.pop('sex'))
print(di.popitem())
'''
print('setdefault方法key存在 {} \nsetdefault方法key不存在 {}'.format(di.setdefault('name','who'),di.setdefault('account','123qweasd')))
print(di.values())
di.update(dict(item2))
print(di)
