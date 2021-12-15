#!python3

'''
658: too high
'''

import csv
from functools import cache

from helpers import BASE

TEST01 = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''


def parse(string):
    map_ = {}
    for y, line in enumerate(string.strip().split('\n')):
        for x, n in enumerate(line):
            map_[x, y] = int(n)
    return map_


def min_rd_neighbours(location, map_):
    x, y = location
    return min(map_.get((x + 1, y), 10_000_000), map_.get((x, y + 1), 10_000_000))


def make_csv(input_map, file_name):
    m = max(input_map)
    x_max = m[0] + 1
    y_max = m[1] + 1
    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        for y in range(x_max):
            row = []
            for x in range(y_max):
                row.append(input_map[x, y])
            writer.writerow(row)


def part1(input_map):
    '''Dynamic programming building up minimum sum from bottom right.
    Minimum sums are generated in the input dict.'''
    # make_csv(input_map, 'day15_1.csv')
    initial = input_map[0, 0]
    n = sum(max(input_map))
    for i in range(n - 1, -1, -1):
        for location in (l for l in input_map if sum(l) == i):
            input_map[location] += min_rd_neighbours(location, input_map)
    # make_csv(input_map, 'day15_2.csv')
    return input_map[0, 0] - initial


def part1a(input_map):
    '''Recursive function starting in top left.'''
    @cache
    def do_sum(location):
        x, y = location
        if x == 0 and y == 0:
            return 0
        if x == 0:
            return do_sum((x, y - 1)) + input_map[location]
        if y == 0:
            return do_sum((x - 1, y)) + input_map[location]
        return min(do_sum((x, y - 1)), do_sum((x - 1, y))) + input_map[location]

    m = max(input_map)
    x_max = m[0] + 1
    y_max = m[1] + 1
    sums = {(0, 0): 0}
    for y in range(y_max):
        for x in range(x_max):
            location = (x, y)
            sums[location] = do_sum(location)
    return sums[m]


def part1b(input_map):
    '''Dynamic programming building up minimum sum from bottom right.
    Similar to part1, but sums are stored in a separate dict.'''
    m = max(input_map)
    x_max = m[0]
    y_max = m[1]
    sums = {}
    sums[m] = input_map[m]
    for x in range(x_max - 1, -1, -1):
        sums[x, y_max] = input_map[x, y_max] + sums[x + 1, y_max]
    for y in range(y_max - 1, -1, -1):
        sums[x_max, y] = input_map[x_max, y] + sums[x_max, y + 1]
    for y in range(y_max - 1, -1, -1):
        for x in range(x_max - 1, -1, -1):
            l = x, y
            l1 = x + 1, y
            l2 = x, y + 1
            sums[l] = input_map[l] + min(sums.get(l1, 1_000_000), sums.get(l2, 1_000_000))
    return sums[0, 0] - input_map[0, 0]


def main():
    test_map = parse(TEST01)
    map_ = parse(open(BASE + 'day15.txt', 'r').read())

    t1 = part1(test_map.copy())
    assert t1 == 40

    print(t1)
    t1a = part1a(test_map.copy())
    print(t1a)
    t1b = part1b(test_map.copy())
    print(t1b)

    p1 = part1(map_.copy())
    print(f'Part 1: {p1}')

    p1a = part1a(map_.copy())
    print(p1a)
    p1b = part1b(map_.copy())
    print(p1b)


if __name__ == '__main__':
    main()
