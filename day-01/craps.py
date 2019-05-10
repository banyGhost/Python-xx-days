#
from random import randrange


def ready():
    count = 0

    def get_point():
        nonlocal count
        count += 1
        return {
            'count': count,
            'point': randrange(1, 7) + randrange(1, 7)
        }

    return get_point


def craps():
    point = 0

    round = ready()

    def play():
        nonlocal point
        res = round()
        # print('count', res['count'], 'point', res['point'])
        if res['count'] == 1:
            point = res['point']
            if res['point'] == 7 or res['point'] == 11:
                return 'win'
            elif res['point'] == 2 or res['point'] == 3 or res['point'] == 12:
                return 'lost'
            else:
                return play()
        else:
            if res['point'] == point:
                return 'win'
            elif res['point'] == 7:
                return 'lost'
            else:
                return play()

    return play()


for x in range(1, 100):
    print(craps())
