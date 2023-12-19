from collections import deque
from enum import Enum

from help import get_input

'''
Answers
29627: too high

INSIDE (-207, 186)
'''

TEST = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''


D = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}


def print_map(map_):
    rs = [r for r, _ in map_.keys()]
    cs = [c for _, c in map_.keys()]
    r_min = min(rs)
    r_max = max(rs)
    c_min = min(cs)
    c_max = max(cs)
    rows = []
    for r in range(r_min, r_max + 1):
        row = []
        for c in range(c_min, c_max + 1):
            p = r, c
            if p in map_:
                row.append('#')
            else:
                row.append('.')
        rows.append(''.join(row))
    return '\n'.join(rows)


def make_map(d):
    map_ = {}
    r, c = 0, 0

    for l in d.split('\n'):
        d, n, colour = l.split(' ')
        n = int(n)
        colour = colour.strip('()#')

        dr, dc = D[d]
        for _ in range(n):
            r += dr
            c += dc
            map_[r, c] = colour
    return map_


def flood_fill(d):
    map_ = make_map(d)
    for k in map_.keys():
        map_[k] = '#'
    start = (-207, 186)
    q = deque()
    q.append(start)
    while q:
        r, c = q.popleft()
        for dr, dc in D.values():
            rr, cc = r + dr, c + dc
            p = map_.get((rr, cc), '.')
            if p == '.':
                map_[(rr, cc)] = '#'
                q.append((rr, cc))
    return map_


d = get_input('18').strip()
# d = TEST.strip()

map_ = flood_fill(d)
print(len(map_))
