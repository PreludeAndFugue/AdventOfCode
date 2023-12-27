
from fractions import Fraction
from itertools import combinations

from help import get_input

'''
y1 = m*x1 + c
y2 = m*x2 + c

y2 - y1 = m(x2 - x1)
dy = m*dx
m = dy/dx
c = y - dy/dx*x

Input data has dx != 0 for all cases.
'''

TEST = '''
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
'''

MIN_TEST = 7
MAX_TEST = 27
MIN = 200000000000000
MAX = 400000000000000


class Hailstone:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.m = Fraction(dy, dx)
        self.c = y - self.m*x

    def intersection(self, other):
        if self.m == other.m:
            if self.c == other.c:
                # This point is not in the past for this hailstone, but it could be for
                # the other hailstone.
                return self.x, self.y
            else:
                return None
        dm = self.m - other.m
        x = (other.c - self.c)/dm
        y = (other.c*self.m - self.c*other.m)/dm
        return x, y

    def point_in_past(self, x, y):
        if x < self.x and self.dx > 0:
            return True
        if x > self.x and self.dx < 0:
            return True
        if y < self.y and self.dy > 0:
            return True
        if y > self.y and self.dy < 0:
            return True
        return False


def parse(d):
    for line in d.strip().split('\n'):
        p, v = line.split(' @ ')
        x, y, _ = tuple(map(int, p.split(', ')))
        dx, dy, _ = tuple(map(int, v.split(', ')))
        yield Hailstone(x, y, dx, dy)


def main():
    d = get_input('24')
    # d = TEST.strip()
    hs = list(parse(d))

    MA = MAX
    MI = MIN

    total = 0
    for h1, h2 in combinations(hs, 2):
        i = h1.intersection(h2)
        if i is None:
            continue
        x, y = i
        if h1.point_in_past(x, y):
            continue
        if h2.point_in_past(x, y):
            continue
        if x < MI or x > MA:
            continue
        if y < MI or y > MA:
            continue
        total += 1
    print(total)


if __name__ == '__main__':
    main()
