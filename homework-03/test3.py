#!/usr/bin/env python
# -*- coding:utf-8 -*-
import login,json,sys

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
asset_all = 0
totalPrice = 0
real_price = 0
balance = 0
his_car = {}
his_total = 0
car = {}
username = login.login()
prodcuts = {
    "prodcuts":car,
    "prodcuts":balance
}
info = {
    username:prodcuts,
}

f = open("test.json", "r+")
info = json.load(f)
f.close()

def write_in(info):
    f = open("test.json", "wb+")
    f.write(bytes(json.dumps(info), encoding="utf-8"))
    f.close()

def shopping(real_price,totalPrice):
    while True:
        for k, v in enumerate(goods, 1):
            print(k, v["name"], v["price"])

        id = input("请输入商品序号(q/Q结算)：")
        if id.lower() == "q":
            print("结算：")
            print("商品\t单价\t数量")
            for k, v in car.items():
                print(v["name"], "\t", v["price"], "\t", v["number"])
                p = v["price"] * v["number"]
                real_price += p

            print("商品总价：", real_price)
            balance = asset_all - real_price
            print("账户余额：", balance)
            prodcuts["balance"] = balance
            car.update(his_car)
            prodcuts["prodcuts"] = car
            info_new = {
                username:prodcuts,
            }
            info.update(info_new)
            write_in(info)
            sys.exit()
        id = int(id)
        if id > 0 and id <= 4:
            if id in car.keys():
                renum = car[id].get("number")
                get = {id: {"name": name, "price": price, "number": renum + 1}}
                totalPrice += get[id]["price"]
                print(totalPrice)
                print(asset_all - totalPrice)
                if totalPrice <= asset_all:
                    print("\033[42;35m成功添加[%s]到购物车。\033[0m" % (get[id]["name"]))
                    if str(id) in his_car.keys():
                        his_car[str(id)]["number"] += 1
                        print(his_car[str(id)]["number"])
                    car.update(get)
                else:
                    print("\033[41;1m余额不足，无法购买！余额：[%s]\033[0m" % (asset_all - totalPrice))
            else:
                name = goods[id - 1].get("name")
                price = goods[id - 1].get("price")
                get = {id: {"name": name, "price": price, "number": 1}}
                totalPrice += get[id]["price"]
                if totalPrice <= asset_all:
                    print("\033[42;35m成功添加[%s]到购物车。\033[0m" % (get[id]["name"]))
                    if str(id) in his_car.keys():
                        his_car[str(id)]["number"] += 1
                        print(his_car[str(id)]["number"])
                    car.update(get)
                else:
                    print("\033[41;1m余额不足，无法购买！余额：[%s]\033[0m" % (asset_all - totalPrice))
        else:
            print("商品不存在！")

if username in info.keys():
    his_car = info[username]['prodcuts']
    asset_all = info[username]['balance']
    print("欢迎再次光临，您的历史购物记录如下：")
    print("商品\t单价\t数量")
    for k, v in his_car.items():
        print(v["name"], "\t", v["price"], "\t", v["number"])
        p = v["price"] * v["number"]
        his_total += p
    print("历史购物共计 %s 元，余额 %s 元。"%(his_total,asset_all))
    print("----------------------------")
    print("")

    shopping(real_price, totalPrice)
else:
    asset_all = input("请输入您的总资产：")
    if asset_all.isdigit():
        asset_all = int(asset_all)
    else:
        print("输入有误，请输入数字！")

shopping(real_price,totalPrice)