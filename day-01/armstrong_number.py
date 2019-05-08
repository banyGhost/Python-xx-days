#!/usr/bin/env ptyhon3
# -*- coding: utf-8 -*-
from functools import reduce


def armstrong(m):
    sum = 0
    for x in str(m):
        sum = sum + int(x) ** 3
    return sum


def armstrong_num():
    l = []
    for x in range(100, 1000):
        sum = armstrong(x)
        if sum == x:
            l.append(x)
    return l


print(armstrong_num())
