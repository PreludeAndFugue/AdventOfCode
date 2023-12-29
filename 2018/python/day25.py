
from collections import defaultdict
from itertools import combinations

from help import get_input


TEST_1 = '''
0,0,0,0
 3,0,0,0
 0,3,0,0
 0,0,3,0
 0,0,0,3
 0,0,0,6
 9,0,0,0
12,0,0,0
'''

TEST_2 = '''
-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0
'''

TEST_3 = '''
1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2
'''

TEST_4 = '''
1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2
'''


def parse(d):
    for line in d.split('\n'):
        p = tuple(int(x) for x in line.split(','))
        yield p


def manhattan(p1, p2):
    x1, y1, z1, t1 = p1
    x2, y2, z2, t2 = p2
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1) + abs(t2 - t1)


def make_graph(ps):
    graph = defaultdict(list)
    for p1, p2 in combinations(ps, 2):
        if manhattan(p1, p2) <= 3:
            graph[p1].append(p2)
            graph[p2].append(p1)
    return graph


def dfs(graph, start, visited):
    stack = [start]
    seen = set()
    while stack:
        v = stack.pop()
        visited[v] = True

        if v in seen:
            continue
        seen.add(v)

        for vv in graph[v]:
            stack.append(vv)


def count_components(graph, vertices):
    visited = {v: False for v in vertices}
    count = 0
    for v in vertices:
        if not visited[v]:
            count += 1
            dfs(graph, v, visited)
    return count


def main():
    d = get_input('25').strip()
    # d = TEST_3.strip()

    vs = list(parse(d))
    graph = make_graph(vs)

    c = count_components(graph, vs)
    print(c)


if __name__ == '__main__':
    main()