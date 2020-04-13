# 单例模式方式

# 1、使用模块，将单例模式的类定义在一个模块中，初次导入模块时创建该类实例，再次导入时不再创建
# 2、使用__new__
# 3、使用装饰器
#    原理：
#       common1 = Common('fwzhang')
#       @singleton相当于Common = singleton（Common），在创建实例对象时会先将Common作为参数传入到singleton函数中，
#       函数在执行过程中不会执行_singleton函数（函数只有调用才会执行），直接返回_singleton函数名。
#       此时可以看作Common = _singleton，创建实例时相当于common1 = _singleton（''），
#       调用get_instance 函数，先判断实例是否在字典中，如果在直接从字典中获取并返回，
#       如果不在执行 instances [cls] = Common（''），
#       然后返回该实例对象并赋值非common1变量，即common1 = instances[cls]。
# 4、使用元类（看不懂）


# 2
class Util:

    def __init__(self):
        self._name = 'zhang'

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return Util._instance


# 3
def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _singleton


@singleton
class Common:

    def __init__(self, name):
        self._name = name


# 4
class SingletonType(type):

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class StringUtil(metaclass=SingletonType):

    def __init__(self):
        self._name = 'zhang'


if __name__ == '__main__':
    util1 = Util()
    util2 = Util()
    print('%d,    %d' % (id(util1), id(util2)))
    common1 = Common('fwzhang')
    common2 = Common('zhang')
    print('%d     %d' % (id(common1), id(common2)))
    string1 = StringUtil()
    string2 = StringUtil()
    print('%d     %d' % (id(string1), id(string2)))
