# 推导式


def list_compre():
    result = [i for i in range(30) if i % 2 == 0]
    print(type(result))
    print(result)


def dict_compre():
    result = {v: k for k, v in {'a': 30, 'b': 40}.items()}
    print(type(result))
    print(result)
    pass


def set_compre():
    result = {x for x in range(50) if x % 5 == 0}
    print(type(result))
    print(result)
    pass


def generator_compre():
    result = (x for x in range(50) if x % 5 == 0)
    print(type(result))
    for i in result:
        print(i)
    pass


from functools import reduce


def lambda_test():
    # lambda传递一个函数作为参数
    lam = lambda x: x*x
    lam_reduce = lambda x, y: x + y
    result = []
    for i in map(lam, range(5)):
        result.append(i)
    print(result)
    print(reduce(lam_reduce, result))


if __name__ == '__main__':
    list_compre()
    dict_compre()
    set_compre()
    generator_compre()
    lambda_test()

