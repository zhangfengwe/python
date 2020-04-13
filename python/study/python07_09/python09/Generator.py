# 生成器
def createGen(listl):
    '''
    创建生成器
    :param list: 序列
    :return:
    '''
    for sublist in listl:
        for element in sublist:
            # 带有yield语句的方法均为生成器,可以返回多个值
            yield element


def flatten(nested):
    '''
    递归生成器
    :param nested:
    :return:
    '''
    try:
        # 用于判断是否为字符串，为字符串抛出TypeError异常,用于
        # 不使用字符串判断，会造成无穷递归，字符串的第一个元素是一个长度为1的字符串，而长度为1的字符串的第一个元素是字符串本身
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


def main():
    nested = [[1, [2, 6, 7]], [3, [4]], [5], 8, 9, [10, [11, [12]]]]
    li = list(flatten(nested))
    print(sorted(li))
    nested2 = ['foo', ['bar', ['baz']]]
    li2 = list(flatten(nested2))
    print(li2)


if __name__ == '__main__':
    main()
