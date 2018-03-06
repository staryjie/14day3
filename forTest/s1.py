#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
products = [['iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
car = []

car.insert(0,products[1])
car.insert(0,products[0])
car.insert(0,products[2])
print(len(products))
for j in range(len(products)):
    print(j)
for i in range(len(car)):
    print(str(i) + "." + car[i][0] + "     " + str(car[i][1]))
'''

'''
names = ['old_driver', 'rain', ['oldby', 'oldgirl'], 'jack', '姗姗', 'peiqi', 'alex', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]
for i,j in enumerate(names):
    print(i,j)
'''

products = [['iphone8',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
print("---------- 商品列表 ----------")
for index,i in enumerate(products):
    print(str(index) + "."+ str(i[0])+"    "+ str(i[1]))