
from help import get_input

from collections import defaultdict
from itertools import combinations

test1 = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''


def parse(source):
    map_ = defaultdict(list)
    r_max = 0
    c_max = 0
    for r, row in enumerate(source.split('\n')):
        for c, ch in enumerate(row):
            r_max = r
            c_max = c
            if ch != '.':
                map_[ch].append((r, c))
    return map_, r_max, c_max


def get_antinodes(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    dr = r2 - r1
    dc = c2 - c1
    yield r1 - dr, c1 - dc
    yield r2 + dr, c2 + dc


def filter(antinodes, r_max, c_max):
    '''Remove antinodes that lie outside the bounds of the map.'''
    for p in antinodes:
        r, c = p
        if r < 0 or r > r_max or c < 0 or c > c_max:
            continue
        yield p


source = test1.strip()
source = get_input(8)
map_, r_max, c_max = parse(source)

antinodes = set()
for k, v in map_.items():
    for p1, p2 in combinations(v, 2):
        ans = list(get_antinodes(p1, p2))
        antinodes.update(ans)


antinodes = list(filter(antinodes, r_max, c_max))

print(len(antinodes))