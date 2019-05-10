# 最大公约数和最小公倍数的计算


def gcd(m, n):
    (m, n) = (n, m) if m > n else (m, n)
    for x in range(m, 0, -1):
        if m % x == 0 and n % x == 0:
            return x


def lcm(m, n):
    return m * n // gcd(m, n)


print(gcd(78, 54))

print(lcm(78, 54))
