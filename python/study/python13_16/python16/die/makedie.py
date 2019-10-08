# 随机摇骰子，绘画柱形图

import matplotlib
import matplotlib.pyplot as plt

from python.study.python13_16.python16.die.die import Die

# 标题中文显示为方框解决办法
chinfo = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')


def make_data_D6():
    '''
    随机掷六面骰子，获取每个点数出现的次数
    :return:
    '''
    die = Die()
    # 掷骰子1000次
    results = []
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)
    # 统计出现次数
    frequencies = []
    for value in range(1, die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)
    return frequencies


def make_data_d6_add(*die_sides, roll_num=1000):
    '''
    随机掷两个骰子1000次，点数和出现的次数
    :return:
    '''
    die1 = Die(die_sides[0])
    die2 = Die(die_sides[1])
    results = []
    for roll_num in range(roll_num):
        result = die1.roll() + die2.roll()
        results.append(result)

    frequencies = []
    for added in range(2, die1.num_sides + die2.num_sides +1):
        frequency = results.count(added)
        frequencies.append(frequency)
    return frequencies


def show_data(x, y, pic_name, title):
    fig, ax = plt.subplots()

    ax.bar(x, y, color='lightblue', align='center')
    ax.set_title(title, fontproperties=chinfo)
    # 设置x轴的刻度间隔为1
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    fig.savefig(pic_name)
    plt.show()


if __name__ == '__main__':
    frequencies = make_data_D6()
    show_data(range(1,7), frequencies, 'die_d6', '点数出现次数统计')
    frequencies2 = make_data_d6_add(6, 6, roll_num=1000)
    show_data(range(2,13), frequencies2, 'die_d6_add', '点数之和次数统计')