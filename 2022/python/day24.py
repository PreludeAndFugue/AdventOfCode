
from collections import defaultdict
import heapq

from help import get_input


TEST = '''#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#'''


TEST2 = '''#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#'''


DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]


def parse(s):
    print(s)
    rows = s.split('\n')
    start = 1, 0
    goal = len(rows[0]) - 2, len(rows) - 1
    xmax = len(rows[0]) - 2
    ymax = len(rows) - 2
    blizzard_types = '<>^v'
    blizzards = defaultdict(list)
    map_ = {}
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch in blizzard_types:
                blizzards[(x, y)].append(ch)
                map_[(x, y)] = '.'
            else:
                map_[(x, y)] = ch
    # print(start, goal, xmax, ymax, blizzards)
    return start, goal, xmax, ymax, map_, blizzards


def draw(map_, blizzards, start, goal, location, xmax, ymax):
    xs = [x for x, _ in map_]
    ys = [y for _, y in map_]
    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    rows = []
    for y in range(ymin, ymax + 1):
        row = []
        for x in range(xmin, xmax + 1):
            ch = map_[(x, y)]
            row.append(ch)
        rows.append(row)
    for (x, y), items in blizzards.items():
        if len(items) == 1:
            rows[y][x] = items[0]
        else:
            rows[y][x] = str(len(items))
    x, y = location
    rows[y][x] = 'E'
    print('\n'.join(''.join(r) for r in rows))
    print()


def move_blizzards(blizzards, xmax, ymax):
    new_blizzards = defaultdict(list)
    for location, items in blizzards.items():
        x, y = location
        for item in items:
            if item == '<':
                nx = xmax if x == 1 else x - 1
                new_blizzards[(nx, y)].append(item)
            elif item == '>':
                nx = 1 if x == xmax else x + 1
                new_blizzards[(nx, y)].append(item)
            elif item == '^':
                ny = ymax if y == 1 else y - 1
                new_blizzards[(x, ny)].append(item)
            elif item == 'v':
                ny = 1 if y == ymax else y + 1
                new_blizzards[(x, ny)].append(item)
            else:
                raise ValueError
    return new_blizzards


def get_neighbours(location, map_, blizzards):
    x, y = location
    for dx, dy in DIRS:
        nx = x + dx
        ny = y + dy
        nl = nx, ny
        ch = map_.get(nl, '#')
        if ch == '#':
            continue
        if nl in blizzards:
            continue
        yield nl


def manhattan(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) + abs(y2 - y1)


def part1(map_, blizzards, start, goal, xmax, ymax, status):
    print('xmax', xmax, 'ymax', ymax)
    dgoal = manhattan(start, goal)
    q = [(0, dgoal, start, blizzards)]
    # (distance, location pairs)
    seen = set()

    i = 0

    while q:
        t, dgoal, location, bl = heapq.heappop(q)

        # print(d, dgoal, location)
        # draw(map_, bl, start, goal, location, xmax, ymax)
        # input()
        i += 1
        if i % 10_000 == 0:
            print(t, dgoal, location, status)

        if location == goal:
            return t, bl

        s = t, location
        if s in seen:
            continue
        seen.add(s)

        new_bl = move_blizzards(bl, xmax, ymax)
        for nl in get_neighbours(location, map_, new_bl):
            ndgoal = manhattan(nl, goal)
            heapq.heappush(q, (t + 1, ndgoal, nl, new_bl))


def part2(map_, blizzards, start, goal, xmax, ymax):
    t1, bl1 = part1(map_, blizzards, start, goal, xmax, ymax, 'to goal')
    t2, bl2 = part1(map_, bl1, goal, start, xmax, ymax, 'to start')
    t3, _ = part1(map_, bl2, start, goal, xmax, ymax, 'to goal 2')

    print(t1, t2, t3)
    return t1 + t2 + t3


def main():
    s = get_input('24')
    # s = TEST.strip()
    # s = TEST2.strip()
    start, goal, xmax, ymax, map_, blizzards = parse(s)

    p1, _ = part1(map_, blizzards, start, goal, xmax, ymax, '')
    p2 = part2(map_, blizzards, start, goal, xmax, ymax)

    print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()
