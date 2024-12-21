
from collections import defaultdict
import heapq

from geometry import NEXT_DIRECTIONS, LEFT, RIGHT, UP, DOWN
from help import get_input

test1 = '''###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############'''

test2 = '''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################'''

def parse(source):
    map_ = set()
    start = None
    end = None
    for r, row in enumerate(source.split('\n')):
        for c, ch in enumerate(row):
            if ch == '.':
                map_.add((r, c))
            elif ch == 'S':
                map_.add((r, c))
                start = r, c
            elif ch == 'E':
                map_.add((r, c))
                end = r, c
    return start, end, map_


def get_next(p, d, map_):
    for dd in NEXT_DIRECTIONS[d]:
        yield p, dd, 1000
    r, c = p
    dr, dc = d
    rr = r + dr
    cc = c + dc
    pp = rr, cc
    if pp in map_:
        yield pp, d, 1


def search(start, direction, end, map_):
    seen = {(start, direction): 0}
    q = [(0, start, direction)]
    children = defaultdict(set)
    while q:
        t, p, d = heapq.heappop(q)

        for pp, dd, dt in get_next(p, d, map_):
            tt = t + dt
            x = pp, dd
            if x not in seen or tt <= seen[x]:
                children[x].add((p, d))
                seen[(pp, dd)] = tt
                heapq.heappush(q, (tt, pp, dd))

    return children


# source = test1.strip()
# source = test2.strip()
source = get_input(16)
start, end, map_ = parse(source)

children = search(start, RIGHT, end, map_)
print(start, end)

x = end, UP
seen = set([x])
parents = [x]
while parents:
    new_parents = []
    for p in parents:
        cs = children[p]
        for c in cs:
            if c not in seen:
                new_parents.append(c)
                seen.add(c)
    parents = new_parents


a = set(x[0] for x in seen)
print(len(a))
