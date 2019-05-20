def max2(arr):
    _max = 0
    _max_2 = 0
    for x in arr:
        if _max < x:
            _max_2 = _max
            _max = x
        else:
            if _max_2 < x != _max:
                _max_2 = x
    return [_max, _max_2]


test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test1 = [1, 2, 3, 4, 5, 6, 8, 9, 9]

print(max2(test))
print(max2(test1))
