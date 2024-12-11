
from collections import defaultdict
import heapq

from help import get_input
from geometry import DIRECTIONS

test1 = '''0123
1234
8765
9876'''

test2 = '''...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9'''

test3 = '''..90..9
...1.98
...2..7
6543456
765.987
876....
987....'''

test4 = '''10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01'''

test5 = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

test6 = '''.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....'''

test7 = '''012345
123456
234567
345678
4.6789
56789.'''


def parse(source):
    map_ = {}
    trailheads = []
    for r, row in enumerate(source.split('\n')):
        for c, ch in enumerate(row):
            if ch.isdigit():
                n = int(ch)
                if n == 0:
                    trailheads.append((r, c))
                map_[(r, c)] = n
    return map_, trailheads


def get_neighbours(p, map_):
    r, c = p
    n = map_[p]
    for direction in DIRECTIONS:
        dr, dc = direction
        pp = r + dr, c + dc
        nn = map_.get(pp, -1)
        # if nn == 9:
        #     print('9', pp)
        if nn - 1 == n:
            yield pp


def bfs(start, map_, part1=True):
    parents = defaultdict(list)
    seen = set([start])
    q = [start]
    count = 0
    while q:
        p = heapq.heappop(q)
        n = map_[p]
        if n == 9:
            count += 1
        for pp in get_neighbours(p, map_):
            if pp not in seen:
                if part1:
                    seen.add(pp)
                parents[pp].append(p)
                heapq.heappush(q, pp)
    return count


def test():
    source = test1.strip()
    map_, trailheads = parse(source)
    assert len(trailheads) == 1
    s = sum(bfs(trailhead, map_) for trailhead in trailheads)
    assert s == 1

    source = test2.strip()
    map_, trailheads = parse(source)
    assert len(trailheads) == 1
    s = sum(bfs(trailhead, map_) for trailhead in trailheads)
    assert s == 2

    source = test3.strip()
    map_, trailheads = parse(source)
    assert len(trailheads) == 1
    s = sum(bfs(trailhead, map_) for trailhead in trailheads)
    assert s == 4

    source = test4.strip()
    map_, trailheads = parse(source)
    assert len(trailheads) == 2
    s = sum(bfs(trailhead, map_) for trailhead in trailheads)
    assert s == 3

    source = test5.strip()
    map_, trailheads = parse(source)
    assert len(trailheads) == 9
    s = sum(bfs(trailhead, map_) for trailhead in trailheads)
    assert s == 36


def part1():
    # source = test5.strip()
    source = get_input(10)

    map_, trailheads = parse(source)

    s1 = sum(bfs(t, map_) for t in trailheads)
    s2 = sum(bfs(t, map_, False) for t in trailheads)
    print(s1)
    print(s2)


# test()
part1()
