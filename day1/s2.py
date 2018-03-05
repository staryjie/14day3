#!/usr/bin/env python
# -*- coding:utf-8 -*-
from decimal import *


'''
python中浮点数默认17位，即16位小数

需要高精度的浮点数，需要借助decimal模块
'''
n = 1.444427374434567987567898567987678098567
print(n)
a = Decimal(4)/Decimal(7)
print(a)