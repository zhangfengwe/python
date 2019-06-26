# 类
'''
    在属性或方法前 增减‘__’两个下划线，用于表示其私有，不可被外部访问
    抽象类 继承abc中ABC类，方法使用@abstractmethod标注，表示子类必须实现的类
    getattr(obj,name[,default]) 获取属性的值
    setattr(obj,name,value) 设置属性的值
'''
import sys
# sys.path.append(r'D:\project\python\python\study\python07\Person.py')
from Person import *
# from Person import


person = Person()
person2 = Person()
# print(person.name)
person.setName('fwzhang')
print(person.getName())
person.ageAdd()
person.changeFlag()
print('{},{}'.format(person.age,person.flag))
# print(Person.__name)
man = Man()
man.changeFlag()
print('{},{}'.format(person2.age,person2.flag))
print(man.flag)

print(issubclass(Man,Person))#判断是否为子类
print(getattr(man,'flag'))
setattr(person,'name','zhang')
print(getattr(person,'name'))

