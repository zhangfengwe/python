# 普通线图
# 使用matplotlib

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def main():
    # example_1()
    # example_2()
    # example_3()
    # test()
    # example_4()
    # example_5()
    # example_6()
    example_7()


def example_1():
    # 获取数据
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)
    # ax2的数据
    input_values = [0, 1, 2, 3, 4, 5]
    squares = [0, 1, 4, 9, 16, 25]

    fig, (ax, ax2) = plt.subplots(nrows=1, ncols=2)
    ax.plot(t, s)
    ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='matplotlib_example_ax')
    # ax.set(linewidth=5)

    ax2.plot(input_values, squares)
    ax2.set(title='matplotlib_example_ax2', xlabel='num', ylabel='num^2')
    # ax.grid()

    fig.savefig('example_1.png')
    plt.show()


def example_2():
    input_values = [0, 1, 2, 3, 4, 5]
    squares = [0, 1, 4, 9, 16, 25]
    plt.figure()
    plt.plot(input_values, squares, linewidth=5)
    plt.title('matplotlib_example_2')
    plt.ylabel('score')  # 显示y轴的标签
    plt.xlabel('num')  # 用于显示x轴的标签
    plt.axis([-5, 10, -5, 25])  # 表示于x轴的显示范围，和y轴的显示范围
    plt.savefig('example_2')  # 将画出的图片保存下来PNG文件
    plt.show()


def example_3():
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 200)
    data_obj = {'x': x, 'y1': 2 * x + 1, 'y2': 3 * x + 1.2,
                'mean': 0.5 * x * np.cos(2*x) + 2.5 * x + 1.1}

    ax.fill_between('x', 'y1', 'y2', color='yellow', data=data_obj)

    ax.plot('x', 'mean', color='black', data=data_obj)
    fig.savefig('example_3')
    plt.show()


def example_4():
    x = np.arange(10)
    y = np.random.randn(10)
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='red')
    fig.savefig('example_4')
    plt.show()


def example_5():
    np.random.seed(1)
    x = np.arange(10)
    y = np.random.randn(10)

    fig, axes = plt.subplots(ncols=2, figsize=plt.figaspect(1/2))

    # 水平条形图 返回artists数组，可以用于操控每个条形图
    vert_bars = axes[0].bar(x, y, color='lightblue', align='center')
    # 垂直条形图
    horiz_bars = axes[1].barh(x, y, color='lightblue', align='center')

    # 在水平或垂直方向上画线
    axes[0].axhline(0, color='gray', linewidth=2)
    axes[1].axvline(0, color='gray', linewidth=2)

    for bars in (vert_bars, horiz_bars):
        for bar, height in zip(bars, y):
            if height < 0:
                bar.set(edgecolor='darkred', color='salmon', linewidth=3)

    fig.savefig('example_5')
    plt.show()


def example_6():
    np.random.seed(1345)
    n_bins = 10
    x = np.random.randn(1000, 3)

    fig, axes = plt.subplots(ncols=2, nrows=2)
    ax0, ax1, ax2, ax3 = axes.flatten()

    colors = ['red', 'tan', 'lime']

    ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
    ax0.legend(prop={'size': 10})
    ax0.set_title('bars with legend')

    ax1.hist(x, n_bins, density=True, histtype='barstacked')
    ax1.set_title('stacked bar')

    ax2.hist(x, histtype='barstacked', rwidth=0.9)

    # x[:, 0] 用于处理多维数组，矩阵，即x[:, m:n],获取所有数据的m到n-1列的数据，包左不包右
    ax3.hist(x[:, 0], rwidth=0.9)
    ax3.set_title('different simple sizes')

    fig.tight_layout()
    fig.savefig('example_6')
    plt.show()


def example_7():
    labels = ['a', 'b', 'c', 'd']
    sizes = [15, 30, 45, 10]
    # 突出饼图的某一块
    explode = (0, 0.1, 0.05, 0)

    fig, (ax1, ax2) = plt.subplots(2)
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
    ax1.axis('equal')

    ax2.pie(sizes, autopct='%1.2f%%', shadow=True, startangle=90, explode=explode, pctdistance=1.12)
    ax2.axis('equal')
    ax2.legend(labels=labels, loc='upper right')

    fig.savefig('example_7')
    plt.show()



def test():
    data = [('apples', 2), ('oranges', 3), ('peaches', 1)]
    fruit, value = zip(*data)
    print(value)
    print(fruit)


if __name__ == '__main__':
    main()
