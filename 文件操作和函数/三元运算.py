#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 对简单条件语句的简写

a = 2
b = 5

# 普通条件判断
if a < b:
    val = a
else:
    val = b

# 三元运算

val = a if a < b else b
print(val)