# 常用标准库

import sys
import fileinput as fli

def sysMoudle():
    # 输出脚本路径及脚本名
    print(sys.argv)
    print(sys.platform)

def osMoudle():
    pass

def fileinputMoudle():
    print(fli.filename())
    # fli.close()



def main():
    sysMoudle()
    fileinputMoudle()

if __name__ == '__main__':
    main()