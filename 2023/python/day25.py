
from collections import Counter, defaultdict, deque
import heapq
from random import choice

from help import get_input

'''
https://en.wikipedia.org/wiki/Minimum_cut
https://en.wikipedia.org/wiki/Karger%27s_algorithm
https://en.wikipedia.org/wiki/Kernighan–Lin_algorithm
https://en.wikipedia.org/wiki/Stoer–Wagner_algorithm

Most common edges:
mfc -- vph
fql -- rmg
sfm -- vmt

'''


TEST = '''
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
'''

def parse(d):
    vertices = set()
    graph = defaultdict(set)

    # f = open('graph25.txt', 'w')

    for line in d.split('\n'):
        a, b = line.split(': ')
        c = b.split(' ')
        vertices.add(a)

        for x in c:
            vertices.add(x)
            graph[a].add(x)
            graph[x].add(a)

            # print(a, '--', x)
            # f.write(f'{a} -- {x}\n')
    return graph


def bfs(start, end, graph):
    # print('start', start, 'end', end)
    q = [(0, start, [start])]
    seen = set()


    prev = {}
    for v in graph.keys():
        prev[v] = None

    while q:
        d, v, path = heapq.heappop(q)

        # print('current', v, d)
        # print('seen', seen)

        if v == end:
            return path

        if v in seen:
            continue
        seen.add(v)

        for vv in graph[v]:
            p = path.copy()
            p.append(vv)
            heapq.heappush(q, (d + 1, vv, p))
            # print('\tprevious', vv, '<-', v)
            prev[vv] = v

    print('len seen', len(seen))


def contract(graph):
    '''https://en.wikipedia.org/wiki/Karger%27s_algorithm'''
    v1 = choice(list(graph.keys()))
    v1_n = graph[v1]
    v2 = choice(list(v1_n))
    v2_n = graph[v2]
    v_new = ''.join(sorted([v1, v2]))
    avoid = set([v1, v2])

    print('contract', v1, v2)

    for vv in v1_n:
        if vv in avoid: continue
        graph[v_new].add(vv)
        graph[vv].add(v_new)
        graph[vv].remove(v1)

    for vv in v2_n:
        if vv in avoid: continue
        graph[v_new].add(vv)
        graph[vv].add(v_new)
        graph[vv].remove(v2)

    del graph[v1]
    del graph[v2]


PAIRS = [
    ('mfc', 'vph'),
    ('fql', 'rmg'),
    ('sfm', 'vmt')
]

PAIRS_TEST = [
    ('bvb', 'cmg'),
    ('hfx', 'pzl'),
    ('jqt', 'nvd')
]

def main():
    d = get_input('25').strip()
    # d = TEST.strip()

    graph = parse(d)
    # print(graph)
    # for v1, v2 in PAIRS:
    # # for v1, v2 in PAIRS_TEST:
    #     graph[v1].remove(v2)
    #     graph[v2].remove(v1)
    # print(graph)

    # bfs('bvb', None, graph)

    vs = list(graph.keys())

    counter = Counter()
    for _ in range(1_000):
        v1 = choice(vs)
        v2 = choice(vs)
        path = bfs(v1, v2, graph)
        for v in path:
            counter[v] += 1
    # path = make_path(previous, v2)
    # print(v1, v2, path)
    print(counter.most_common(7))


if __name__ == '__main__':
    main()
