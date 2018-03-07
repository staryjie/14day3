#!/usr/bin/env python
# -*- coding:utf-8 -*-

### 集合

'''
########## 取两个列表的共有的元素
iPhone7 = ["alex","lucy","lily","bob"]
iPhone8 = ["alex","tom","lily","eric"]

botn_list = []
for name in iPhone7:
    if name in iPhone8:
        botn_list.append(name)
print(botn_list)
'''

'''
集合是无序的，不能重复的数据组合

作用：
1.去重，把一个列表变成集合，就自动去重
2.关系测试，测试两组数据之间的交集、差集、并集等关系
'''

### 创建集合

s = {1,2,3,4}
print(type(s))

li = [1,2,3,4,5,5,2,1]
s1 = set(li)
print(s1,type(s1))

### 增加，一次只能增加一个
s.add(6)
print(s)

## pop()随机删除
s.pop()
print(s)

## remove()删除指定的，不存在会报错
s.remove(2)
print(s)

#discard()，删除指定元素，不存在不会报错
s.discard(6)

#update()
s.update([2,3,4,5])
print(s)

#clear()清空
s.clear()
print(s)
