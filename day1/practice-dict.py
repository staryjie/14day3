#!/usr/bin/env python
# -*- coding:utf-8 -*-

#字典练习题
dic = { "k1":"v1","k2":"v2","k3":"v3" }

#1.循环遍历出所有的key
for key in dic.keys():
    print(key)

#2.循环遍历出所有的value
for value in dic.values():
    print(value)

#3.循环遍历出所有的key和value
for k,v in dic.items():
    print(k,v)

#4.在字典中添加"k4":"v4"，并输出添加后的字典
dic["k4"] = "v4"
print(dic)

#5.删除字典中"k1","v1",并输出删除后的字典
dic.pop("k1")
print(dic)

#6.删除"k5"对应的键值对，如果不存在则不报错，并让其返回None
if "k5" in dic.keys():
    dic.pop("k5")
    print(dic)
else:
    print("None")

#7.获取"k2"对应的值
print(dic.get("k2"))

#8.获取"k6"对应的键值对，如果不存在则不报错，并让其返回None
if "k6" in dic.keys():
    print(dic.get("k6"))
else:
    print("None")

#9.合并两个字典
dic1 = { "k1":"v1","k2":"v2","k3":"v3" }
dic2 = {"k1":"v111","a":"b"}
dic2.update(dic1)
print(dic2)

#10.
lis = [["k",["qwe",20,{"k1":["tt",3,"1"]},89],"ab"]]

#10.1 将lis中的"tt"变成大写（2种方法）

###### 方法一
# print(type(lis[0][1][2]["k1"][0]))
lis[0][1][2]["k1"][0] = "TT"
# print(lis[0][1][2]["k1"][0])
print(lis)

###### 方法二
dic3 = {"k1":["TT",3,"1"]}
lis[0][1][2].update(dic3)
print(lis)


#10.2将列表中的数字3，变成字符串100（两种方式）

###### 方法二
lis[0][1][2]["k1"][1] = "100"
print(lis)
###### 方法二
dic4 = {"k1":["TT","100","1"]}
lis[0][1][2].update(dic4)
print(lis)


#10.3将列表中的字符串“1”，变成数字101,（两种方法）

###### 方法一
lis[0][1][2]["k1"][2] = 101
print(lis)

###### 方法二
dic5 = {"k1":["TT",3,101]}
lis[0][1][2].update(dic5)
print(lis)

#11.
li = [1,2,3,"a","b",4,"c"]
dic = {}

#如果字典中没有"k1"这个键，则添加一个"k1":[]，并将li中索引位为奇数的元素添加到"k1"对应的空列表中。
#如果字典中有"k1"这个键，且"k1"对应的value是列表类型，将li中索引位为奇数的元素添加到"k1"对应的空列表中。

if "k1" not in dic.keys():
    dic["k1"] = []
    for k,v in enumerate(li):
        if k / 2 != 0:
            dic["k1"].append(v)
else:
    if isinstance(dic["k1"],list):
        for k, v in enumerate(li):
            if k / 2 != 0:
                dic["k1"].append(v)
print(dic)