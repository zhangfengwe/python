# 自定义异常类
class MyException(Exception):

    def printExe(self):
        print(MyException.__name__)