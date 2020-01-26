# requests模块处理cookie
import requests
import re

url = 'http://www.renren.com/PLogin.do'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

post_data = {
    'email': '此处填写账号',
    'password': '此处填写密码'
}

# 创建session对象
session = requests.Session()
session.headers = headers

# 发送post请求，模拟登陆
session.post(url, data=post_data)

# 验证登录
response = session.get('此处填写人人网个人中心页面的url')
print(response.url)
