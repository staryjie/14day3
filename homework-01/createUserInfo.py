#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

#创建用户账户信息
users = {
    "user1":{
        "password":"3580b5fda8e926c345fdbc2e2f99886c",
        "isLocked":False,
    },
    "user2":{
        "password": "3580b5fda8e926c345fdbc2e2f99886c",
        "isLocked": False,
    },
    "user3":{
        "password": "3580b5fda8e926c345fdbc2e2f99886c",
        "isLocked": False,
    }
}
f = open("user.json","wb")
f.write(bytes(json.dumps(users),encoding="utf-8"))
f.close()