
from help import get_input

'''
Part 2
------
3418: too high
2339: too high
2053: too low

is hole (2, 12, 8)
is hole (3, 6, 6)
is hole (3, 7, 13)
is hole (3, 8, 9)
is hole (3, 10, 6)
is hole (4, 11, 13)
is hole (4, 13, 4)
is hole (4, 13, 14)
is hole (5, 10, 16)
is hole (5, 14, 8)
is hole (6, 6, 16)
is hole (7, 2, 13)
is hole (7, 10, 17)
is hole (7, 12, 3)
is hole (7, 16, 12)
is hole (8, 4, 14)
is hole (9, 9, 17)
is hole (9, 12, 3)
is hole (9, 16, 6)
is hole (10, 8, 1)
is hole (11, 4, 15)
is hole (12, 2, 13)
is hole (12, 10, 17)
is hole (13, 14, 14)
is hole (13, 16, 10)
is hole (13, 16, 12)
is hole (14, 6, 14)
is hole (14, 8, 5)
is hole (14, 15, 11)
is hole (15, 6, 7)
is hole (16, 8, 13)
is hole (17, 12, 8)
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


def is_hole_2(c, cubes, xmin, xmax, ymin, ymax, zmin, zmax):
    cx, cy, cz = c

    for x in range(xmax - cx + 2):
        l = cx + x, cy, cz
        if l in cubes:
            break
    else:
        return False

    for x in range(cx - xmin + 2):
        l = cx - x, cy, cz
        if l in cubes:
            break
    else:
        return False

    for y in range(ymax - cy + 2):
        l = cx, cy + y, cz
        if l in cubes:
            break
    else:
        return False

    for y in range(cy - ymin + 2):
        l = cx, cy - y, cz
        if l in cubes:
            break
    else:
        return False

    for z in range(zmax - cz + 2):
        l = cx, cy, cz + z
        if l in cubes:
            break
    else:
        return False

    for z in range(cz - zmin + 2):
        l = cx, cy, cz - z
        if l in cubes:
            break
    else:
        return False

    return True


def part1(cubes):
    neighbours = dict()
    for c1 in cubes:
        neighbours[c1] = []
        for c2 in cubes:
            if manhattan(c1, c2) == 1:
                neighbours[c1].append(c2)
    answer = 0
    for _, ns in neighbours.items():
        answer += 6 - len(ns)
    return answer


def part2(cubes, p1):
    xs = set()
    ys = set()
    zs = set()
    for c in cubes:
        xs.add(c[0])
        ys.add(c[1])
        zs.add(c[2])
    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    zmin = min(zs)
    zmax = max(zs)

    x_range = range(xmin, xmax + 1)
    y_range = range(ymin, ymax + 1)
    z_range = range(zmin, zmax + 1)

    cubes = set(cubes)
    holes = []
    not_holes = []
    for x in x_range:
        for y in y_range:
            for z in z_range:
                c1 = x, y, z
                if c1 in cubes:
                    continue
                if is_hole_2(c1, cubes, xmin, xmax, ymin, ymax, zmin, zmax):
                    holes.append(c1)
                else:
                    not_holes.append(c1)

    # If a hole touches a 'not hole' it is not a hole
    holes = set(holes)
    while True:
        new_not_holes = []
        for hole in holes:
            for not_hole in not_holes:
                if manhattan(hole, not_hole) == 1:
                    new_not_holes.append(hole)
        for x in new_not_holes:
            holes.remove(x)
            not_holes.append(x)
        if not new_not_holes:
            break

    touch = 0
    for h in holes:
        for c in cubes:
            if manhattan(h, c) == 1:
                touch += 1

    return p1 - touch


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
