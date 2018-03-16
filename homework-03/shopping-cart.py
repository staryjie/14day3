#!/usr/bin/env python
# -*- coding:utf-8 -*-
import login,json,sys

# 商品列表
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

asset_all = 0 #总资产
totalPrice = 0 #购物总花费，用于在加入购物车的时候判断是否超过总资产
real_price = 0 #真正购买的花费，因为totalPrice只是拿来判断是否超过总资产，当超过总资产时，totalPrice并不是你真正能购买的物品的总价
balance = 0 # 账户余额
his_car = {} #历史购物记录
his_total = 0 # 历史购物总费用
car = {} # 购物过程中的购物车（能够真正购买的）

username = login.login() #调用之前的用户登陆作业，实现用户登陆和锁定

# 产品字典，用于将存储已购买的商品信息
prodcuts = {
    "prodcuts":car,
    "prodcuts":balance
}
#通过username当key来存储不同用户的购买信息，持久化到文件中（再次打开就是用户的历史购买信息）
info = {
    username:prodcuts,
}
# 读取之前持久化的数据，可以用来判断用户是否有过购买记录
f = open("info.json", "r+")
info = json.load(f)
f.close()

# 定义持久化数据的函数
def write_in(info):
    f = open("info.json", "wb+")
    f.write(bytes(json.dumps(info), encoding="utf-8"))
    f.close()

#定义购物函数，实现商品添加到购物车的所有流程
def shopping(real_price,totalPrice,his_car):
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
            info_new = {username:prodcuts,}
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

    shopping(real_price, totalPrice,his_car)
else:
    asset_all = input("请输入您的总资产：")
    if asset_all.isdigit():
        asset_all = int(asset_all)
    else:
        print("输入有误，请输入数字！")

shopping(real_price,totalPrice,his_car)