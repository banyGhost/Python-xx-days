# 判断是否是素数


def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    # 考虑1的特殊情况
    return True if num != 1 else False
