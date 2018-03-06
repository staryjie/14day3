#!/usr/bin/env python
# -*- coding:utf-8 -*-

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
        if len(car) > 0:
            print("购物车中有以下商品：")
            for i in range(len(car)):
                print(str(i) + "." + car[i][0] + "     " + str(car[i][1]))
        break
    if choice.isdigit() and  int(choice) in range(len(products)):
        choice = int(choice)
        car.insert(0, products[choice])
        print("Added product %s into shopping cart." % (products[choice]))
    else:
        print("输入有误！")
