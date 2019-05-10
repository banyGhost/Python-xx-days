# 判断一个数是否是回文数


def is_palindrome(n):
    m = str(n)
    for x in range(len(m) // 2):
        if m[x] != m[-(x + 1)]:
            return False
    return True


def is_palindrome2(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
