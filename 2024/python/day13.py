
from fractions import Fraction
import re

from help import get_input

test1 = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''

p1 = r'Button A: X\+(\d+), Y\+(\d+)'
p2 = r'Button B: X\+(\d+), Y\+(\d+)'
p3 = r'Prize: X=(\d+), Y=(\d+)'

r1 = re.compile(p1)
r2 = re.compile(p2)
r3 = re.compile(p3)

'''
94a + 22b = 8400
34a + 67b = 5400


'''


def parse(source):
    t = 0
    for item in source.split('\n\n'):
        i1, i2, i3 = item.split('\n')
        m1 = r1.match(i1)
        m2 = r2.match(i2)
        m3 = r3.match(i3)
        a1, a2 = int(m1.group(1)), int(m1.group(2))
        b1, b2 = int(m2.group(1)), int(m2.group(2))
        c1, c2 = int(m3.group(1)), int(m3.group(2))
        c1 += 10000000000000
        c2 += 10000000000000

        d1 = a1*b2 - a2*b1
        x1 = c1*b2 - c2*b1
        y1 = a1*c2 - c1*a2

        x = Fraction(x1, d1)
        y = Fraction(y1, d1)
        if x.is_integer() and x >= 0 and y.is_integer() and y >= 0:
            t += 3*x + y
    print(t)


source = test1.strip()
source = get_input(13)

x = parse(source)
