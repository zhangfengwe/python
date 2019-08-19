# 菜单显示类

import python.study.other.yinghua as yin

class menu:

    screen_width = 100
    text_width = 50

    def __init__(self, lists):
        '''
        菜单类初始话
        :param lists: 每一项为一个字典,{index:1,desc:'测试功能',obj:A,method:'func'}
        :type lists:list
        '''
        self.menu_list = lists
        self.menu_list.sort(key=lambda e: e.__getitem__('index'))

    @property
    def menus(self):
        return self.menu_list

    @menus.setter
    def menus(self, lists):
        self.menu_list = lists

    def show_menu(self):
        '''
        打印菜单
        :return:
        '''
        box_width = self.text_width + self.screen_width // 2
        left_margin = (self.screen_width - box_width) // 2
        print(' ' * left_margin + '*' * box_width)
        print(' ' * left_margin + '功能列表'.center(box_width - 6) )

        for menu in self.menu_list:
            content = '{}、{}：'.format(menu.get('index'), menu.get('desc'))
            print(' ' * left_margin + ' ' * 25 + content +
                  ' ' * (self.screen_width - 27 - len(content.encode('gbk'))))
        print(' ' * left_margin + ' ' * 25 + '0、退出' +
              ' ' * (self.screen_width - 27 - len('0、退出'.encode('gbk'))))
        print(' ' * left_margin + '-' * box_width)


    def chose_func(self):
        '''
        选择功能并执行
        :return:
        '''
        while True:
            chose = int(input('please input your chose:'))
            if not chose:
                exit()
            dic_chosed = self.menu_list[chose-1]
            func = getattr(dic_chosed.get('obj'),dic_chosed.get('method'),None)
            if func:
                if dic_chosed.get('paramflag'):
                    func(dic_chosed.get('obj'))
                else:
                    func()
            else:
                print('the function you chosed is not exit')
        else:
            exit()

    def test_func(self):
        a = int(input('the first param:'))
        b = int(input('the second param'))
        print(a**b)


def main():
    test_menu = []
    func1 = dict(index=1, desc='测试功能1', obj=menu, method='test_func', paramflag=True)
    func2 = dict(index=2, desc='樱花', obj=yin, method='main', paramflag=False)
    func3 = dict(index=3, desc='测试功能1')
    test_menu.append(func3)
    test_menu.append(func2)
    test_menu.append(func1)
    menu_t = menu(test_menu)
    # menu_t.menus = test_menu
    menu_t.show_menu()
    menu_t.chose_func()

if __name__ == '__main__':
    main()