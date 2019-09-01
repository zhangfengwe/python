# 测试类
from abc import ABC,abstractmethod
class Peo(ABC):
    @abstractmethod
    def talk(self):
        print('talk ........')

class Person(Peo):

    # __name = ''
    # age = 0
    flag = 0

    # 限定自定义对象只能设置某些属性，只对当前类有效
    __slots__ = ('_name', '_age')

    def __init__(self):
        self.name = Person.__name__

    def talk(self):
        print('person talk........')

    '''
        修改get,set方法，使用@property进行优化
    '''
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age

    def ageAdd(self):
        self.age += 1

    def changeFlag(self):
        Person.flag += 1

class Man(Person):
    def changeFlag(self):
        self.flag = True


