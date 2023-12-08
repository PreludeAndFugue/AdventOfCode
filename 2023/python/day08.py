
from math import lcm
from itertools import cycle

from help import get_input

TEST1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''

TEST2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''

NS = {'L': 0, 'R': 1}

def parse(d):
    directions, b = d.split('\n', maxsplit=1)
    directions = directions.strip()

    m = {}
    for l in b.strip().split('\n'):
        p = l.split(' = ')
        x, y = p[0], p[1]
        y = y.replace('(', '')
        y = y.replace(')', '')
        y = y.split(', ')
        m[x] = y
    return directions, m


def part1(directions, m, start, endf):
    p = start
    for i, d in enumerate(cycle(directions), start=1):
        n = NS[d]
        p = m[p][n]
        if endf(p):
            return i


def part2(directions, m):
    starts = [m for m in m.keys() if m.endswith('A')]
    l = 1
    for p in starts:
        c = part1(directions, m, p, lambda p: p.endswith('Z'))
        l = lcm(l, c)
    return l


def main():
    d = get_input('08').strip()
    # d = TEST1.strip()
    # d = TEST2.strip()

    directions, m = parse(d)

    p1 = part1(directions, m, 'AAA', lambda p: p == 'ZZZ')
    print(p1)

    p2 = part2(directions, m)
    print(p2)


if __name__ == '__main__':
    main()
