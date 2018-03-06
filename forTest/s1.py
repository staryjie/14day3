#!/usr/bin/env python
# -*- coding:utf-8 -*-
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