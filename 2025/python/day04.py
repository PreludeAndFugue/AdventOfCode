
from help import get_input

TEST01 = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''


NEIGHBOURS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1)
]

source = TEST01.strip()
source = get_input(4)


def make_map(source):
    map_ = {}
    for y, line in enumerate(source.split('\n')):
        for x, c in enumerate(line.strip()):
            if c == '@':
                map_[(x, y)] = c
    return map_


def get_neighbours(x, y, map_):
    neighbours = []
    for dx, dy in NEIGHBOURS:
        nx, ny = x + dx, y + dy
        if (nx, ny) in map_:
            neighbours.append((nx, ny))
    return neighbours


def part1():
    map_ = make_map(source)
    t = 0
    for x, y in map_:
        neighbours = get_neighbours(x, y, map_)
        if len(neighbours) < 4:
            t += 1
    return t


def part2():
    map_ = make_map(source)
    t = 0
    while True:
        points_to_delete = []
        for x, y in map_:
            neighbours = get_neighbours(x, y, map_)
            if len(neighbours) < 4:
                t += 1
                points_to_delete.append((x, y))
        if not points_to_delete:
            break
        for p in points_to_delete:
            del map_[p]
    return t


if __name__ == '__main__':
    p1 = part1()
    print(p1)
    p2 = part2()
    print(p2)
