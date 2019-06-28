# 静态方法，类方法
class TestClass:

    @classmethod
    def clssMethod(cls):
        print('class name is {},full name is {}'.format(cls.__name__,cls.__qualname__))

    @staticmethod
    def staticMethod():
        print('this is static method')

def main():
    TestClass.clssMethod()
    TestClass.staticMethod()

if __name__ == '__main__':
    main()