#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json,hashlib

def lock(users):
    #将login()函数中修改账户状态的users字典传入该函数，该函数负责持久化数据
    f = open("user.json", "wb+")
    f.write(bytes(json.dumps(users), encoding="utf-8"))
    f.close()

def md5(passwd):
    '''
    实现用户密码的MD5加密
    :param passwd: 传入参数，用户输入的密码
    :return: 返回值，返回加密后的密文
    '''
    hash = hashlib.md5(bytes("staryjie", encoding="utf-8"))
    hash.update(bytes(passwd, encoding="utf-8"))
    return hash.hexdigest()

def login():
    #读取json文件中的账户信息，放到users字典中
    f = open("user.json", "rb+")
    users = json.load(f)

    #count计数，错误达3次锁定账户
    count = 0
    while True:
        if count == 3:
            #将账户是否锁定状态更新为True
            users[username]["isLocked"] = True
            #调用锁定账户函数，持久化到文件中
            lock(users)
            print("Error up to 3 times, the account is locked!")
            break
        username = input("Pls enter your username: ")
        password = md5(input("Pls enter your password: "))

        #判断用户名是否在json文件中
        if username in users.keys():
            #判断该用户账户是否已经被锁定
            if users[username]["isLocked"] != True:
                passwd = users[username]["password"]
            else:
                print("Account has been locked!")
                break
            if password == passwd:
                print("Welcome %s !" % username)
                break
            else:
                print("The password is error!")
                count += 1
                # print(count)
        else:
            print("No such username!")
    f.close()
    return username


# 调用登陆函数
# login()