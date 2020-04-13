# 字符串格式化
def priceFormat(amt, country='CNY'):
    '''
    返回金钱格式的字符串，国家+2为小数
    :param amt:
    :param country: 默认为CNY 中国
    :return:
    '''
    return "{} {:.2f}".format(country, amt)


def menu():
    print('*' * 80)
    print(' ' * 10 + '1-金钱格式化')
    print('*' * 80)


def initMenu():
    # dic = {1=}
    pass


def main():
    menu()
