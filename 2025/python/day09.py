from itertools import combinations

from help import get_input

TEST01 = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

source = TEST01.strip()
source = get_input(9)


def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def part1():
    ps = []
    for line in source.split('\n'):
        p = tuple(map(int, line.split(',')))
        ps.append(p)
    a = 0
    for p1, p2 in combinations(ps, 2):
        a = max(a, area(p1, p2))
    return a


if __name__ == '__main__':
    p1 = part1()
    print(p1)
