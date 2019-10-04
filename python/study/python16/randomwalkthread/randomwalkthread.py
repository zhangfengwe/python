# 随机漫步多线程实现

from threading import Thread
import matplotlib.pyplot as plt
from random import choice


class RandomWalk(Thread):

    def __init__(self, num_points=5000, cmap=plt.cm.Blues, start_color='orange', end_color='yellow'):
        super().__init__()
        self.num_points = num_points
        self.cmap = cmap
        self.x_values = [0]
        self.y_values = [0]
        self.start_color = start_color
        self.end_color = end_color

    def run(self):
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

def show_picture(datas):
    # 绘图
    # point_num = list(range(datas[0].num_points))
    fig, ax = plt.subplots()
    for rw in datas:
        point_num = list(range(rw.num_points))
        ax.scatter(rw.x_values, rw.y_values, c=point_num, cmap=rw.cmap, edgecolor='none', s=15)
        # 突出起点和终点
        ax.scatter(rw.x_values[0], rw.y_values[0], color=rw.start_color, s=50)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], color=rw.end_color, s=50)

    # 隐藏坐标轴
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    # 设置边框不可见
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    fig.savefig('random_walk_thread_2')
    plt.show()


def make_random_walk():
    rw = RandomWalk(cmap=plt.cm.Reds, start_color='black', end_color='green')
    rw2 = RandomWalk()
    rw.start()
    rw2.start()
    rw.join()
    rw2.join()

    show_picture([rw, rw2])



if __name__ == '__main__':
    make_random_walk()