#使用模板字符串格式化字符串
'''
使用string模块中Template，通过关键字参数（包含等号的参数），关键字参数使用$定义
'''

from string import Template
tmpl = Template("Hello world ----$langu")
tmpl = tmpl.substitute(langu="python")
print(tmpl)