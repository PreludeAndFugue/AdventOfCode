#!python3

from collections import Counter

INPUT = 'day11.txt'
TEST_INPUT = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''


DIRECTIONS = [
    (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
]


def get_input(input):
    grid = {}
    for r, line in enumerate(input.strip().split('\n')):
        for c, el in enumerate(line.strip()):
            grid[(r, c)] = el
    return grid


def print_grid(grid):
    max_row = max(k[0] for k in grid.keys()) + 1
    max_col = max(k[1] for k in grid.keys()) + 1
    result = ''
    for r in range(max_row):
        row = []
        for c in range(max_col):
            row.append(grid[(r, c)])
        result = result + '\n' + ''.join(row)
    print(result)


def get_neighbour1(row, col, grid):
    for r, c in DIRECTIONS:
        if r == c == 0:
            continue
        new_row = row + r
        new_col = col + c
        yield grid.get((new_row, new_col), '.')


def get_neighbour2(row, col, grid):
    def get(grid, row, col, dr, dc):
        while True:
            row += dr
            col += dc
            el = grid.get((row, col), 'x')
            if el == '.':
                continue
            elif el == 'x':
                return '.'
            else:
                return el
    for r, c in DIRECTIONS:
        x = get(grid, row, col, r, c)
        yield x


def update_seats(grid, limit, get_neighbour):
    new_grid = {}
    for coord, el in grid.items():
        if el == '.':
            new_grid[coord] = el
        else:
            n = get_neighbour(*coord, grid)
            c = Counter(n)
            if el == 'L':
                if c['#'] == 0:
                    new_grid[coord] = '#'
                else:
                    new_grid[coord] = el
            elif el == '#':
                if c['#'] >= limit:
                    new_grid[coord] = 'L'
                else:
                    new_grid[coord] = '#'
            else:
                raise IOError
    return new_grid


def part1(grid):
    while True:
        new_grid = update_seats(grid, 4, get_neighbour1)
        if new_grid == grid:
            c = Counter(v for v in grid.values())
            return c['#']
        grid = new_grid


def part2(grid):
    while True:
        new_grid = update_seats(grid, 5, get_neighbour2)
        if new_grid == grid:
            c = Counter(v for v in grid.values())
            return c['#']
        grid = new_grid


def main():
    grid = get_input(open(INPUT, 'r').read())
    test_grid = get_input(TEST_INPUT)

    assert part1(test_grid) == 37

    p = part1(grid)
    print(p)

    assert part2(test_grid) == 26

    p = part2(grid)
    print(p)


if __name__ == "__main__":
    main()
