
import heapq

from geometry import DIRECTIONS
from help import get_input

test1 = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''


def parse(source):
    coords = []
    for line in source.split('\n'):
        a, b = line.split(',')
        a = int(a)
        b = int(b)
        coords.append((a, b))
    return coords


def get_neighbours(p, map_):
    x, y = p
    for d in DIRECTIONS:
        # print(x, y)
        dx, dy = d
        xx = x + dx
        yy = y + dy
        pp = xx, yy
        ch = map_.get(pp, '#')
        if ch == '.':
            yield pp


def search(start, end, map_):
    seen = set([start])
    q = [(0, start)]
    while q:
        d, p = heapq.heappop(q)
        # print(d, p)
        if p == end:
            return d
        for pp in get_neighbours(p, map_):
            if pp not in seen:
                seen.add(pp)
                heapq.heappush(q, (d + 1, pp))
    return None


# source = test1.strip()
source = get_input(18)
coords = parse(source)
# print(coords)

D = 70
N = 1024
NN = 3451
start = 0, 0
end = D, D

map_ = {}
for x in range(D + 1):
    for y in range(D + 1):
        p = x, y
        map_[p] = '.'

# for p in coords:
#     map_[p] = '#'

for i in range(N, NN):
    m = map_.copy()
    for p in coords[:i]:
        m[p] = '#'
    s = search(start, end, m)
    print(i, s, coords[i])
    if s is None:
        break
