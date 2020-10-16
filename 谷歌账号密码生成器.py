# !/usr/bin/python3
# --coding:utf-8--
# @Author:吴磊
# @Time: 2019年11月20日18时
# @File: 谷歌账号密码生成器.py

import random

# 新建一个字符列表
lib2 = []
# 添加数字集合
lib2.extend(i for i in range(0, 10))
# 添加大写字母 64-90
lib2.extend(chr(i) for i in range(65, 91))
# 添加小写字母 97-122
lib2.extend(chr(i) for i in range(97, 123))


# 开始合成
def synthesis(number1=8, number2=8):
    """

    Args:
        number1: 账号的位数, 默认为8
        number2: 密码的位数, 默认为8

    """
    account = ''
    password = ''
    for i in range(number1):
        account += str(random.choice(lib2))
    for i in range(number2):
        password += str(random.choice(lib2))
    account += "@gmail.com"
    print(account)
    print(password)
    with open("stc.txt", 'a') as f:
        f.write(account + '\n' + password + '\n')


if __name__ == '__main__':
    # with open('stc.txt', 'r') as f:
    #     print(f.read().strip('\n'))
    # synthesis()
    print(lib2)
    
    

