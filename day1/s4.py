#!/usr/bin/env python
# -*- coding:utf-8 -*-

#列表练习题

#1.创建一个空列表，命名为names，往里面添加old_driver,rain,jack,shanshan,peiqi,black_girl 元素

names = []
names.append("old_driver")
names.append("rain")
names.append("jack")
names.append("shanshan")
names.append("peiqi")
names.append("black_girl")
print(names)

#2.在names列表里black_girl前面插入一个alex

names.insert(names.index("black_girl"),"alex")
print(names)

#3.把shanshan的名字改成中文，姗姗

names[names.index("shanshan")] = "姗姗"
print(names)

#4.往names列表rain的后面插入一个子列表，[oldby,oldgirl]

list = ['oldby','oldgirl']
names.insert((names.index('rain')+1),list)
print(names)

#5.返回peiqi的索引值

print(names.index('peiqi'))

#6.创建新列表[1,2,3,4,2,5,6,2]，合并入names列表

list1 = [1,2,3,4,2,5,6,2]
names.extend(list1)
print(names)

#7.取出names列表中索引4-7的元素

print(names[4:8])

#8.取出names列表中索引2-10的元素，步长为2

print(names[2:10:2])

#9.取出names列表中最后三个元素

print(names[-3:])

#10.循环names列表，打印每个元素的索引和元素

for i in range(len(names)):
    print(i,names[i])

##10 方法二 枚举方法
for index,i in enumerate(names):
    print(index,i)

#11.循环names列表，打印每个元素的索引和元素,当索引为偶数时，把对应的元素改为-1

for i in range(len(names)):
    if i % 2 == 0:
        names[i] = -1
    print(i,names[i])

## 方法2
first_index = names.index(2)
new_names = names[(first_index + 1):]
print(new_names.index(2))

#12.names列表中有三个2，请返回第二个2的索引值；不要人肉数，要动态找（提示，找到第一个2的位置，在此基础上再找第二个2）

names = ['old_driver', 'rain', ['oldby', 'oldgirl'], 'jack', '姗姗', 'peiqi', 'alex', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]
# count = 0
# i = 0
# while i < len(names):
#     if names[i] == 2:
#         count +=1
#         if count == 2:
#             print("第二个2元素的索引为：" + str(i))
#             break
#     i += 1
for i in range((names.index(2) + 1),len(names)):
    if names[i] == 2:
        print("第二个2元素的索引为：" + str(i))
        break

#13.格式化输出列表中的内容

products = [['iphone8',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
print("---------- 商品列表 ----------")
for i in range(len(products)):
    print(str(i)+"."+products[i][0]+ "     "+ str(products[i][1]))

## 方法二
products = [['iphone8',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
print("---------- 商品列表 ----------")
for index,i in enumerate(products):
    print(str(index) + "."+ str(i[0])+"    "+ str(i[1]))

# 14.循环询问用户需要购买什么，用户输入编号，把对应的商品加入购物车，用户输入q时退出循环，打印购物车里的商品列表
products = [['iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
car = []

while True:
    print("---------- 商品列表 ----------")
    for index, i in enumerate(products):
        print(str(index) + "." + str(i[0]) + "    " + str(i[1]))

    choice = input("请输入您需要购买的商品编号(q/Q退出)：")
    if choice.lower() == 'q':
        print("退出...")
        break
    if choice.isdigit() and  int(choice) in range(len(products)):
        choice = int(choice)
        car.insert(0, products[choice])
        print("Added product %s into shopping cart." % (products[choice]))
print("购物车中有以下商品：")
for i in range(len(car)):
    print(str(i) + "." + car[i][0] + "     " + str(car[i][1]))