from itertools import combinations
from functools import cache

from help import get_input

TEST01 = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

source = TEST01.strip()
source = get_input(9)


def get_points(source):
    ps = []
    for line in source.split('\n'):
        p = tuple(map(int, line.split(',')))
        ps.append(p)
    return ps


def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = abs(x1 - x2) + 1
    dy = abs(y1 - y2) + 1
    return dx*dy


def part1():
    ps = get_points(source)
    a = 0
    for p1, p2 in combinations(ps, 2):
        a = max(a, area(p1, p2))
    return a


def print_map(map_):
    xs = []
    ys = []
    for x, y in map_:
        xs.append(x)
        ys.append(y)
    x_max = max(xs)
    y_max = max(ys)
    print('map dimensions', 0, 0, x_max, y_max)
    rows = []
    for y in range(0, y_max + 1):
        row = []
        for x in range(0, x_max + 1):
            row.append(map_.get((x, y), '.'))
        rows.append(''.join(row))
    print('\n'.join(rows))


outside_cache = {}
cache_count = 0

# @cache
def is_outside(p: tuple[int, int], map_, x_max, y_max) -> bool:
    if p in outside_cache:
        # print('used cache')
        global cache_count
        cache_count += 1
        # if cache_count % 1_000 == 0:
        #     print('used cache', cache_count)
        return outside_cache[p]

    if p in map_:
        outside_cache[p] = False
        return False

    x, y = p
    while True:
        x -= 1
        if (x, y) in map_:
            break
        if x < 0:
            # print('\tescape', p, '->', x, y)
            outside_cache[p] = True
            return True

    x, y = p
    while True:
        y -= 1
        if (x, y) in map_:
            break
        if y < 0:
            # print('\tescape', p, '->', x, y)
            outside_cache[p] = True
            return True

    x, y = p
    while True:
        x += 1
        if (x, y) in map_:
            break
        if x > x_max:
            # print('\tescape', p, '->', x, y)
            outside_cache[p] = True
            return True

    x, y = p
    while True:
        y += 1
        if (x, y) in map_:
            break
        if y > y_max:
            # print('\tescape', p, '->', x, y)
            outside_cache[p] = True
            return True

    outside_cache[p] = False
    return False


def is_outside_rectangle(ps, map_, x_max, y_max) -> bool:
    for p in ps:
        if is_outside(p, map_, x_max, y_max):
            return True
    return False


def rectangle_points(p1, p2) -> list[tuple[int, int]]:
    points: list[tuple[int, int]] = []
    x1, y1 = p1
    x2, y2 = p2
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])

    if x1 == x2:
        points.append(p1)
        points.append(p2)
        for y in range(y1 + 1, y2):
            points.append((x1, y))
        return points

    if y1 == y2:
        points.append(p1)
        points.append(p2)
        for x in range(x1 + 1, x2):
            points.append((x, y1))
        return points

    points.append((x1, y1))
    points.append((x1, y2))
    points.append((x2, y1))
    points.append((x2, y2))

    for x in range(x1 + 1, x2):
        points.append((x, y1))
        points.append((x, y2))
    for y in range(y1 + 1, y2):
        points.append((x1, y))
        points.append((x2, y))

    return points


def part2(ps) -> tuple[tuple[int, int], tuple[int, int]]:
    xs = []
    ys = []
    for x, y in ps:
        xs.append(x)
        ys.append(y)
    x_max = max(xs) + 10
    y_max = max(ys) + 10

    map_ = {}
    for p1, p2 in zip(ps, ps[1:] + [ps[0]]):
        map_[p1] = '#'
        map_[p2] = '#'
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            for y in range(min(y1, y2) + 1, max(y1, y2)):
                map_[(x1, y)] = 'X'
        elif y1 == y1:
            for x in range(min(x1, x2) + 1, max(x1, x2)):
                map_[(x, y1)] = 'X'
        else:
            for x in range(min(x1, x2) + 1, max(x1, x2)):
                map_[(x, y1)] = 'X'
            for y in range(min(y1, y2) + 1, max(y1, y2)):
                map_[(x1, y)] = 'X'

    a = 0
    P1 = 0, 0
    P2 = 0, 0
    for p1, p2 in combinations(ps, 2):
        rectangle = rectangle_points(p1, p2)
        if not is_outside_rectangle(rectangle, map_, x_max, y_max):
            a1 = area(p1, p2)
            if a1 > a:
                a = a1
                P1 = p1
                P2 = p2

    return P1, P2


def part2a():
    '''
    Compact coordinates.
    '''
    ps = get_points(source)
    xs = set()
    ys = set()
    for x, y in ps:
        xs.add(x)
        ys.add(y)
    xs = sorted(xs)
    ys = sorted(ys)

    x_map_to_compact = {}
    x_map_from_compact = {}
    y_map_to_compact = {}
    y_map_from_compact = {}
    for i, x in enumerate(xs):
        x_map_from_compact[i] = x
        x_map_to_compact[x] = i
    for i, y in enumerate(ys):
        y_map_from_compact[i] = y
        y_map_to_compact[y] = i

    ps_compact = []
    for x, y in ps:
        p_compact = x_map_to_compact[x], y_map_to_compact[y]
        ps_compact.append(p_compact)

    p1, p2 = part2(ps_compact)

    q1 = x_map_from_compact[p1[0]], y_map_from_compact[p1[1]]
    q2 = x_map_from_compact[p2[0]], y_map_from_compact[p2[1]]

    return area(q1, q2)


if __name__ == '__main__':
    p1 = part1()
    print(p1)
    # p2 = part2()
    # print(p2)

    p2 = part2a()
    print(p2)
