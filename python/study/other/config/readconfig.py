# 读取配置文件

import configparser
import os


class MyConfig:
    config = configparser.ConfigParser()
    # @staticmethod
    # def load_config_file():

    try:
        CONFIG_PATH = os.environ['CONFIG_PATH']
    except Exception:

        CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        if not CONFIG_PATH:
            raise FileNotFoundError
    # 读取使用绝对路径
    # 在其他模块中使用时，使用相对路径会读取失败
    config.read(CONFIG_PATH)

    @staticmethod
    def get_value(section, option):

        try:
            return MyConfig.config.get(section=section, option=option)
        except ValueError:
            raise ValueError


def main():
    print(MyConfig.get_value('logger', 'log_level'))


if __name__ == '__main__':
    main()


