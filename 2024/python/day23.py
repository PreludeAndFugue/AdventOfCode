
from collections import defaultdict
from itertools import combinations

from graphs import find_cliques
from help import get_input

test1 = '''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn'''

test2 = '''
1-2
2-3
3-6
6-5
5-4
4-1'''

test3 = '''
1-2
2-3
3-1
3-4
4-5
5-3'''


def parse(source):
    map_ = defaultdict(list)
    for line in source.split('\n'):
        a, b = line.split('-')
        map_[a].append(b)
        map_[b].append(a)
    return map_



# source = test1.strip()
# source = test2.strip()
# source = test3.strip()
source = get_input(23)
map_ = parse(source)
# print(map_)


def depth_3_paths(start, map_):
    d0 = [[start]]
    d1 = []
    d2 = []
    d3 = []

    for path in d0:
        p = path[-1]
        for pp in map_[p]:
            path_ = path.copy()
            path_.append(pp)
            d1.append(path_)

    for path in d1:
        p = path[-1]
        for pp in map_[p]:
            if pp == path[0]:
                continue
            path_ = path.copy()
            path_.append(pp)
            d2.append(path_)

    for path in d2:
        p = path[-1]
        for pp in map_[p]:
            if pp == path[1]:
                continue
            path_ = path.copy()
            path_.append(pp)
            d3.append(path_)

    for p in d3:
        if p[3] == p[0]:
            yield tuple(sorted(p[:3]))


cycles = set()
for k in map_.keys():
    for p in depth_3_paths(k, map_):
        cycles.add(p)

t = 0
for cycle in cycles:
    # print(cycle)
    for s in cycle:
        if s.startswith('t'):
            # print('\thas t')
            t += 1
            break
print(t)


c = find_cliques(map_)
c.sort(key=len)
cl = c[-1]
print(','.join(sorted(cl)))
