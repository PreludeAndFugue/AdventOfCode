
from itertools import combinations

from help import get_input

TEST = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''

TEST_EXPAND = '''....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......'''


def expand(x):
    def e(rows):
        y = []
        for row in rows:
            s = set(row)
            y.append(row)
            if len(s) == 1:
                y.append(tuple('.' for _ in range(len(row))))
        return y
    x = e(x)
    x = list(zip(*x))
    x = e(x)
    x = list(zip(*x))
    return x


def get_galaxies(x):
    galaxies = []
    for r, row in enumerate(x):
        for c, ch in enumerate(row):
            if ch == '#':
                galaxies.append((r, c))
    return galaxies


def distance(galaxies):
    total_d = 0
    for g1, g2 in combinations(galaxies, 2):
        r1, c1 = g1
        r2, c2 = g2
        d = abs(r1 - r2) + abs(c1 - c2)
        total_d += d
    return total_d


def expand_2(galaxies, empty_r, empty_c, n):
    expanded_galaxies = []
    for galaxy in galaxies:
        r, c = galaxy
        extra_r = (n - 1)*sum(1 for m in empty_r if m < r)
        extra_c = (n - 1)*sum(1 for m in empty_c if m < c)
        expanded_galaxies.append((r + extra_r, c + extra_c))
    return expanded_galaxies


def part1(x):
    x = expand(x)

    # test = '\n'.join(''.join(a) for a in x)
    # assert test == TEST_EXPAND

    galaxies = get_galaxies(x)
    return distance(galaxies)


def part2(x):
    empty_r = set()
    for r, row in enumerate(x):
        if len(set(row)) == 1:
            empty_r.add(r)

    empty_c = set()
    for c, row in enumerate(zip(*x)):
        if len(set(row)) == 1:
            empty_c.add(c)

    galaxies = get_galaxies(x)
    expanded_galaxies = expand_2(galaxies, empty_r, empty_c, 1_000_000)
    return distance(expanded_galaxies)


d = get_input('11').strip()
# d = TEST.strip()
x = [tuple(a) for a in d.split('\n')]

p1 = part1(x)
print(p1)

p2 = part2(x)
print(p2)
