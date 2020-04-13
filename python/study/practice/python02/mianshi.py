# 面试题相关练习


class Person:

    def __init__(self):
        self.__name = 'fwzhang'

    def __str__(self):
        return self.__name


def jinzhi():
    '''
    进制转换
    :return:
    '''
    a = 20
    # 十进制转换为二进制
    print('20转换为二进制：{}'.format(bin(a)))
    # 十进制转换为八进制
    print('20转换为八进制： {}'.format(oct(a)))
    # 十进制转换为十六进制
    print('20转换为十六进制： {}'.format(hex(a)))


def change():
    '''
    将['1', '2', '3']变为[1, 2, 3]
    :return:
    '''
    print(list(map(lambda x: int(x), ['1', '2', '3'])))


def param_list(a, b=None):
    '''
    函数参数默认值为可变对象，存在问题
    当函数被调用时，参数b使用默认值，只会在第一次调用时初始化，后续调用函数时，参数b的值为第一次初始话后的结果
    :param a:
    :param b:默认值为空list
    :return:
    '''
    # 修改方法
    # 将b的默认值设置为None,在操作前进行一次判断
    if b is None:
        b = []
    b.append(a)
    return b


def param_list_test():
    print(param_list(1))
    print(param_list(2))
    print(param_list('a', []))
    print(param_list(3))


if __name__ == '__main__':
    # person = Person()
    # print(person._Person__name)
    # jinzhi()
    # change()
    # param_list_test()
    key = 'abcde'
    value = range(1, 6)
    b0 = dict(zip(key, value))
    for s in b0:
        print(s)
    print('*' * 6)
    b1 = range(10)
    b2 = [i for i in b1 if i in b0]
    print(b2)
    # for s in b0返回的是对应的dict的键值即索引值
    print([b0[s] for s in b0])
    b3 = [b0[s] for s in b0]
    b4 = [i for i in b1 if i in b3]
    print(b4)
    b5 = {i: i * i for i in b1}
    print(b5)
    b6 = [[i * i] for i in b1]
    print(b6)
