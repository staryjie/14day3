#!/usr/bin/env python
# -*- coding:utf-8 -*-

## 字典的详细方法
'''
info = {
    "stu1101":"TengLan Wu",
    "stu1102":"LongZe Luola",
    "stu1103":"XiaoZe Maliya",
}

### 增加

info["stu1104"] = "JingKong Cang"
print(info)

### 修改
info["stu1101"] = "武藤兰"
print(info)

### 查找

print("stu1102" in info)

### 获取
print(info.get("stu1102"))
print(info.get("stu1111"))
print(info["stu1101"])
# print(info["stu1111"]) ## 如果没有会报错


### 删除
res = info.pop("stu1101") # 删除指定的
print(res,info)

info.popitem() # 随机删除
print(info)

del info["stu1101"]
'''

#### 多级字典的嵌套

menu = {
    '山东': {
        '青岛': ['四方', '黄岛', '崂山', '李沧', '城阳'],
        '济南': ['历城', '槐荫', '高新', '长青', '章丘'],
        '烟台': ['龙口', '莱山', '牟平', '蓬莱', '招远']
    },
    '江苏': {
        '苏州': ['沧浪', '相城', '平江', '吴中', '昆山'],
        '南京': ['白下', '秦淮', '浦口', '栖霞', '江宁'],
        '无锡': ['崇安', '南长', '北塘', '锡山', '江阴']
    },
    '浙江': {
        '杭州': ['西湖', '江干', '下城', '上城', '滨江'],
        '宁波': ['海曙', '江东', '江北', '镇海', '余姚'],
        '温州': ['鹿城', '龙湾', '乐清', '瑞安', '永嘉']
    },
    '安徽': {
        '合肥': ['蜀山', '庐阳', '包河', '经开', '新站'],
        '芜湖': ['镜湖', '鸠江', '无为', '三山', '南陵'],
        '蚌埠': ['蚌山', '龙子湖', '淮上', '怀远', '固镇']
    },
    '广东': {
        '深圳': ['罗湖', '福田', '南山', '宝安', '布吉'],
        '广州': ['天河', '珠海', '越秀', '白云', '黄埔'],
        '东莞': ['莞城', '长安', '虎门', '万江', '大朗']
    }
}

### keys()
for key in menu.keys():
    print(key)

#values()
for value in menu.values():
    print(value)

#items()
for k,v in menu.items():
    print(k,v)

#update()
dict1 = {
    "alex":[24,"it"],
    "jack":22,
    "rain":[19,"NT"],
}

dict2 = {
    1:2,
    2:3,
    "jack":[22,"Jack Ma","Alibaba CEO"]
}
dict1.update(dict2)
print(dict1)