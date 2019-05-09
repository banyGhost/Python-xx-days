#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__name = 'Bert'


def fib(n):
    L = []
    while True:
        if len(L) == 0 or len(L) == 1:
            L.append(1)
        else:
            L.append(L[-1] + L[-2])
        if len(L) == n:
            break
    return L


print(fib(10))
