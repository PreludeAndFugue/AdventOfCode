#!python3

from itertools import groupby


INPUT = '1113222113'


def look_and_say(sequence):
    result = []
    for k, g in groupby(sequence):
        g_items = list(g)
        result.append(str(len(g_items)))
        result.append(g_items[0])
    return ''.join(result)


if __name__ == '__main__':
    x = INPUT
    for _ in range(50):
        x = look_and_say(x)

    print('len x', len(x))
