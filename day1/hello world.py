#!/usr/bin/env python
# -*- coding:utf-8 -*-

count = 0
while count < 10:
    print("loop",count)
    if count == 3:
        count += 1
        continue
    count += 1