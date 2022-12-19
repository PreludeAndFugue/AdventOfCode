from collections import Counter

from help import get_input
from day15 import parse, manhattan, TEST1


def get_c(x, y, m):
    '''
    Find c using x, y, m from y = mx + c
    c = y - mx
    '''
    return y - m*x


def intersection(l1, l2):
    m1, c1 = l1
    m2, c2 = l2
    dc1 = c2 - c1
    dc2 = c2 + c1
    assert dc1 % 2 == 0
    assert dc2 % 2 == 0
    x = dc1 // (m1 - m2)
    y = dc2 //2
    return x, y


def make_lines(s, b):
    '''
    Return pairs (m, c) of y = mx + c
    '''
    d = manhattan(s, b)
    x, y = s
    y1 = y + d + 1
    y2 = y - d - 1
    ms = (-1, 1)
    for yy in (y1, y2):
        for m in ms:
            yield m, yy - m*x


def part2():
    # x = get_input('15')
    x = TEST1.strip()

    sbs = list(parse(x))
    lines = []
    for s, b in sbs:
        for l in make_lines(s, b):
            lines.append(l)
    c = Counter(lines)
    l1, l2 = [line for (line, _) in c.most_common(2)]
    i = intersection(l1, l2)
    print(i)



def main():
    p2 = part2()

    print('Part 2:', p2)


if __name__ == '__main__':
    main()
