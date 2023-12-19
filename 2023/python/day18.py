from collections import deque
from enum import Enum

from help import get_input

'''
Answers
29627: too high

INSIDE (-207, 186)

Part 2
129373114893213: too low

Example to help calculate area
------------------------------

R4, D3, R2, D4, L5, U2, L1, U5

S is start position

(0, 0), (4, 0), (4, 3), (6, 3), (6, 7),
(1, 7), (1, 4), (0, 4) -> (0, 0)

Then based on these coordinates
area: 33
perimeter: 26

But we are digging out 1 metre square holes.
The following diagram shows the boundary, wher
I: point inside the boundary of polygon
O: point outside the boundary of polygon

Area of dig: A + P/2 + 1

SIIIO
I   O
I   O
I   IIO
OI    O
 I    O
 I    O
 OOOOOO
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

D_2 = {
    # right
    0: (0, 1),
    # left
    2: (0, -1),
    # up
    3: (-1, 0),
    # down
    1: (1, 0)
}
D_2_A = {
    0: 'R', 2: 'L', 3: 'U', 1: 'D'
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


def make_map_2(d):
    map_ = [(0, 0)]
    r, c = 0, 0

    last_d = None

    for l in d.split('\n'):
        _, _, colour = l.split(' ')
        colour = colour.strip('()#')

        d = colour[-1]
        d = int(d)
        n = colour[:-1]
        n = int(n, base=16)

        if last_d is not None:
            dd = abs(d - last_d)
            assert dd % 2
        last_d = d

        # print(d, D_2[d], D_2_A[d], n)
        dr, dc = D_2[d]
        r += n*dr
        c += n*dc
        map_.append((r, c))
    return map_


def area(ps):
    '''
    https://stackoverflow.com/a/2432482/132767
    https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon

    '''
    a = 0
    for p1, p2 in zip(ps, ps[1:] + [ps[0]]):
        x1, y1 = p1
        x2, y2 = p2
        a += x1*y2
        a -= y1*x2
    # print(abs(a))
    return abs(a/2)


def area_2(ps):
    '''
    https://www.topcoder.com/thrive/articles/Geometry%20Concepts%20part%201:%20Basic%20Concepts#PolygonArea

    //We will triangulate the polygon
    //into triangles with points p[0],p[i],p[i+1]

    for (int i = 1; i + 1 < N; i++) {
    int x1 = p[i][0] - p[0][0];
    int y1 = p[i][1] - p[0][1];
    int x2 = p[i + 1][0] - p[0][0];
    int y2 = p[i + 1][1] - p[0][1];
    int cross = x1y2 - x2y1;
    area += cross;
    }
    return abs(area / 2);
    '''
    x0, y0 = ps[0]
    a = 0
    for pi, pj in zip(ps[1:], ps[2:]):
        # print(x0, y0, pi, pj)
        x1 = pi[0] - x0
        y1 = pi[1] - y0
        x2 = pj[0] - x0
        y2 = pj[1] - y0
        cross = x1*y2 - x2*y1
        a += cross
    return abs(a / 2)


def perimeter(ps):
    ps = ps + [ps[0]]
    p = 0
    for p1, p2 in zip(ps, ps[1:]):
        r1, c1 = p1
        r2, c2 = p2
        dr = abs(r2 - r1)
        dc = abs(c2 - c1)
        d = dr + dc
        p += d
    return p


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

ps = make_map_2(d)

a = area(ps)
p = perimeter(ps)

print(a + p/2 + 1)
