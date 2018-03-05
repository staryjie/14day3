#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib,json


def md5(passwd):
    '''
    实现用户密码的MD5加密
    :param passwd: 传入参数，用户输入的密码
    :return: 返回值，返回加密后的密文
    '''
    hash = hashlib.md5(bytes("staryjie", encoding="utf-8"))
    hash.update(bytes(passwd, encoding="utf-8"))
    return hash.hexdigest()

def writeIn(users):
    f = open("user.json", "wb+")
    f.write(bytes(json.dumps(users), encoding="utf-8"))
    f.close()

def lock(users):
    #将login()函数中修改账户状态的users字典传入该函数，该函数负责持久化数据
    f = open("user.json", "wb+")
    f.write(bytes(json.dumps(users), encoding="utf-8"))
    f.close()

def register(username, passwd):
    '''
    实现用户注册功能，有待完善检查用户名是否已经存在的功能
    :param username:用户名
    :param passwd:用户输入的密码
    :return:返回知否注册成功
    '''

    f = open("user.json", "rb+")
    users = json.load(f)
    f.close()
    if username in users.keys():
        print("This username has been used!")
        return False
    else:
        user = {
            username : {
                "password" : md5(passwd),
                "isLocked" : True,
            }
        }
        users.update(user)
        writeIn(users)
        return True

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
    return users

def main():
    '''
    主函数，实现用户登录和注册的选择
    :return:
    '''
    print("1.登陆；2.注册")
    num = input("请输入对应的序号： ")
    if num == "2":
        username = input("用户名：")
        passwd = input("密码：")
        register(username, passwd)
    elif num == "1":
        login()
    else:
        print("没有该选项！")

main()