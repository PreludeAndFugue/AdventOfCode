
from help import get_input
from day15 import parse, manhattan, TEST1
from day15a import make_boundary, tuning_freq

'''
Go round boundary points and find the first one that is not inside any of the
other sensor-beacon diamonds.
'''

x = get_input('15')
# x = TEST1.strip()
sbs = list(parse(x))

# mmax = 20
mmax = 4000000


def is_outside_all(x, s1, sbs):
    for s, b in sbs:
        if s == s1:
            continue
        d = manhattan(s, b)
        d1 = manhattan(x, s)
        if d1 <= d:
            return False
    return True


def test():
    for s, b in sbs:
        boundary = make_boundary(s, b, mmax)
        for x in boundary:
            if is_outside_all(x, s, sbs):
                return tuning_freq(x)

print(test())
