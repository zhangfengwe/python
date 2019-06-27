# 测试类
from abc import ABC,abstractmethod
class Peo(ABC):
    @abstractmethod
    def talk(self):
        print('talk ........')

class Person(Peo):

    __name = ''
    age = 0
    flag = 0

    def __init__(self):
        self.name = Person.__name__

    def talk(self):
        print('person talk........')

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self,age):
        self.age = age

    def ageAdd(self):
        self.age += 1

    def changeFlag(self):
        Person.flag += 1

class Man(Person):
    def changeFlag(self):
        self.flag = True


