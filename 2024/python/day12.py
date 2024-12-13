
from collections import defaultdict
import heapq

from geometry import DIRECTIONS
from help import get_input

test1 = '''AAAA
BBCD
BBCC
EEEC'''

test2 = '''OOOOO
OXOXO
OOOOO
OXOXO
OOOOO'''

test3 = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''


def parse(source):
    map_ = defaultdict(set)
    for r, row in enumerate(source.split('\n')):
        for c, ch in enumerate(row):
            map_[ch].add((r, c))
    return map_


def get_neighbours(p, ps):
    r, c = p
    for dp in DIRECTIONS:
        dr, dc, = dp
        rr = r + dr
        cc = c + dc
        pp = rr, cc
        if pp in ps:
            yield pp


def search(ps):
    pps = ps.copy()

    results = []

    while pps:
        start = pps.pop()
        q = [start]
        seen = set([start])
        edges = set()
        while q:
            p = heapq.heappop(q)
            for pp in get_neighbours(p, ps):
                edges.add(tuple(sorted([p, pp])))
                if pp not in seen:
                    seen.add(pp)
                    heapq.heappush(q, pp)

        area = len(seen)
        perimeter = 4*area - 2*len(edges)
        results.append((perimeter, area))
        pps = pps - seen
        seen = set()
        edges = set()

    t = 0
    for perimeter, area in results:
        t += perimeter*area
    return t



def part1():
    # source = test1.strip()
    source = get_input(12)

    map_ = parse(source)

    t = 0
    for k, v in map_.items():
        x = search(v)
        t += x
    print(t)


def part2():
    source = test1.strip()


# part1()
part2()
