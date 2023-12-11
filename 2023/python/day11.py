
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


d = get_input('11').strip()
# d = TEST.strip()
x = [tuple(a) for a in d.split('\n')]
x = expand(x)

# test = '\n'.join(''.join(a) for a in x)
# assert test == TEST_EXPAND

galaxies = []
for r, row in enumerate(x):
    for c, ch in enumerate(row):
        if ch == '#':
            galaxies.append((r, c))

total_d = 0
for g1, g2 in combinations(galaxies, 2):
    r1, c1 = g1
    r2, c2 = g2
    d = abs(r1 - r2) + abs(c1 - c2)
    total_d += d

print(total_d)
