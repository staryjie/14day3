#!/usr/bin/env python
# -*- coding:utf-8 -*-


### 集合的关系测试

'''
交集
差集
并集
对称差集
'''

iPhone7 = {"alex","lucy","lily","bob"}
iPhone8 = {"alex","tom","lily","eric"}

#### 交集
s1 = iPhone7.intersection(iPhone8)
s2 = iPhone7 & iPhone8
print(s1)
print(s2)

#### 差集
s3 = iPhone7.difference(iPhone8)
s4 = iPhone7 - iPhone8
print(s3)
print(s4)

s5 = iPhone8.difference(iPhone7)
s6 = iPhone8 - iPhone7
print(s5)
print(s6)

#### 并集
s7 = iPhone7.union(iPhone8)
s8 = iPhone7 | iPhone8
print(s7)
print(s8)

#### 对称差集
s9 = iPhone7.symmetric_difference(iPhone8)
print(s9)

### 子集超集
se1 = {1,2,3,4,5}
se2 = {2,3,4}

print(se2.issubset(se1))
print(se2 <= se1)

print(se1.issuperset(se2))
print(se1 >= se2)

#### 判断两个集合是不是不想交,True不想交，False相交
print(iPhone7.isdisjoint(iPhone8))