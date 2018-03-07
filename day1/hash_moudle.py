#!/usr/bin/env python
# -*- coding:utf-8 -*-

#将任意长度的字符串通过散列算法，变成固定长度的输出，散列值的空间一般小于输入值，不同的输入可能会散列成相同的散列值
'''
被hash的内容必须是固定的（不可变的）
用途：
文件签名
MD5加密
密码验证
'''

print(hash("staryjie"))
print(hash("staryjie1"))
print(hash("staryjie2"))
