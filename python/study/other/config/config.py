# 外部配置文件
# 使用ini的文件格式
# 只用于生成ini配置文件

import configparser

config = configparser.ConfigParser()

config['logger'] = {'LOG_LEVEL': 'info', 'LOG_FILE': 'log/Python_Study_{}-{}-{}.log', 'LOG_MAX_SIZE': 100 * 1024 * 1024,
                    'LOG_BACKUP_COUNT': 0}

config['database'] = {'user': 'xlink', 'password': '942640', 'host': '127.0.0.1', 'port': '1521', 'dbname': 'HKXLINK'}

config['path'] = {'win_base_path': 'D:/python/', 'linux_base_path': '/home/fwzhang/python/'}

with open('config.ini', 'w') as file:
    config.write(file)
