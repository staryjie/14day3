#!/usr/bin/env python
# -*- coding:utf-8 -*-

''''
列表的功能：
创建
查询
切片
增加
修改
删除
循环
排序
'''


'''
#创建
## 方法一
l1 = []
l2 = [1,2,3,4,5]
names = ['alex','lily','luffy','sanzhi']
##方法二，一般不用
l3 = list()
'''

'''
#查询
## 通过索引
print(l2[0])
print(names[1])
#取最后一个可以用索引-1
print(names[-1])
print(names[-2])
## 获取指定内容的索引值（默认取第一个匹配的）
id = names.index('luffy')
print(names[id])
## 统计元素个数
n2 = ['alex','lily','luffy','sanzhi',1,2,3,4,5,5,5,5,6,6,7,8,9,1,3]
print(names.count(5))
'''

'''
#切片，只能从左往右切片
## 顾头不顾尾
n2 = ['alex','lily','luffy','sanzhi',1,2,3,4,5,5,5,5,6,6,7,8,9,1,3]
print(n2[0:3])
## 取后五个（注意索引前后位置，必须从左往右）
print(n2[-5:])
print(n2[:3])
## 按步长取
print(n2[0:6:1])
print(n2[0:6:2])
print(n2[:-1:3])
print(n2[::2])
'''

'''
#增加
n2 = ['alex','lily','luffy','sanzhi',1,2,3,4,5,5,5,5,6,6,7,8,9,1,3]
## append()，追加,放在列表最后面
n2.append('Peiqi')
print(n2)
## 插入，插入指定索引，其后索引加1
n2.insert(0,'staryjie')
print(n2)
'''

'''
#修改
n2 = ['alex','lily','luffy','sanzhi',1,2,3,4,5,5,5,5,6,6,7,8,9,1,3]
## 修改单个元素
n2[2] = 'tutu'
print(n2,n2[2])
## 修改连续多个元素
n2[0:3] = 'haha'
n2[4:6] = ['jack chen','jack zhou']
print(n2)
'''

'''
#删除
n2 = ['alex','lily','luffy','sanzhi',1,2,3,4,5,5,5,5,6,6,7,8,9,1,3]
## pop()，删除最后一个元素,删除的元素可以赋值给变量
res = n2.pop()
print(res,n2)
## remove()删除指定元素，删除从左往右第一个匹配到的元素，只能一个个删除
n2.remove(3)
print(n2)
## del()，删除指定索引的元素,是一个全局性的方法，可以批量删除
del n2[2]
print(n2)
del n2[5:8]
print(n2)
'''

''''''
#循环
n2 = [1,2,3,4,5,6]
## for循环
for i in n2:
    print(i)