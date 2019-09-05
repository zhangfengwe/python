# python线程之间通信
# 加锁

from threading import Thread, Lock
from time import time, sleep


class Account:

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)#模拟其他操作
            self._balance = new_balance
        finally:
            self._lock.release()


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():

    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    balance = account.balance
    print('账户余额为{:.2f}元'.format(balance))


if __name__ == '__main__':
    main()