#!python3

from math import sqrt

from helpers import BASE
import day11test

TEST02 = '''11111
19991
19191
19991
11111'''


NEIGHBOURS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]


def parse(string):
    grid = {}
    for y, line in enumerate(string.split('\n')):
        for x, c in enumerate(line):
            n = int(c)
            grid[x, y] = n
    return grid


def get_neighbours(location, grid):
    x, y = location
    for dx, dy in NEIGHBOURS:
        new_location = x + dx, y + dy
        try:
            _ = grid[new_location]
            yield new_location
        except:
            pass


def print_grid(grid):
    n = int(sqrt(len(grid)))
    rows = []
    for y in range(n):
        row = ''.join(str(grid[x, y]) for x in range(n))
        rows.append(row)
    g = '\n'.join(rows)
    print(g)


def step(grid):
    for location in grid:
        grid[location] += 1

    will_flash = set()
    can_flash = [l for l, v in grid.items() if v >= 10]
    while can_flash:
        location = can_flash.pop()
        if location in will_flash:
            continue
        for l in get_neighbours(location, grid):
            grid[l] += 1
            if grid[l] >= 10:
                can_flash.append(l)
        will_flash.add(location)

    for location in will_flash:
        grid[location] = 0
    return len(will_flash)


def part1(grid):
    return sum(step(grid) for _ in range(100))


def part2(grid):
    step_count = 0
    while True:
        c = step(grid)
        step_count += 1
        if c == 100:
            return step_count


def main():
    test_grid_1 = parse(day11test.TEST01[0])
    grid = parse(open(BASE + 'day11.txt', 'r').read())

    g = test_grid_1.copy()
    t1 = part1(g)
    assert t1 == 1656

    g = grid.copy()
    p1 = part1(g)
    print(f'Part 1: {p1}')

    g = test_grid_1.copy()
    t2 = part2(g)
    assert t2 == 195

    g = grid.copy()
    p2 = part2(g)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
