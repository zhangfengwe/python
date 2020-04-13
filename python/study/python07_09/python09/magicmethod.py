# 魔法方法


class MagicMethod:

    def __init__(self, name='MagicMethod'):
        self._name = name

    def __repr__(self):
        # 输出一个对象的官方字符串表示
        print('__repr__被调用')
        return '魔法方法repr实验'

    def __str__(self):
        print('__str__被调用')
        return self._name

    def __format__(self, format_spec):
        # str.format()调用该方法
        print('__format__被调用')
        return self._name + format_spec * 5 + self._name

    # __hash__和__eq__方法类似于Java中的equal()和hashCode方法
    def __hash__(self):
        # hash()调用该方法，对哈希集的成员进行操作
        return hash((self._name, '1234'))

    def __bool__(self):
        # 真实值检测，bool()调用
        print('__bool__被调用')
        if self._name == 'MagicMethod':
            return True
        return False


if __name__ == '__main__':
    m = MagicMethod()
    print(m)
    print(str(m))
    print('{:*}'.format(m))
    if m:
        print('true')
    m1 = MagicMethod(name='m1')
    if not m1:
        print('false')

