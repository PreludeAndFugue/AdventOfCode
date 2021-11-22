#!python3

INPUT = 'day24.txt'
TEST_INPUT = '''....#
#..#.
#..##
..#..
#....
'''


MOVES = (
    (-1, 0), (1, 0), (0, -1), (0, 1)
)


def parse_input(input):
    result = {}
    for y, row in enumerate(input.strip().split('\n')):
        for x, el in enumerate(row):
            if el == '#':
                result[(x, y)] = True
            else:
                result[(x, y)] = False
    return result


def get_neighbour_coords(c):
    x, y = c
    for dx, dy in MOVES:
        new_x = x + dx
        new_y = y + dy
        if new_x < 0 or new_x > 4 or new_y < 0 or new_y > 4:
            continue
        yield x + dx, y + dy


def update(c, grid):
    s = sum(grid.get(n) for n in get_neighbour_coords(c))
    if grid.get(c):
        return s == 1
    else:
        return s == 1 or s == 2


def update_grid(grid):
    new_grid = {}
    for c in grid.keys():
        new_grid[c] = update(c, grid)
    return new_grid


def grid_state(grid):
    rows = []
    for y in range(5):
        row = []
        for x in range(5):
            c = x, y
            v = '#' if grid[c] else '.'
            row.append(v)
        rows.append(''.join(row))
    return '\n'.join(rows)


def biodiversity_rating(grid):
    rating = 0
    for y in range(5):
        for x in range(5):
            c = x, y
            if grid[c]:
                p = 5*y + x
                rating += 2**p
    return rating


def print_grid(grid):
    print(grid_state(grid))
    print()


def _part1(grid):
    states = set([grid_state(grid)])
    while True:
        grid = update_grid(grid)
        state = grid_state(grid)
        if state in states:
            r = biodiversity_rating(grid)
            return r
        states.add(state)


def test1():
    grid = parse_input(TEST_INPUT)
    assert _part1(grid) == 2129920


def part1():
    grid = parse_input(open(INPUT, 'r').read())
    return _part1(grid)


def main():
    test1()

    p1 = part1()
    print(p1)


if __name__ == "__main__":
    main()
