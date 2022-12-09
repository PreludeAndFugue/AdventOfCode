
from help import get_input

'''
Part 2
------
700 too low
'''


TEST = '''30373
25512
65332
33549
35390'''

DIRS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def part1(grid):
    def check(row, col):
        nonlocal height
        h = grid[row][col]
        if h > height:
            can_see.add((row, col))
            height = h

    columns = len(grid[0])
    rows = len(grid)
    can_see = set()
    for row in range(rows):
        height = -1
        for col in range(columns):
            check(row, col)

        height = -1
        for col in reversed(range(columns)):
            check(row, col)

    for col in range(columns):
        height = -1
        for row in range(rows):
            check(row, col)

        height = -1
        for row in reversed(range(rows)):
            check(row, col)

    return len(can_see)


def scenic_score(row, col, grid):
    height = grid[row][col]
    result = 1
    # up, left, right, down
    for dr, dc in DIRS:
        count = 0
        r, c = row, col
        while True:
            r += dr
            c += dc
            if r < 0 or c < 0:
                break
            try:
                h = grid[r][c]
            except IndexError:
                break
            count += 1
            if h >= height:
                break
        result *= count
    return result


def part2(grid):
    c = len(grid[0])
    r = len(grid)
    return max(scenic_score(row, col, grid) for row in range(r) for col in range(c))


def main():
    s = get_input('08')
    # s = TEST.strip()
    grid = list(list(map(int, l))for l in s.strip().split('\n'))

    p1 = part1(grid)
    p2 = part2(grid)

    print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()
