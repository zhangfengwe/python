# 随机漫步类

from random import choice
import matplotlib.pyplot as plt


class RandomWalk():

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points:

            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


def make_random_walk():
    rw = RandomWalk()
    rw.fill_walk()
    point_num = list(range(rw.num_points))

    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, c=point_num, cmap=plt.cm.Blues, edgecolor='none', s=15)
    fig.savefig('random_walk_1')
    plt.show()


if __name__ == '__main__':
    make_random_walk()