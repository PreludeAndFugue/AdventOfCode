
from collections import defaultdict
from itertools import combinations

from help import get_input

TEST = '''
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
'''

def intersection(r1, r2):
    '''Returns the intersection of two ranges. If the intersection is empty return None'''
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None


class Brick:
    def __init__(self, n, x, y, z):
        self.n = n
        self.x = x
        self.y = y
        self.z = z

    def interects_x_y(self, other):
        x = bool(intersection(self.x, other.x))
        if not x: return False
        y = bool(intersection(self.y, other.y))
        return y

    def __repr__(self) -> str:
        return f'{self.n}: {self.x.start}-{self.x.stop - 1},{self.y.start}-{self.y.stop - 1},{self.z.start}-{self.z.stop - 1}'


def parse(d):
    for i, line in enumerate(d.split('\n')):
        a, b = line.split('~')
        a = [int(x) for x in a.split(',')]
        b = [int(x) for x in b.split(',')]
        yield Brick(i, range(a[0], b[0] + 1), range(a[1], b[1] + 1), range(a[2], b[2] + 1))


def do_fall_a(d):
    bricks = sorted(list(parse(d)), key=lambda b: b.z.start)
    for i, b in enumerate(bricks):
        if b.z.start == 1: continue
        zs = []
        for other in bricks[:i]:
            if b.interects_x_y(other):
                zs.append(other.z)
        if zs:
            z_start = max(z.stop for z in zs)
            # drop to rest on block
            l = b.z.stop - b.z.start
            b.z = range(z_start, z_start + l)
        else:
            # drop to rest on ground
            r = b.z
            b.z = range(1, r.stop - r.start + 1)

    return bricks


def make_dependencies(bricks):
    supports = defaultdict(list)
    rests_on = defaultdict(list)
    for b in bricks:
        for other in bricks:
            if other.n == b.n: continue
            if not b.interects_x_y(other): continue
            if b.z.stop == other.z.start:
                supports[b.n].append(other)
                rests_on[other.n].append(b)
    return supports, rests_on


def main():
    d = get_input('22').strip()
    # d = TEST.strip()

    bricks = do_fall_a(d)

    bricks = sorted(bricks, key=lambda b: (b.z.start, b.x.start, b.y.start))
    brick_dict = {b.n: b for b in bricks}

    supports, rests_on = make_dependencies(bricks)

    can_disintigrate = set()
    for b in bricks:
        supported = supports[b.n]
        if not supported:
            can_disintigrate.add(b.n)
            continue
        tests = []
        for s in supported:
            supporters = rests_on[s.n]
            if len(supporters) > 1:
                tests.append(True)
            else:
                tests.append(False)
        if all(tests):
            can_disintigrate.add(b.n)
    print(len(can_disintigrate))


if __name__ == '__main__':
    main()
