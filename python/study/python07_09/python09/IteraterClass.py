# 迭代协议
class Iterater:

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        # 使用序列解包的原理，首先计算a+b,然后将等号后面的同时赋值给左边的
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            # 防止迭代器过长，装换为序列时出现错误
            raise StopIteration
        return self.a


def main():
    itera = Iterater()
    # for i in itera:
    #     print(i)
    #     if i > 5:
    #         break
    it = list(itera)
    print(it)
    # for j in range(10):
    #     print(it[j])


if __name__ == '__main__':
    main()
