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


def get_neighbour(row, col, grid):
    for r in (-1, 0, 1):
        for c in (-1, 0, 1):
            if r == c == 0:
                continue
            new_row = row + r
            new_col = col + c
            yield grid.get((new_row, new_col), '.')


def update_seats(grid):
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
                if c['#'] >= 4:
                    new_grid[coord] = 'L'
                else:
                    new_grid[coord] = '#'
            else:
                raise IOError
    return new_grid


def _part1(grid):
    while True:
        new_grid = update_seats(grid)
        if new_grid == grid:
            c = Counter(v for v in grid.values())
            return c['#']
        grid = new_grid


def test1():
    grid = get_input(TEST_INPUT)
    return _part1(grid)


def part1():
    grid = get_input(open(INPUT, 'r').read())
    return _part1(grid)


def main():
    assert test1() == 37

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
