
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

    def can_fall(self):
        return self.z.start > 1

    def fall(self):
        self.z = range(self.z.start - 1, self.z.stop - 1)

    def test_fall(self):
        z = range(self.z.start - 1, self.z.stop - 1)
        return Brick(self.n, self.x, self.y, z)

    def intersects(self, other):
        x = bool(intersection(self.x, other.x))
        if not x: return False
        y = bool(intersection(self.y, other.y))
        if not y: return False
        z = bool(intersection(self.z, other.z))
        return z
        # return x and y and z

    def __repr__(self) -> str:
        return f'{self.n}: {self.x.start},{self.y.start},{self.z.start}~{self.x.stop - 1},{self.y.stop - 1},{self.z.stop - 1}'


def parse(d):
    for i, line in enumerate(d.split('\n')):
        a, b = line.split('~')
        a = [int(x) for x in a.split(',')]
        b = [int(x) for x in b.split(',')]
        yield Brick(i, range(a[0], b[0] + 1), range(a[1], b[1] + 1), range(a[2], b[2] + 1))


def get_fallers(bricks):
    for b in bricks:
        if b.can_fall():
            yield b


def find_faller(bricks):
    '''A single fall step for all bricks'''
    fallers = list(get_fallers(bricks))
    # print('fallers', len(fallers))
    if not fallers:
        return None
    for f in fallers:
        # print("fall test", f.n)
        f_test = f.test_fall()
        intersections = []
        for other in bricks:
            if other.n == f_test.n:
                continue
            intersections.append(f_test.intersects(other))
        # print('fall intersections', intersections)
        if not any(intersections):
            return f
    return None


def part1(d):
    def process_fall(b, bricks):
        # print('process fall', b)
        did_fall = False
        while True:
            # print('\tcan fall', b.can_fall())
            if not b.can_fall():
                return did_fall
            test_b = b.test_fall()
            for other in bricks:
                if other.n == test_b.n: continue
                if test_b.intersects(other):
                    return did_fall
            b.fall()
            # print('\tfalling', b)
            did_fall = True

    bricks = list(parse(d))
    bricks = sorted(bricks, key=lambda b: b.z.start)

    repeat = True
    while repeat:
        repeat = any(process_fall(b, bricks) for b in bricks)

    return bricks


def main():
    d = get_input('22').strip()
    # d = TEST.strip()

    bricks = part1(d)

    can_disintigrate = []
    for b in bricks:
        others = bricks[:b.n] + bricks[b.n + 1:]
        f = find_faller(others)
        if f is None:
            can_disintigrate.append(b)

    print('can disintigrate')
    print(len(can_disintigrate))


if __name__ == '__main__':
    main()
