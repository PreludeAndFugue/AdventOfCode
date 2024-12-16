
import heapq

from geometry import NEXT_DIRECTIONS, RIGHT
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
    seen = set([(start, direction)])
    q = [(0, start, direction)]
    while q:
        t, p, d = heapq.heappop(q)
        # print(t, p, d)

        if p == end:
            return t
        for pp, dd, dt in get_next(p, d, map_):
            x = pp, dd
            if x not in seen:
                seen.add(x)
                # print('\tadding', t + dt, pp, dd)
                heapq.heappush(q, (t + dt, pp, dd))


# source = test1.strip()
# source = test2.strip()
source = get_input(16)
start, end, map_ = parse(source)

# print(start, end)
# print(map_)

s = search(start, RIGHT, end, map_)
print(s)
