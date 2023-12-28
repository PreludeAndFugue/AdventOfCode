
from fractions import Fraction
from itertools import combinations

from sympy import Symbol, nonlinsolve

from help import get_input

'''
y1 = m*x1 + c
y2 = m*x2 + c

y2 - y1 = m(x2 - x1)
dy = m*dx
m = dy/dx
c = y - dy/dx*x

Input data has dx != 0 for all cases.

For part 1
----------

Use parametric equations for line:
x0 + dx0*t0 = x1 + dx1*t1
y0 + dy0*t0 = y1 + dy1*t1

x0, y0, dx0, dy0, x1, y1, dx1, dy1 are known.
Solve for t0 and t1.

For part 2
----------

P = (x, y, z) is position of stone at t = 0
V = (dx, dy, dz) is velocity of stone

Solve parametric equations. Three vector equations - or 9 equations in total.

P + V*T1 = p1 + v1*T1
P + V*T2 = p2 + v2*T2
P + V*T3 = p3 + v3*T3

p1 and v1 are position (at t = 0) and velocity of hailstone 1, etc.

Unknows P (3 variables), V (3 variables), T1, T2, and T3.

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
    def __init__(self, x, y, z, dx, dy, dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.m = Fraction(dy, dx)
        self.c = y - self.m*x

    def p(self, t):
        return self.x + t*self.dx, self.y + t*self.dy


def parse(d):
    for line in d.strip().split('\n'):
        p, v = line.split(' @ ')
        x, y, z = tuple(map(int, p.split(', ')))
        dx, dy, dz = tuple(map(int, v.split(', ')))
        yield Hailstone(x, y, z, dx, dy, dz)


def solve_for_t(h1, h2):
    n = (h2.x - h1.x)*h2.dy - (h2.y - h1.y)*h2.dx
    d = h1.dx*h2.dy - h2.dx*h1.dy
    if d == 0:
        return None
    t1 = Fraction(n, d)
    t2 = Fraction(h1.x - h2.x, h2.dx) + t1*Fraction(h1.dx, h2.dx)
    return t1, t2


def part1(hs):
    MA = MAX
    MI = MIN
    # MA = MAX_TEST
    # MI = MIN_TEST

    total = 0
    for h0, h1 in combinations(hs, 2):
        ts = solve_for_t(h0, h1)
        if ts is None:
            continue
        t0, t1 = ts
        if t0 < 0 or t1 < 0:
            continue
        x0, y0 = h0.p(t0)
        x1, y1 = h1.p(t1)
        if MI <= x0 <= MA and MI <= y0 <= MA and MI <= x1 <= MA and MI <= y1 <= MA:
            total += 1
    return total


def part2(hs):
    x = Symbol('x')
    dx = Symbol('dx')
    y = Symbol('y')
    dy = Symbol('dy')
    z = Symbol('z')
    dz = Symbol('dz')
    t1 = Symbol('t1')
    t2 = Symbol('t2')
    t3 = Symbol('t3')
    fs = []
    ts = (t1, t2, t3)
    for h, t in zip(hs[:3], ts):
        f1 = x + dx*t - h.x - h.dx*t
        fs.append(f1)
        f2 = y + dy*t - h.y - h.dy*t
        fs.append(f2)
        f3 = z + dz*t - h.z - h.dz*t
        fs.append(f3)

    vs = [x, y, z, dx, dy, dz, t1, t2, t3]

    solution = nonlinsolve(fs, vs)
    for result in solution:
        x, y, z, _, _, _, _, _, _ = result
    return x + y + z


def main():
    d = get_input('24')
    # d = TEST.strip()
    hs = list(parse(d))

    p1 = part1(hs)
    print(p1)

    p2 = part2(hs)
    print(p2)



if __name__ == '__main__':
    main()
