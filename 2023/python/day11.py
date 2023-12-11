
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


def get_empty(x):
    empty_r = set()
    for r, row in enumerate(x):
        if len(set(row)) == 1:
            empty_r.add(r)

    empty_c = set()
    for c, row in enumerate(zip(*x)):
        if len(set(row)) == 1:
            empty_c.add(c)

    return empty_r, empty_c


def solve(galaxies, empty_r, empty_c, expand):
    expanded_galaxies = expand_2(galaxies, empty_r, empty_c, expand)
    return distance(expanded_galaxies)


d = get_input('11').strip()
# d = TEST.strip()
x = [tuple(a) for a in d.split('\n')]

galaxies = get_galaxies(x)
empty_r, empty_c = get_empty(x)

p1 = solve(galaxies, empty_r, empty_c, 2)
print(p1)

p2 = solve(galaxies, empty_r, empty_c, 1_000_000)
print(p2)
