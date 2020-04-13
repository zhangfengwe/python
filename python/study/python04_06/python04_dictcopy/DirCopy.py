# 字典的浅复制和深复制
'''
    copy()浅复制
    deepcopy()深复制
'''
from copy import deepcopy
# x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
# y = x.copy()
# z = x
# m = deepcopy(x)
# y['machines'].remove('baz')
# y['username'] = 'mlh'
# z['username'] = 'fwzhang'
# z['machines'].append('row')
# m['machines'].append('tool')
# m['username'] = 'zhangfengwei'
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
# print('原本{}\n副本{}\n等于号创建{}\n深复制{}'.format(x, y, z, m))


def copy_test():
    '''
    浅拷贝测试，修改副本中的值
    预计输出：副本修改不可变对象，原本值不变，副本修改可变对象（list）,原本随之发生改变
    :return:
    '''
    a = [1, 2, 3, 4, ['a', 'b'], 5]
    a_dict = {'username': 'zhang', 'machines': ['foo', 'bar', 'baz']}
    # 浅拷贝
    c = a.copy()
    c_dict = a_dict.copy()
    c[0] = 'e'
    c[4].append('c')
    c_dict['age'] = 25
    c_dict['machines'].append('dict_copy')
    c_dict['username'] = 'admin'
    print('list--->原本：{} \n浅拷贝：{}'.format(a, c))
    print('dict--->原本：{} \n浅拷贝：{}'.format(a_dict, c_dict))


def deepcopy_test():
    '''
    深拷贝测试
    预计输出：副本修改可变对象（list）,不影响原本
    :return:
    '''
    a = [1, 2, 3, 4, ['a', 'b'], 5]
    a_dict = {'username': 'zhang', 'machines': ['foo', 'bar', 'baz']}
    # 深拷贝
    d = deepcopy(a)
    d_dict = deepcopy(a_dict)
    d[0] = 'deepcopy'
    d[4].append('f')
    d_dict['age'] = 25
    d_dict['machines'].append('dict_deepcopy')
    d_dict['username'] = 'admin_ddepcopy'

    print('list---->原本：{}  \n深拷贝：{}'.format(a, d))
    print('dict---->原本：{}  \n深拷贝：{}'.format(a_dict, d_dict))


def equals_test():
    '''
    等于号，就地修改
    预计输出：副本与原本一致
    :return:
    '''
    a = [1, 2, 3, 4, ['a', 'b'], 5]
    a_dict = {'username': 'zhang', 'machines': ['foo', 'bar', 'baz']}
    # 等于号
    c = a
    c_dict = a_dict
    c[0] = 'e'
    c[4].append('c')
    c_dict['age'] = 25
    c_dict['machines'].append('dict_equals')
    c_dict['username'] = 'admin'
    print('list--->原本：{} \n等于号：{}'.format(a, c))
    print('dict--->原本：{} \n等于号：{}'.format(a_dict, c_dict))


if __name__ == '__main__':
    copy_test()
    deepcopy_test()
    equals_test()

