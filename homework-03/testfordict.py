#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import json
#
# f = open("info.json","r+")
# info = json.load(f)
# f.close()
# print(info)

info = {
    "user1": {
        "prodcuts": {
            "1": {"name": "\u7535\u8111", "price": 1999, "number": 1},
            "2": {"name": "\u9f20\u6807", "price": 10, "number": 1},
            "3": {"name": "\u6e38\u8247", "price": 20, "number": 1},
            "4": {"name": "\u7f8e\u5973", "price": 998, "number": 1},
        },
        "balance": 16973,
    }
}

info_new = {
    "user2": {
        "prodcuts": {
            "1": {"name": "\u7535\u8111", "price": 1999, "number": 1},
            "2": {"name": "\u9f20\u6807", "price": 10, "number": 1},
        },
        "balance": 20000,
    }
}

info.update(info_new)
print(info)

rest = {
    'user1': {
        'prodcuts': {
            '1': {'name': '电脑', 'price': 1999, 'number': 1},
            '2': {'name': '鼠标', 'price': 10, 'number': 1},
            '3': {'name': '游艇', 'price': 20, 'number': 1},
            '4': {'name': '美女', 'price': 998, 'number': 1},
        },
        'balance': 16973,
    },
    'user2': {
        'prodcuts': {
            '1': {'name': '电脑', 'price': 1999, 'number': 1},
            '2': {'name': '鼠标', 'price': 10, 'number': 1},
        },
        'balance': 20000,
    }
}


three = {
    "user1": {
        "prodcuts": {
            "2": {"name": "\u9f20\u6807", "price": 10, "number": 1},
            "1": {"name": "\u7535\u8111", "price": 1999, "number": 1},
        },
        "balance": 17991,
    }
}

his_car = {
    "1": {
        "name": "电脑",
        "price": 1999,
        "number": 1,
    }
}
car = {
    "1": {
        "name": "电脑",
        "price": 1999,
        "number": 1,
    }
}
for k in car.keys():
    if k in his_car.keys():
        his_car[k]["number"] += 1
print(his_car)