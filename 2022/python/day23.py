
from collections import defaultdict, deque

from help import get_input

TEST = '''....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..'''


TEST2 = '''.....
..##.
..#..
.....
..##.
.....'''


SURROUND = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1)
]


MOVE = deque([
    # north
    [(-1, -1), (0, -1), (1, -1)],
    # south
    [(-1, 1), (0, 1), (1, 1)],
    # west
    [(-1, -1), (-1, 0), (-1, 1)],
    # east
    [(1, -1), (1, 0), (1, 1)],
])


def parse(s):
    map_ = set()
    for y, row in enumerate(s.split('\n')):
        for x, col in enumerate(row):
            if col == '#':
                map_.add((x, y))
    return map_


def draw(map_):
    xs = [x for x, y in map_]
    xmin = min(xs)
    xmax = max(xs)
    ys = [y for x, y in map_]
    ymin = min(ys)
    ymax = max(ys)
    rows = []
    for y in range(ymin - 1, ymax + 2):
        row = ''
        for x in range(xmin - 1, xmax + 2):
            e = x, y
            if e in map_:
                row += '#'
            else:
                row += '.'
        rows.append(row)
    print('\n'.join(rows))
    print()


def is_alone(e, map_):
    x, y = e
    for dx, dy in SURROUND:
        xx = x + dx
        yy = y + dy
        if (xx, yy) in map_:
            return False
    return True


def next_position(e, map_):
    if is_alone(e, map_):
        return e
    x, y = e
    for direction in MOVE:
        s = set((x + dx, y + dy) for dx, dy in direction)
        if not map_ & s:
            dxx, dyy = direction[1]
            return x + dxx, y + dyy
    return e


def next_positions(map_):
    np = defaultdict(set)
    for e in map_:
        ne = next_position(e, map_)
        np[ne].add(e)
    return np


def move(np):
    new_map = set()
    for new_position, current_positions in np.items():
        if len(current_positions) > 1:
            new_map |= current_positions
        else:
            new_map.add(new_position)
    return new_map


def size(map_):
    xs = [x for x, y in map_]
    xmin = min(xs)
    xmax = max(xs) + 1
    ys = [y for x, y in map_]
    ymin = min(ys)
    ymax = max(ys) + 1
    square = (xmax - xmin) * (ymax - ymin)
    return square - len(map_)


def main():
    s = get_input('23')
    # s = TEST.strip()
    # s = TEST2.strip()
    map_ = parse(s)
    l = len(map_)

    p1 = 0
    p2 = 0

    for i in range(10_000):
        nps = next_positions(map_)
        new_map = move(nps)
        if i == 9:
            p1 = size(new_map)
        if new_map == map_:
            p2 = i + 1
            break
        map_ = new_map
        assert len(map_) == l

        MOVE.rotate(-1)

    print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()
