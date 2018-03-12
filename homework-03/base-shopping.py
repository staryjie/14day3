#!/usr/bin/env python
# -*- coding:utf-8 -*-
import login

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

username = login.login()
car = {}
totalPrice = 0
real_price = 0
asset_all = 0
balance = 0

prodcuts = {
    "prodcuts":car,
    "prodcuts":balance
}
info = {
    username:prodcuts,
}

asset_all = input("请输入您的总资产：")
if asset_all.isdigit():
    asset_all = int(asset_all)
    print("总资产为：",asset_all)
else:
    print("请输入数字！")

while True:
    for k,v in enumerate(goods,1):
        print(k,v["name"],v["price"])

    id = input("请输入商品序号(q/Q结算)：")
    if id.lower() == "q":
        break
    id = int(id)
    if id > 0 and id <= 4:
        if id in car.keys():
            renum = car[id].get("number")
            get = {id:{"name":name,"price":price,"number":renum+1}}
            totalPrice += get[id]["price"]
            print(totalPrice)
            print(asset_all - totalPrice)
            if totalPrice < asset_all:
                print("\033[42;35m成功添加[%s]到购物车,余额还剩[%s]\033[0m" % (get[id]["name"],asset_all - totalPrice))
                car.update(get)
            else:
                print("\033[41;1m余额不足，无法购买！余额：[%s]\033[0m" %(asset_all - totalPrice))
        else:
            name = goods[id -1].get("name")
            price = goods[id -1].get("price")
            get = {id:{"name":name,"price":price,"number":1}}
            totalPrice += get[id]["price"]
            if totalPrice < asset_all:
                print("\033[42;35m成功添加[%s]到购物车,余额还剩[%s]\033[0m" % (get[id]["name"], asset_all - totalPrice))
                car.update(get)
            else:
                print("\033[41;1m余额不足，无法购买！余额：[%s]\033[0m" %(asset_all - totalPrice))
    else:
        print("商品不存在！")

print("结算：")
print("商品\t单价\t数量")
for k,v in car.items():
    print(v["name"],"\t",v["price"],"\t",v["number"])
    p = v["price"] * v["number"]
    real_price += p

print("商品总价：",real_price)
print("账户余额：",(asset_all - real_price))