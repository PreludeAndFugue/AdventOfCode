
from help import get_input

from copy import deepcopy


test1 = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

DIRECTIONS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

TURN_RIGHT = {
    'U': 'R',
    'R': 'D',
    'D': 'L',
    'L': 'U'
}


def parse(source):
    map_ = {}
    start = None
    for r, row in enumerate(source.split('\n')):
        for c, ch in enumerate(row):
            if ch == '^':
                start = r, c
                ch == '.'
            map_[(r, c)] = ch
    return map_, start


def move(p, d, map_):
    r, c = p
    dr, dc = DIRECTIONS[d]
    rr = r + dr
    cc = c + dc
    pp = rr, cc
    ch = map_.get(pp, None)
    if ch is None:
        return None, None
    if ch == '#':
        return p, TURN_RIGHT[d]
    else:
        return pp, d


def walk(start, direction, map_):
    p = start
    # (start, direction) tuples
    locations = set([(start, direction)])
    while True:
        p, direction = move(p, direction, map_)
        if p is None:
            return False
        location = p, direction
        if location in locations:
            return True
        locations.add(location)


def original_walk(start, direction, map_):
    points = set([start])
    p = start
    while True:
        p, direction = move(p, direction, map_)
        if p is None:
            break
        points.add(p)
    return points


def part1():
    source = get_input(6)
    # source = test1.strip()

    map_, start = parse(source)
    direction = 'U'

    points = original_walk(start, direction, map_)

    print(len(points))


def part2():
    source = get_input(6)
    # source = test1.strip()

    map_, start = parse(source)
    direction = 'U'

    points = original_walk(start, direction, map_)
    obstructions = sorted(p for p in points if p != start)

    valid = []
    for obstruction in obstructions:
        print(obstruction)
        m = deepcopy(map_)
        m[obstruction] = '#'
        result = walk(start, direction, m)
        if result:
            valid.append(obstruction)

    print(len(valid))


part1()
part2()
