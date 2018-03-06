#!/usr/bin/env python
# -*- coding:utf-8 -*-

#### 列表的深浅拷贝

'''
#先看变量
a = 1
b = a
print(id(a),id(b))
a = 3
print(id(a),id(b))
'''


'''
names = ['alex','jack','1','mack','racheal','shanshan']
n2 = names
#n2列表指向names列表的内存地址
print(id(names))
print(id(n2))
print(id(names[0]))
print(id(n2[0]))
print(id(names[1]))
print(id(n2[1]))
#修改其中一个列表中的元素，另一个列表的元素也会改变
names[2] = "2"
print(names[2])
print(n2[2])
'''

names = ['alex','jack','1','mack','racheal','shanshan']
n2 = names.copy()
#两个列表指向了不同的内存地址，即这是两个独立的列表
print(id(names))
print(id(n2))

#修改其中一个列表中的元素，对另一个列表无影响
names[1] = "staryjie"
print(names[1])
print(n2[1])

#但是两个列表中相同索引的相同内容的元素的内存地址却是相同的
print(id(names[0]))
print(id(n2[0]))

print(id(names[1]))
print(id(n2[1]))

#列表的copy()只是产生了一个新的列表，但是列表中的元素的内存地址是相同的，修改其中一个列表的元素内容，
# 只是在内存中新开辟一块空间，将该列表中该索引位置指向这个新开辟的内存地址。适用于列表中嵌套列表

names = ['alex','jack','1','mack','racheal','shanshan',['longting',24]]
n3 = names.copy()
names[0] = "Alex Li"
print(names)
print(n3)

print(id(names[-1]))
print(id(n3[-1]))
# copy()嵌套子列表的列表时，子列表指向的内存地址是相同的
names[-1][0] = "龙庭"
print(names[-1])
print(n3[-1])

################ 以上内容都是列表的浅拷贝 #####################
# 第一层生效，第二层不生效

import copy

# 深拷贝，拷贝之后两个列表是完全独立的
n4 = copy.deepcopy(names)
#两个列表的内存地址不同
print(id(names))
print(id(n4))

#修改其中一个子列表元素内容，对另一个深拷贝的列表的子列表无影响
names[-1][0] = "hehe"
print(names)
print(n4)
