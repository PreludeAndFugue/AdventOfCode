#!python3

from collections import Counter

from helpers import BASE

TEST01 = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''


def parse(text):
    for line in text.strip().split('\n'):
        p1, p2 = line.split(' -> ')
        p1 = tuple(map(int, p1.split(',')))
        p2 = tuple(map(int, p2.split(',')))
        yield p1, p2


def make_range(diff):
    if diff > 0:
        return range(diff + 1)
    elif diff < 0:
        return range(0, diff - 1, -1)
    else:
        return None


def point_range(p1, p2, part1=True):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    rx = make_range(dx)
    ry = make_range(dy)
    if dy == 0:
        for x in rx:
            yield p1[0] + x, p1[1]
    elif dx == 0:
        for y in ry:
            yield p1[0], p1[1] + y
    elif abs(dx) == abs(dy):
        if part1:
            return
        for x, y in zip(rx, ry):
            yield p1[0] + x, p1[1] + y
    else:
        print('Invalid range', p1, p2)


def part(pairs, part1=True):
    counter = Counter()
    for p1, p2 in pairs:
        points = point_range(p1, p2, part1)
        counter.update(points)
    s = sum(1 for _, count in counter.items() if count >= 2)
    return s


def main():
    test_pairs = list(parse(TEST01))
    pairs = list(parse(open(BASE + 'day05.txt', 'r').read()))

    t1 = part(test_pairs)
    assert t1 == 5

    p1 = part(pairs)
    print(f'Part 1: {p1}')

    t2 = part(test_pairs, part1=False)
    assert t2 == 12

    p2 = part(pairs, part1=False)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
