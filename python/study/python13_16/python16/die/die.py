# 骰子类

from random import randint


class Die():

    def __init__(self, num_sides=6):
        '''
        初始化
        :param num_sides: 骰子面数，默认为6
        '''
        self._num_sides = num_sides

    @property
    def num_sides(self):
        return self._num_sides

    @num_sides.setter
    def num_sides(self, num_sides):
        self._num_sides = num_sides

    def roll(self):
        '''
        模拟摇骰子，返回1到骰子面数之间的随机值
        :return:
        '''
        return randint(1, self.num_sides)

