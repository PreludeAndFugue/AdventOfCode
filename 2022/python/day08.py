
from help import get_input


TEST = '''30373
25512
65332
33549
35390'''


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
    for row in range(columns):
        height = -1
        for col in range(rows):
            check(row, col)

        height = -1
        for col in reversed(range(rows)):
            check(row, col)

    for col in range(rows):
        height = -1
        for row in range(columns):
            check(row, col)

        height = -1
        for row in reversed(range(columns)):
            check(row, col)

    return len(can_see)


def main():
    s = get_input('08')
    # s = TEST.strip()
    grid = list(list(map(int, l))for l in s.strip().split('\n'))

    p1 = part1(grid)

    print('Part 1:', p1)


if __name__ == '__main__':
    main()
