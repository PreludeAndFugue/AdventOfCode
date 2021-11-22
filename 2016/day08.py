#!python3

import re

SOURCE = 'day08.txt'

TEST1 = '''rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1'''


PATTERN_RECT = r'rect (\d+)x(\d+)'
PATTERN_ROW = r'rotate row y=(\d+) by (\d+)'
PATTERN_COL = r'rotate column x=(\d+) by (\d+)'

p1 = re.compile(PATTERN_RECT)
p2 = re.compile(PATTERN_ROW)
p3 = re.compile(PATTERN_COL)


def transpose(screen):
    x = zip(*screen)
    return [''.join(y) for y in x]


def match(row):
    m1 = p1.match(row)
    if m1:
        return rect, *list(map(int, m1.groups()))
    m2 = p2.match(row)
    if m2:
        return rotate_row, *list(map(int, m2.groups()))
    m3 = p3.match(row)
    if m3:
        return rotate_col, *list(map(int, m3.groups()))


def rect(row, col, screen):
    for i in range(col):
        r = screen[i]
        x = '#' * row
        r = x + r[row:]
        screen[i] = r
    return screen


def rotate_row(row_index, by, screen):
    r = screen[row_index]
    rlen = len(r)
    by = by % rlen
    i = rlen - by
    r = r[i:] + r[:i]
    screen[row_index] = r
    return screen


def rotate_col(col_index, by, screen):
    screen = transpose(screen)
    screen = rotate_row(col_index, by, screen)
    screen = transpose(screen)
    return screen


def print_screen(screen):
    print('\n'.join(screen))


def count_on(screen):
    count = 0
    for row in screen:
        for x in row:
            if x == '#':
                count += 1
    return count


def main1():
    screen = ['.' * 50 for _ in range(6)]
    for row in open(SOURCE, 'r').read().strip().split('\n'):
        f, a, b = match(row)
        screen = f(a, b, screen)
    print(count_on(screen))
    print_screen(screen)



def test1():
    screen = [
        '.......',
        '.......',
        '.......'
    ]
    test = [
        '.#..#.#',
        '#.#....',
        '.#.....',
    ]
    for row in TEST1.strip().split('\n'):
        f, a, b = match(row)
        screen = f(a, b, screen)
    assert screen == test


if __name__ == '__main__':
    test1()
    main1()
