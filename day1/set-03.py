#!/usr/bin/env python
# -*- coding:utf-8 -*-

s1 = {1,2,3,4,5}
s2 = {2,3,4,7,8,9}

print(s1.difference(s2))
# difference_update(self, *args, **kwargs)
# 从当前集合中删除和B中相同的元素，更新自己
print(s1.difference_update(s2))

# intersection(self, *args, **kwargs)
# 取两个集合的交集，返回一个新的集合，可以用变量接收

s3 = {11,22,33,44,"hehe"}
s4 = {22,"hehe",12,45,87}
ret = s3.intersection(s4)
print(ret)