
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


class Vertex:
    def __init__(self, p):
        self.p = p
        self.visited = False

    def __repr__(self) -> str:
        return f'V({self.p}, {self.visited})'

    def __hash__(self) -> int:
        return hash(self.p)


def parse(d):
    for line in d.split('\n'):
        p = tuple(int(x) for x in line.split(','))
        yield Vertex(p)


def manhattan(v1, v2):
    x1, y1, z1, t1 = v1.p
    x2, y2, z2, t2 = v2.p
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1) + abs(t2 - t1)


def make_graph(vs):
    graph = defaultdict(list)
    for v1, v2 in combinations(vs, 2):
        if manhattan(v1, v2) <= 3:
            graph[v1].append(v2)
            graph[v2].append(v1)
    return graph


def dfs(graph, start):
    stack = [start]
    seen = set()
    while stack:
        v = stack.pop()
        v.visited = True

        if v in seen:
            continue
        seen.add(v)

        for vv in graph[v]:
            stack.append(vv)


def count_components(graph, vertices):
    count = 0
    for v in vertices:
        if not v.visited:
            count += 1
            dfs(graph, v)
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