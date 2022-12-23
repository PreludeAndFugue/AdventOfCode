from collections import defaultdict, deque

from help import get_input
from day23 import TEST


SURROUND = [
    -1 -1j, -1j, 1 - 1j,
    -1,          1,
    -1 + 1j, 1j, 1 + 1j
]


MOVE = deque([
    # north
    [-1 - 1j, -1j, 1 - 1j],
    # south
    [-1 + 1j, 1j, 1 + 1j],
    # west
    [-1 - 1j, -1, -1 + 1j],
    # east
    [1 - 1j, 1, 1 + 1j],
])


def parse(s):
    map_ = set()
    for y, row in enumerate(s.split('\n')):
        for x, col in enumerate(row):
            if col == '#':
                map_.add(x + y*1j)
    return map_


def is_alone(z, map_):
    for w in SURROUND:
        if z + w in map_:
            return False
    return True


def next_position(z, map_):
    if is_alone(z, map_):
        return z
    for direction in MOVE:
        s = set(z + w for w in direction)
        if not map_ & s:
            w = direction[1]
            return z + w
    return z


def next_positions(map_):
    np = defaultdict(set)
    for z in map_:
        nz = next_position(z, map_)
        np[nz].add(z)
    return np


def move(np):
    new_map = set()
    for nz, current_zs in np.items():
        if len(current_zs) > 1:
            new_map |= current_zs
        else:
            new_map.add(nz)
    return new_map


def size(map_):
    xs = [z.real for z in map_]
    ys = [z.imag for z in map_]
    xmin = min(xs)
    xmax = max(xs) + 1
    ymin = min(ys)
    ymax = max(ys) + 1
    square = (xmax - xmin) * (ymax - ymin)
    return square - len(map_)


def main():
    s = get_input('23')
    # s = TEST.strip()
    map_ = parse(s)

    # print(map_)

    p1 = 0
    p2 = 0

    for i in range(10_000):
        nz = next_positions(map_)
        new_map = move(nz)
        if i == 9:
            p1 = size(new_map)
        if new_map == map_:
            p2 = i + 1
            break
        map_ = new_map

        MOVE.rotate(-1)

    print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()
