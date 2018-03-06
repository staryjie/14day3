#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
## 字符串，不可变

a = "jie"
print(id(a))
a = "staryjie"
print(id(a))
#两次变量a的内存地址是不一样的，说明a的第二次赋值并不是把之前的内容修改了，而是在内存中创建了一个新的内容，a变量指向了新的内存地址、
'''

### 字符串的方法

s = "Hello World!"
#大写变小写，小写变大写，并不是修改原值，而是在内存中生成一个新的字符串
print(s.swapcase())
# 返回一个首字母大写的字符串
print(s.capitalize())
#返回一个全部小写的字符串
print(s.casefold())
#字符串居中，指定长度，不足的两侧用指定字符填充
print(s.center(50,"*"))
#统计字符串中元素的个数,可以指定范围统计
print(s.count('o',0,5))
#判断是否以指定内容结尾
print(s.endswith("!"))
print(s.endswith("!s"))
#扩展tab键
s2 = "a\tbc"
print(s2)
print(s2.expandtabs(5))
#查找元素，并返回索引，查不到返回-1
print(s.find('o',1,5))
print(s.find('w'))
#格式化
s3 = "My name is {0}, i am {1} years old."
print(s3.format("staryjie",26))
s3 = "My name is {name}, i am {age} years old."
print(s3.format(name="staryjie",age=26))