#!/usr/bin/env python
# -*- coding:utf-8 -*-
import login,json

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

def main():
    f = open("test.json","r+")
    info = json.load(f)
    f.close()
    totalPrice = 0
    real_price = 0
    car = {}
    username = login.login()
    if username in info.keys():
         print(info)
         old_car = info[username]['prodcuts']
         balance = info[username]['balance']
         # print(car,balance)
         asset_all = balance
         prodcuts = {
             "prodcuts": car,
             "prodcuts": balance
         }
         shopping(username, asset_all, car, totalPrice, prodcuts, info, real_price,old_car)
    else:
        print("waitting...")

    return car,asset_all,totalPrice,prodcuts,username,totalPrice,info,real_price,old_car


def shopping(username,asset_all,car,totalPrice,prodcuts,info,real_price,old_car):
    while True:
        for k, v in enumerate(goods, 1):
            print(k, v["name"], v["price"])

        choice = input("请输入要购买的商品编号：")
        if choice.lower() == "q":
            checkout(username, car, asset_all, prodcuts, info, real_price,old_car)
            break
        elif choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= 4:
                if choice in car.keys():
                    renum = car[choice].get("number")
                    get = {choice: {"name": name, "price": price, "number": renum + 1}}
                    totalPrice += get[choice]["price"]
                    if totalPrice < asset_all:
                        print("\033[42;35m成功添加[%s]到购物车。\033[0m" % (get[id]["name"]))
                        car.update(get)
                    else:
                        print("\033[41;1m余额不足，无法购买！余额：[%s]\033[0m" % (asset_all - totalPrice))
                else:
                    name = goods[choice - 1].get("name")
                    price = goods[choice - 1].get("price")
                    get = {choice: {"name": name, "price": price, "number": 1}}
                    totalPrice += get[choice]["price"]
                    if totalPrice < asset_all:
                        print("\033[42;35m成功添加[%s]到购物车。\033[0m" % (get[choice]["name"]))
                        car.update(get)
                    else:
                        print("\033[41;1m余额不足，无法购买！余额：[%s]\033[0m" % (asset_all - totalPrice))
            else:
                print("商品不存在！")

def checkout(username,car,asset_all,prodcuts,info,real_price,old_car):
    print("---------- 结算 ----------")
    for k, v in car.items():
        print(v["name"], "\t", v["price"], "\t", v["number"])
        p = v["price"] * v["number"]
        real_price += p

    print("商品总价：", real_price)
    balance = asset_all - real_price
    print("账户余额：", balance)
    prodcuts["balance"] = balance
    prodcuts["prodcuts"].update(old_car)

    info = {
        username: prodcuts,
    }

    print(info)
main()