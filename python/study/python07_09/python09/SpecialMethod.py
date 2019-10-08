# 特殊方法
'''
    _init_  构造函数
'''


def checkIndex(index):
    '''
    判断index是否合法
    :param index: 指定的索引是否合法
    :return:
    '''
    if not isinstance(index,int):
        raise TypeError
    if index < 0 :
        raise IndexError


class noLenList:

    def __init__(self,start=0,step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, item):
        checkIndex(item)

        try:
            return self.changed[item]
        except KeyError:
            return self.start + item * self.step

    def __setitem__(self, key, value):

        checkIndex(key)
        self.changed[key] = value


class CounterList(list):

    def __init__(self,*args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, item):
        self.counter += 1
        return super().__getitem__(item)


def main():

    s = noLenList(1, 2)
    print(s[2])
    s[3] = 9
    print(s[3])
    print(s[5])
    # print(s[-2])
    li = CounterList(range(10))
    print(li)
    print('{} + {} = {}'.format(li[2], li[3], li[2] + li[3]))
    print(li.counter)


if __name__ == '__main__':
    main()
