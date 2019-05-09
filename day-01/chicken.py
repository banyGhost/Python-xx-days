# 5 3 1/3 100
def get_num():
    result = []
    for x in range(0, 20):
        for y in range(0, 34):
            if 5 * x + 3 * y + (100 - x - y) * 1 / 3 == 100:
                result.append({
                    'x': x,
                    'y': y,
                    'z': (100 - x - y)
                })
    return result


print(get_num())
