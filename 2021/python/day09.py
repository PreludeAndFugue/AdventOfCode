#!python3

from helpers import BASE

TEST01 = '''2199943210
3987894921
9856789892
8767896789
9899965678'''


def parse(string):
    lines = string.strip().split('\n')
    map = {}
    for i, row in enumerate(lines):
        for j, col in enumerate(row):
            map[i, j] = int(col)
    return map


def neighbour_heights(map, row, col):
    return [
        map.get((row - 1, col), 1_000_000),
        map.get((row + 1, col), 1_000_000),
        map.get((row, col - 1), 1_000_000),
        map.get((row, col + 1), 1_000_000),
    ]


def part1(map):
    minima = []
    for location, height in map.items():
        nh = neighbour_heights(map, *location)
        if height < min(nh):
            minima.append(height)
    return sum(n + 1 for n in minima)


def main():
    test_map = parse(TEST01)
    map_ = parse(open(BASE + 'day09.txt').read())

    t1 = part1(test_map)
    assert t1 == 15

    p1 = part1(map_)
    print(f'Part 1: {p1}')


if __name__ == '__main__':
    main()
