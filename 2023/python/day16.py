
from collections import deque

from help import get_input

TEST = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''


d = get_input('16').strip()
# d = TEST.strip()
map_ = {}
for r, row in enumerate(d.split('\n')):
    for c, ch in enumerate(row):
        map_[(r, c)] = ch

# Direction: change in coordinates
D = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}
# Change in coordinates: direction
DD = {v: k for k, v in D.items()}
# Mirrors
M = {
    'R': {
        '/': (-1, 0),
        '\\': (1, 0)
    },
    'L': {
        '/': (1, 0),
        '\\': (-1, 0)
    },
    'U': {
        '/': (0, 1),
        '\\': (0, -1)
    },
    'D':
    {
        '/': (0, -1),
        '\\': (0, 1)
    }
}
# Splitters
S = {
    'R': {'|': ((-1, 0), (1, 0))},
    'L': {'|': ((-1, 0), (1, 0))},
    'U': {'-': ((0, -1), (0, 1))},
    'D': {'-': ((0, -1), (0, 1))}
}

def print_map(map_, items):
    points = set(p for p, _ in items)
    rs = [r for r, _ in map_.keys()]
    cs = [c for _, c in map_.keys()]
    r_max = max(rs)
    c_max = max(cs)
    rows = []
    for r in range(r_max + 1):
        row = []
        for c in range(c_max + 1):
            p = r, c
            if p in points:
                row.append('#')
            else:
                row.append('.')
        rows.append(''.join(row))
    return '\n'.join(rows)


def energise(start, map_):
    q = deque([start])
    # unique positions, direcion pairs the light has been.
    seen = set()

    while q:
        item = q.popleft()

        if item in seen:
            continue

        p, d = item
        r, c = p
        g = map_.get(p, None)

        if g is None:
            continue
        elif g == '.':
            dr, dc = D[d]
            rr = r + dr
            cc = c + dc
            q.append(((rr, cc), d))
        elif g == '\\' or g == '/':
            dp = M[d][g]
            dd = DD[dp]
            dr, dc = dp
            rr = r + dr
            cc = c + dc
            q.append(((rr, cc), dd))
        elif g == '-' or g == '|':
            ds = S[d].get(g, None)
            if ds is None:
                dr, dc = D[d]
                rr = r + dr
                cc = c + dc
                q.append(((rr, cc), d))
            else:
                for dp in S[d][g]:
                    dd = DD[dp]
                    dr, dc = dp
                    rr = r + dr
                    cc = c + dc
                    q.append(((rr, cc), dd))
        else:
            raise ValueError

        seen.add(item)

    seen_p = set(p for p, d in seen)
    return len(seen_p)

def part2(map_):
    rs = [r for r, _ in map_.keys()]
    cs = [c for _, c in map_.keys()]
    r_max = max(rs)
    c_max = max(cs)
    es = []
    for r in range(r_max + 1):
        for c in range(c_max + 1):
            ds = []
            if r == 0:
                ds.append('D')
            if r == r_max:
                ds.append('U')
            if c == 0:
                ds.append('R')
            if c == c_max:
                ds.append('L')
            if ds:
                for d in ds:
                    start = (r, c), d
                    e = energise(start, map_)
                    es.append(e)
    return max(es)


p1 = energise(((0, 0), 'R'), map_)
print(p1)

p2 = part2(map_)
print(p2)
