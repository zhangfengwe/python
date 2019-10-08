import random
# 八皇后问题


def confict(state, nextX):
    '''
    判断是否发生冲突
    :param state: 表示状态的列表
    :param nextX:
    :return:
    '''
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0,nextY-i):
            return True
    return False


def queen(num, state=()):
    '''
    递归
    :param num:
    :param state:
    :return:
    '''
    for pos in range(num):
        if not confict(state, pos):
            if len(state) == num -1:
                yield (pos,)
            else:
                for result in queen(num, state + (pos,)):
                    yield (pos,)+result


def formatQueen(result):
    li = random.choice(list(result))
    print(li)
    for pos in li:
        print('. ' * pos + 'Q ' + '. ' * (len(li)-pos-1))


def main():

    formatQueen(queen(8))


if __name__ == '__main__':
    main()
