import random


def getVerifyCode(l=4):
    str = '12345678990abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    verifyCode = ''
    for x in range(l):
        verifyCode += str[random.randrange(0, len(str), 1)]
    return verifyCode


print(getVerifyCode())
