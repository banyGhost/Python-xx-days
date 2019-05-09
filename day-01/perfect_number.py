"""
寻找1-9999之间所有的完美数
"""
from functools import reduce


def perfect_num():
    L = []
    for x in range(1, 10000):
        L1 = []
        for y in range(1, x):
            if x % y == 0:
                L1.append(y)
        if len(L1) != 0 and reduce(lambda m, n: m + n, L1) == x:
            L.append(x)
    return L


print(perfect_num())
