
from help import get_input

'''
Part 2
------
3418: too high
'''

TEST1 = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''


def parse(s):
    for line in s.split('\n'):
        yield tuple(map(int, line.split(',')))


def manhattan(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)


def is_hole(c, cubes):
    '''Is the cube location c a hole in all the cubes.

    This means that c is not in cubes and c has six neighbours.
    '''
    if c in cubes:
        return False
    n = 0
    for x in cubes:
        if manhattan(c, x) == 1:
            n += 1
        if n >= 6:
            return True
    return False


def part1(cubes):
    neighbours = dict()
    for c1 in cubes:
        neighbours[c1] = []
        for c2 in cubes:
            if manhattan(c1, c2) == 1:
                neighbours[c1].append(c2)
    answer = 0
    for c, ns in neighbours.items():
        answer += 6 - len(ns)
        # print(c)
        # print('\t', ns)
    return answer


def part2(cubes, p1):
    xs = set()
    ys = set()
    zs = set()
    for c in cubes:
        xs.add(c[0])
        ys.add(c[1])
        zs.add(c[2])
    xs = sorted(xs)
    ys = sorted(ys)
    zs = sorted(zs)

    # print(xs)
    # print(ys)
    # print(zs)

    x_range = range(xs[0] - 1, xs[-1] + 2)
    y_range = range(ys[0] - 1, ys[-1] + 2)
    z_range = range(zs[0] - 1, zs[-1] + 2)
    # print(x_range)
    # print(y_range)
    # print(z_range)
    cubes = set(cubes)
    count = 0
    for x in x_range:
        for y in y_range:
            for z in z_range:
                c1 = x, y, z
                if is_hole(c1, cubes):
                    # print('is hole', c1)
                    count += 1
    return p1 - 6 * count



def main():
    s = get_input('18')
    # s = TEST1.strip()

    cubes = list(parse(s))

    p1 = part1(cubes)
    p2 = part2(cubes, p1)

    print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()
