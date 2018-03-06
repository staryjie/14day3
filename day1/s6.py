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