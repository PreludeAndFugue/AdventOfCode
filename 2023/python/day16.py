
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

# print(map_)


D = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}
DD = {
    (0, 1): 'R',
    (0, -1): 'L',
    (-1, 0): 'U',
    (1, 0): 'D'
}
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
S = {
    'R': {'|': ((-1, 0), (1, 0))},
    'L': {'|': ((-1, 0), (1, 0))},
    'U': {'-': ((0, -1), (0, 1))},
    'D': {'-': ((0, -1), (0, 1))}
}

def print_map(map_, items):
    points = set(p for p, d in items)
    rs = [r for r, c in map_.keys()]
    cs = [c for r, c in map_.keys()]
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


start = ((0, 0), 'R')
q = deque([start])
# unique positions the light has been.
seen = set()

while q:
    item = q.popleft()

    if item in seen:
        continue

    p, d = item
    r, c = p
    g = map_.get(p, None)
    # print(p, d, g)

    # print(g)

    # print(print_map(map_, seen))
    # input()

    if g is None:
        # print('g is None')
        continue
    elif g == '.':
        dr, dc = D[d]
        rr = r + dr
        cc = c + dc
        # print('\t',r, c,  dr, dc, rr, cc)
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

    # print('adding item to seen', item)
    seen.add(item)

# print(seen)
seen_p = set(p for p, d in seen)
print(len(seen_p))

# print(print_map(map_, seen))
