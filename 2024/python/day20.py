
from collections import Counter
import heapq

from geometry import UP, DOWN, LEFT, RIGHT, DIRECTIONS
from help import get_input

test1 = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''

VERTICAL = [UP, DOWN]
HORIZONTAL = [LEFT, RIGHT]


def parse(source):
    map_ = {}
    start = None
    end = None
    for r, row in enumerate(source.split('\n')):
        for c, ch in enumerate(row):
            if ch == 'S':
                ch = '.'
                start = r, c
            elif ch == 'E':
                ch = '.'
                end = r, c
            map_[(r, c)] = ch
    return map_, start, end


def get_shortcut_neighbours(p, directions, map_):
    r, c = p
    ps = []
    for dr, dc in directions:
        rr = r + dr
        cc = c + dc
        pp = rr, cc
        ch = map_.get(pp, None)
        if ch == '.':
            ps.append(pp)
        else:
            return None, None
    return tuple(ps)


def get_shortcuts(map_):
    for p, ch in map_.items():
        if ch != '#':
            continue
        # print('checking shortcut for', p)
        for directions in (HORIZONTAL, VERTICAL):
            p1, p2 = get_shortcut_neighbours(p, directions, map_)
            if p1 is not None and p2 is not None:
                yield p1, p, p2


def get_neighbours(p, map_):
    r, c = p
    for dr, dc in DIRECTIONS:
        rr = r + dr
        cc = c + dc
        pp = rr, cc
        ch = map_.get(pp, '')
        if ch == '.':
            yield pp


def bfs(start, end, map_):
    distances = {}
    seen = set([start])
    q = [(0, start)]
    while q:
        t, p = heapq.heappop(q)
        distances[p] = t
        for pp in get_neighbours(p, map_):
            if pp not in seen:
                seen.add(pp)
                heapq.heappush(q, (t + 1, pp))
    return distances


# source = test1.strip()
source = get_input(20)

map_, start, end = parse(source)

distances = bfs(start, end, map_)

counter = Counter()
for p1, p, p2 in get_shortcuts(map_):
    d1 = distances[p1]
    d2 = distances[p2]
    d = abs(d1 - d2) - 2
    counter[d] += 1


t = 0
for k in sorted(counter.keys()):
    if k >= 100:
        t += counter[k]

print(t)

