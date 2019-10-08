# 条件语句及循环语句
'''
    python中False，None,0,"",[],(),{}这些为假，其他为真
    语句格式
    if 条件：
        执行体
    elif 条件:
        执行体
    else：
        执行体
    布尔值运算 &&使用and，||使用or，!使用not
    is 比较对象是否相同，==比较两个对象是否相等，is类似于java中的==，==类似于java中的equals，不可将is用于字符串和数等不可变的基本值
    断言，assert 条件,语句（断言说明） 满足条件继续执行，不满足条件结束执行
'''
name = ''
static_sex = ['N', 'n']
while not name :
    name = input('请输入你的姓名：')
sex = input('请选择您的性别，男：N，女：n')
assert sex in static_sex, '性别输入错误'
while sex not in static_sex:
    sex = input('请正确选择您的性别，男：N，女：n')
if name.endswith('zhang'):
    if sex == 'N':
        print('欢迎您，张先生')
    elif sex == 'n':
        print('欢迎您，张小姐')
    else:
        print('欢迎光临')
else:
    print('欢迎您')

