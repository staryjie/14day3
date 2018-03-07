#!/usr/bin/env python
# -*- coding:utf-8 -*-

###字符串操作-2
# 字符串： 有序，不可变
s = "Hello World!"

#返回列表的索引值，可以指定区间查找，找不到会报错
print(s.index('o',5,8))

s = "22"
#是否是阿拉伯数字，只是数字
print(s.isalnum())
#是否是阿拉伯字符,只是字符
s = "dd"
print(s.isalpha())
#是否是整数，小数也不行
s = "22"
print(s.isdecimal())
print(s.isdigit())

#是否是可用的标识符(变量名)
s = "flag"
s1 = "Hello World"
print(s.isidentifier())
print(s1.isidentifier())

#是否是小写
s = "abc"
print(s.islower())

#是否是大写
s = "ABC"
print(s.isupper())

#只有数字
s = "12345"
print(s.isnumeric())

#是否可以打印
s = "sasa12"
print(s.isprintable())

#是否是空格
s = " "
print(s.isspace())

#是否是标题
s = "Hello Gay"
print(s.istitle())

#将列表转换成字符串，以指定格式分隔
names = ['alex','jack','rain']
s = "-"
print(s.join(names))

#字符串按指定长度向左对齐，不够的以指定字符填充，默认空格
s = "Hello World!"
print(s.ljust(50,'-'))

#变成小写
s = "ABCD"
print(s.lower())

#变大写
s = "abcd"
print(s.upper())

#去除字符串两边(左边/右边)空格（包含空格、换行、tab键）
s = "   hehe  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# 映射关系
str_in = "abcdef"
str_out = "!@#$%^"
table = str.maketrans(str_in,str_out)
s = "abcdeacd"
print(s.translate(table))

#以指定字符串分隔字符串,以第一个匹配的为分隔
s = "Hello World"
print(s.partition('o'))

#替换,可以指定替换次数，默认全部替换
s = "Hello World"
print(s.replace("o","w",1))

#rfind()查找，返回最右边匹配到的索引，找不到返回-1
s = "Hello World"
print(s.rfind('o'))

#返回索引，返回最右边匹配到的索引，找不到报错
s = "Hello World"
print(s.rindex('o'))

#分割字符串，返回一个列表，默认以空格分割
s = "Hello World"
print(s.split())
print(s.split("l"))

print(s.rsplit("o"))
print(s.rsplit("o",1))

#按行分割
s = "abc\ndef\nghi"
print(s.splitlines())

#以什么开始，以什么结束
s = "hello world"
print(s.startswith("hello"))
print(s.endswith("ld"))

#swapcase,字符串全部大写
s = "hello"
print(s.swapcase())

#将字符串转换成title
s = "hello hehe"
print(s.title())

#填充，指定长度右对齐，不够的左边以数字0填充,系统底层做二进制换算用到
s = "hehe"
print(s.zfill(8))


'''
常用：
isdigit
replace
find
count
strip
center
split
join
'''