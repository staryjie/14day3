#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 14.循环询问用户需要购买什么，用户输入编号，把对应的商品加入购物车，用户输入q时退出循环，打印购物车里的商品列表
products = [['iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
car = []
print("---------- 商品列表 ----------")
for i in range(len(products)):
    print(str(i) + "." + products[i][0] + "     " + str(products[i][1]))
while True:
    choice = input("请输入您需要购买的商品编号(q/Q退出)：")
    if choice.lower() == 'q':
        print("退出...")
        break
    if int(choice) in range(len(products)):
        car.insert(0, products[int(choice)])
print("购物车中有以下商品：")
for i in range(len(car)):
    print(str(i) + "." + car[i][0] + "     " + str(car[i][1]))
