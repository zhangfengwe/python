#字典的浅复制和深复制
'''
    copy()浅复制
    deepcopy()深复制
'''
from copy import deepcopy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
z = x
m = deepcopy(x)
y['machines'].remove('baz')
y['username'] = 'mlh'
z['username'] = 'fwzhang'
z['machines'].append('row')
m['machines'].append('tool')
m['username'] = 'zhangfengwei'
'''
浅复制：
    副本替换不会影响原件，副本中字典项就地修改就会影响原原件，原因字典中键指向值，替换副本中的键指向新的值（可以理解为有新的地址），
    原件中的键还是指向原有的地址，原件不发生改变。就地修改，副本中的键指向的值的地址不变，值变了，原件中的键还是指向该地址，所以原
    件改变
深复制：
    副本改变不会影响原原件
等于号：
    副本替换，就地修改都会影响原件
'''
print('原本{}\n副本{}\n等于号创建{}\n深复制{}'.format(x,y,z,m))