
from collections import defaultdict, Counter
import heapq

from geometry import DIRECTIONS, UP, DOWN, LEFT, RIGHT
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

test4 = '''EEEEE
EXXXX
EEEEE
EXXXX
EEEEE'''

test5 = '''AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA'''


def parse(source):
    map_ = {}
    for r, row in enumerate(source.split('\n')):
        for c, ch in enumerate(row):
            map_[(r, c)] = ch
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


def get_neighbours2(p, ch, map_):
    r, c = p
    for dr, dc in DIRECTIONS:
        rr = r + dr
        cc = c + dc
        pp = rr, cc
        chh = map_.get(pp, '')
        if chh == ch:
            yield pp


def get_region(p, map_):
    ch = map_[p]
    q = [p]
    seen = set([p])
    while q:
        p = heapq.heappop(q)
        for pp in get_neighbours2(p, ch, map_):
            if pp not in seen:
                seen.add(pp)
                heapq.heappush(q, pp)
    return seen


def get_regions(map_):
    regions = []
    while map_:
        p = sorted(map_.keys())[0]
        r = get_region(p, map_)
        regions.append(r)
        for p in r:
            map_.pop(p)
    return regions


def count(region):
    region = sorted(region)
    check = set(region)
    rs = [r for r, _ in region]
    cs = [c for _, c in region]
    r_min = min(rs)
    r_max = max(rs)
    c_min = min(cs)
    c_max = max(cs)

    inside = False
    ins = set()
    outs = set()
    fences = 0
    for r in range(r_min, r_max + 1):
        current_ins = set()
        current_outs = set()
        for c in range(c_min, c_max + 1):
            p = r, c
            if p in check:
                if not inside:
                    inside = True
                    current_ins.add(c)
                    if c not in ins:
                        fences += 1
            else:
                if inside:
                    inside = False
                    current_outs.add(c)
                    if c not in outs:
                        fences += 1

        if inside:
            inside = False
            current_outs.add(c + 1)
            if (c + 1) not in outs:
                fences += 1

        ins = current_ins
        outs = current_outs

    inside = False
    ins = set()
    outs = set()
    for c in range(c_min, c_max + 1):
        current_ins = set()
        current_outs = set()
        for r in range(r_min, r_max + 1):
            p = r, c
            if p in check:
                if not inside:
                    inside = True
                    current_ins.add(r)
                    if r not in ins:
                        fences += 1
            else:
                if inside:
                    inside = False
                    current_outs.add(r)
                    if r not in outs:
                        fences += 1

        if inside:
            inside = False
            current_outs.add(r + 1)
            if (r + 1) not in outs:
                fences += 1

        ins = current_ins
        outs = current_outs

    return fences * len(region)


def part2():
    # source = test1.strip()
    # source = test2.strip()
    # source = test3.strip()
    # source = test4.strip()
    # source = test5.strip()
    source = get_input(12)
    map_ = parse(source)
    regions = get_regions(map_)
    s = 0
    for region in regions:
        c = count(region)
        s += c
    print(s)


# part1()
part2()
