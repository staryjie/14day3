#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import login

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

car = {}
totalPrice = 0
real_price = 0
balance = 0

prodcuts = {
    "prodcuts":car,
    "prodcuts":balance
}

def load_info():
    f = open("test.json","r+")
    info = json.load(f)
    f.close()
    check(info,prodcuts)
    return info

def check(info,products):
    username = login.login()
    if username in info.keys():
        print(info)
        car = info[username]['prodcuts']
        balance = info[username]['balance']
        judge(car, balance, username, products)
    else:
        print("你没有任何购买记录！")
        car = {}
        balance = 0
    return car,balance,username

def generate_information(username,products):
    info = {
        username: prodcuts,
    }
    return info

def judge(car,balance,username,products):
    if balance == 0:
        asset_all = input("请输入您的总资产：")
        if asset_all.isdigit():
            asset_all = int(asset_all)
            car = car
            shopping(asset_all, car, totalPrice, username, products)
        else:
            print("请输入数字！")
    else:
        asset_all = balance
        car = car
        shopping(asset_all, car, totalPrice, username, products)
    return asset_all,car

def shopping(asset_all,car,totalPrice,username,products):
    while True:
        for k, v in enumerate(goods, 1):
            print(k, v["name"], v["price"])

        choice = input("请输入要购买的商品编号：")
        if choice.lower() == "q":
            clearing(real_price, asset_all, car, username, products,info)
            break
        elif choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= 4:
                if choice in car.keys():
                    renum = car[id].get("number")
                    get = {choice: {"name": name, "price": price, "number": renum + 1}}
                    totalPrice += get[id]["price"]
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

def clearing(real_price,asset_all,car,username,products,info):
    for k, v in car.items():
        print(v["name"], "\t", v["price"], "\t", v["number"])
        p = v["price"] * v["number"]
        real_price += p

    print("商品总价：", real_price)
    balance = asset_all - real_price
    print("账户余额：", balance)
    prodcuts["balance"] = balance
    prodcuts["prodcuts"] = car
    generate_information(username, products)
    # print(car)
    # print(info)
    write_in(info)

def write_in(info):
    f = open("info.json", "ab+")
    f.write(bytes(json.dumps(info), encoding="utf-8"))
    f.close()


info = load_info()
