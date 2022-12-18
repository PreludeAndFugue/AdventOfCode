
from itertools import cycle

from suffix_tree import Tree

from help import get_input

'''
Look for a repeating pattern in the rock.

https://en.wikipedia.org/wiki/Longest_repeated_substring_problem

Example
-------
After first 36 rows (21 rocks), there is a repeating pattern of 53 rows (at rock 56).

....#..
....#..
....#..
....#..
.##.#..
.##.#..
..###..
...#...
..###..
...#...
..####.
..###..
..###..
..####.
....###
.....#.
.#####.
.#..#..
.#..#..
.####.#
.####.#
###.###
.#####.
.###...
.###...
.#.#...
.#.#.#.
.######
.#####.
....#..
....#..
....#..
....#..
.##.#..
.##.#..
..###..
....#..
...###.
#...#..
#####..
#.#....
#.#....
####...
..#####
...#.##
..####.
.##....
.##...#
..#...#
..#.###
..#..#.
..#.###
.#####.

'''

TEST1 = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''

CHAMBER = {(x, 0): '#' for x in range(7)}
MIN_X = 0
MAX_X = 6
DY = 4


def rock1(y):
    return [
        (2, y + DY), (3,  y + DY), (4, y + DY), (5, y + DY)
    ]

def rock2(y):
    return [
                         (3, y + DY + 2),
        (2, y + DY + 1), (3, y + DY + 1), (4, y + DY + 1),
                         (3, y + DY)
    ]

def rock3(y):
    return [
                                  (4, y + DY + 2),
                                  (4, y + DY + 1),
        (2, y + DY), (3, y + DY), (4, y + DY),
    ]

def rock4(y):
    return [
        (2, y + DY + 3),
        (2, y + DY + 2),
        (2, y + DY + 1),
        (2, y + DY),
    ]

def rock5(y):
    return [
        (2, y + DY + 1), (3, y + DY + 1),
        (2, y + DY), (3, y + DY)
    ]

ROCKS = [rock1, rock2, rock3, rock4, rock5]


def make_jet(s):
    return cycle((i, si) for i, si in enumerate(s))


def make_rocks(rfunc):
    return cycle((i, r) for i, r in enumerate(rfunc))


def draw(chamber, rock):
    xs = []
    ys = []
    for x, y in chamber.keys():
        xs.append(x)
        ys.append(y)
    for x, y in rock:
        xs.append(x)
        ys.append(y)
    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    rows = []
    for y in range(ymax, ymin - 1, -1):
        row = []
        for x in range(xmin, xmax + 1):
            l = chamber.get((x, y), '.')
            row.append(l)
            if (x, y) in rock:
                row[-1] = '@'
        rows.append(''.join(row))
    return '\n'.join(rows)


def can_push(r, chamber):
    for ri in r:
        if ri in chamber:
            return False
        xi = ri[0]
        if xi < MIN_X or xi > MAX_X:
            return False
    return True


def push(r, j, chamber):
    dx = -1 if j == '<' else 1
    r1 = [(x + dx, y) for x, y in r]
    if can_push(r1, chamber):
        return r1
    return r


def can_move(r, chamber):
    for ri in r:
        if ri in chamber:
            return False
    return True


def move(r, chamber):
    r1 = [(x, y - 1) for x, y in r]
    if can_move(r1, chamber):
        return r1, True
    else:
        return r, False


def hit_test(r, chamber):
    for ri in r:
        if ri in chamber:
            return 2
        xi = ri[0]
        if xi < MIN_X or xi > MAX_X:
            return 1
    return 0


def fall(i, r, ri, jet, chamber):
    did_move = True
    while did_move:
        ji, j = next(jet)
        # print(ji, j)
        # if ri == 0 and ji == 0:
        #     print('Zeroth rock and zeroth jet', i)
        r = push(r, j, chamber)
        r, did_move = move(r, chamber)
    return r


def merge(r, chamber):
    for ri in r:
        chamber[ri] = '#'


def get_max_y(chamber):
    return max(y for _, y in chamber.keys())


def part1(s):
    jet = make_jet(s)
    rocks = make_rocks(ROCKS)
    chamber = CHAMBER.copy()

    ys = []
    for i in range(1, 2022 + 1):
        max_y = get_max_y(chamber)

        ri, rfunc = next(rocks)
        r = rfunc(max_y)
        r = fall(i, r, ri, jet, chamber)
        merge(r, chamber)

        max_y = get_max_y(chamber)
        ys.append(max_y)

    with open('t17.txt', 'w') as g:
        y_previous = 0
        for i, y in enumerate(ys):
            dy = y - y_previous
            y_previous = y
            g.write(f'{dy}')

    return get_max_y(chamber)


def main():
    s = get_input('17')
    # s = TEST1.strip()

    p1 = part1(s)

    print('Part 1:', p1)


if __name__ == '__main__':
    main()
