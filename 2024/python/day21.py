
from collections import defaultdict
from functools import cache
import heapq
from itertools import permutations

from geometry import UP, DOWN, LEFT, RIGHT, DIRECTIONS
from help import get_input

test1 = '''029A
980A
179A
456A
379A'''


NUMERIC_KEYPAD = '''
789
456
123
 0A'''

DIRECTIONAL_KEYPAD = '''
 ^A
<v>'''

DD = {
    UP: '^',
    DOWN: 'v',
    LEFT: '<',
    RIGHT: '>'
}

def make_map(keypad):
    map_ = {}
    for r, row in enumerate(keypad.split('\n')):
        for c, ch in enumerate(row):
            if ch == ' ':
                continue
            map_[ch] = r, c
    return map_


def get_neighbours(p, map_):
    r, c = p
    for dr, dc in DIRECTIONS:
        rr = r + dr
        cc = c + dc
        pp = rr, cc
        if pp in map_:
            yield pp


def make_paths(parents, path, start, end):
    if not path:
        path = [end]
    end = path[-1]
    next_values = parents[end]
    if not next_values:
        yield list(reversed(path))
    for p in next_values:
        pp = path.copy()
        pp.append(p)
        if p == start:
            yield list(reversed(pp))
        else:
            yield from make_paths(parents, pp, start, end)


def make_directions(path):
    directions = []
    for p1, p2 in zip(path, path[1:]):
        r1, c1 = p1
        r2, c2 = p2
        dr = r2 - r1
        dc = c2 - c1
        d = dr, dc
        directions.append(DD[d])
    return directions


def bfs(start, map_):
    seen = set([start])
    q = [(0, start)]
    parents = defaultdict(set)
    distances = defaultdict(lambda: 1_000_000_000)
    distances[start] = 0
    while q:
        d, p = heapq.heappop(q)
        for pp in get_neighbours(p, map_):
            if pp not in seen or distances[pp] >= d + 1:
                seen.add(pp)
                parents[pp].add(p)
                distances[pp] = d + 1
                heapq.heappush(q, (d + 1, pp))
    return parents


num_map = make_map(NUMERIC_KEYPAD)
num_map_inverse = {v: k for k, v in num_map.items()}
dir_map = make_map(DIRECTIONAL_KEYPAD)
dir_map_inverse = {v: k for k, v in dir_map.items()}

num_map_paths = {}
for n1 in num_map.keys():
    p1 = num_map[n1]
    parents = bfs(p1, num_map_inverse)
    for n2 in num_map.keys():
        if n2 == n1:
            continue
        p2 = num_map[n2]
        paths = list(make_paths(parents, [], p1, p2))
        num_map_paths[(n1, n2)] = paths
num_map_paths = {k: [''.join(make_directions(p)) for p in v] for k, v in num_map_paths.items()}


dir_map_paths = {}
for n1 in dir_map.keys():
    p1 = dir_map[n1]
    parents = bfs(p1, dir_map_inverse)
    for n2 in dir_map.keys():
        if n2 == n1:
            continue
        p2 = dir_map[n2]
        paths = list(make_paths(parents, [], p1, p2))
        dir_map_paths[(n1, n2)] = paths
dir_map_paths = {k: [''.join(make_directions(p)) for p in v] for k, v in dir_map_paths.items()}


def make_num_paths(num, path):
    if len(num) < 2:
        yield path
    else:
        start = num[0]
        end = num[1]
        num = num[1:]
        sub_paths = num_map_paths[(start, end)]
        for sp in sub_paths:
            yield from make_num_paths(num, path + sp + 'A')


def make_dir_paths(dd, path):
    if len(dd) < 2:
        yield path
    else:
        start = dd[0]
        end = dd[1]
        dd = dd[1:]
        if start == end:
            yield from make_dir_paths(dd, path + 'A')
        else:
            sub_paths = dir_map_paths[(start, end)]
            for sp in sub_paths:
                yield from make_dir_paths(dd, path + sp + 'A')


def check(num):
    num = 'A' + num
    t = 1_000_000_000
    p1s = list(make_num_paths(num, ''))
    for p1 in p1s:
        for p2 in make_dir_paths('A' + p1, ''):
            for p3 in make_dir_paths('A' + p2, ''):
                t = min(t, len(p3))
    return t


t = 0
# source = test1.strip()
source = get_input(21)
for num in source.split('\n'):
    print(num)
    d = int(num[:-1])
    tt = check(num)
    t += d*tt
print(t)
