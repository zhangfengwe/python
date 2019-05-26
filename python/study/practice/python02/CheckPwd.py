# 列表成员资格示例，in运算符使用
# 检查用户名密码是否匹配

# 模拟数据库用户表,使用字典更佳
database = [
    ['fwzhang','123456'],
    ['zhangfengwei','123qweasd'],
    ['xiaoming','1234567890']
]
account = input('请输入账户：')
pwd = input('请输入密码：')
if [account,pwd] in database:
    print('输入正确，请进行下一步操作')
else:
    print('密码或用户名不正确')