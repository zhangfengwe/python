# 普通线图
# 使用matplotlib

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def main():
    # 获取数据
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s, )

    ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')

    ax.grid()

    fig.savefig('test.png')
    plt.show()

if __name__ == '__main__':
    main()
