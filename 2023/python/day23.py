
from collections import defaultdict, deque
from copy import copy
import heapq
from itertools import combinations

from help import get_input

'''
Part2
-----
4722 - too low
5662 - too low
6042 - too low
6310 - too low


Smaller graph connecting junctions (example graph in TEST).
GraphViz
--------
graph {
    "3, 11" -- "5, 3" [label=22]
    "3, 11" -- "11, 21" [label=30]
    "3, 11" -- "13, 13" [label=24]
    "5, 3" -- "13, 5" [label=22]
    "5, 3" -- "0, 1" [label=15]
    "11, 21" -- "13, 13" [label=18]
    "11, 21" -- "19, 19" [label=10]
    "13, 13" -- "13, 5" [label=12]
    "13, 13" -- "19, 13" [label=10]
    "13, 5" -- "19, 13" [label=38]
    "19, 19" -- "19, 13" [label=10]
    "19, 19" -- "22, 21" [label=5]
}
'''

TEST = '''
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
'''

D = {
    complex(1, 0): '>',
    complex(-1, 0): '<',
    complex(0, 1): 'v',
    complex(0, -1): '^'
}
DD = list(D.keys())

def make_map(d, part2=False):
    map_ = {}
    slides = set()
    for r, l in enumerate(d.split('\n')):
        for c, ch in enumerate(l):
            if ch != '#':
                map_[complex(c, r)] = '.' if part2 else ch
                if ch != '.':
                    # print(ch, 'slide')
                    slides.add(complex(c, r))
    x = {k: v for k, v in map_.items() if v == '.'}
    x = sorted(x.keys(), key=lambda z: z.imag)
    start = x[0]
    end = x[-1]
    return map_, start, end, slides


class State:
    def __init__(self, n, p, d, previous):
        '''
        n: number of steps
        p: position
        d: direction
        previous: previous state positions for this state
        '''
        self.n = n
        self.p = p
        self.d = d
        self.previous = previous

    def seen_key(self):
        return self.p, frozenset(self.previous)

    def __lt__(self, other):
        return (-self.n, self.p.real, self.p.imag) < (-other.n, other.p.real, other.p.imag)

    def __repr__(self):
        d = D[self.d]
        return f'S({self.n}, {self.p}, {d}, {len(self.previous)})'


def get_next(state, map_, slides):
    ch = map_[state.p]
    D = {
        '>': [complex(1, 0)],
        '<': [complex(-1, 0)],
        '^': [complex(0, -1)],
        'v': [complex(0, 1)],
        '.': [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]
    }
    for d in D[ch]:
        if state.d + d == 0:
            # can't move backwards
            continue
        pp = state.p + d
        if pp in state.previous:
            # can't move to a point already visited on this path.
            continue
        ch = map_.get(pp, None)
        if ch is not None:
            previous = copy(state.previous)
            if pp in slides:
                previous.add(pp)
            yield State(state.n + 1, pp, d, previous)


def part1(d):
    map_, start, end, slides = make_map(d)

    seen = set()
    q = deque([State(0, start, complex(0, 1), set())])
    n_max = 0
    while q:
        state = q.pop()

        if state.p == end:
            n_max = max(n_max, state.n)

        k = state.seen_key()
        if k in seen:
            continue
        seen.add(k)

        for new_state in get_next(state, map_, slides):
            q.append(new_state)

    return n_max


def re_map(d):
    class S:
        def __init__(self, n, p):
            self.n = n
            self.p = p
        def __lt__(self, other):
            return (self.n, self.p.real, self.p.imag) < (other.n, other.p.real, other.p.imag)
        def __repr__(self) -> str:
            return f'S({self.n}, {self.p})'
    map_, start, end, _ = make_map(d, part2=True)

    neighbour_count = {}
    for p in map_.keys():
        n = 0
        for d in DD:
            pp = p + d
            if pp in map_:
                n += 1
        neighbour_count[p] = n

    junctions = [k for k, v in neighbour_count.items() if v > 2]

    def bfs(map_, start, end, junctions):
        def next_p(state, map_):
            for d in DD:
                pp = state.p + d
                if pp in map_:
                    yield S(state.n + 1, pp)

        h = [S(0, start)]
        seen = set()
        while h:
            state = heapq.heappop(h)

            if state.p == end:
                return state.n

            if state.p in junctions:
                # don't want to pass through another junction point when searching
                # for the shortest path between two junctions
                continue

            if state.p in seen:
                continue
            seen.add(state.p)

            for new_state in next_p(state, map_):
                heapq.heappush(h, new_state)

    junctions.append(start)
    junctions.append(end)

    map_new = defaultdict(list)
    for p1, p2 in combinations(junctions, 2):
        j = set(junctions)
        j.remove(p1)
        j.remove(p2)
        n = bfs(map_, p1, p2, j)
        if n is not None:
            map_new[p1].append((p2, n))
            map_new[p2].append((p1, n))
    seen = set()
    for k, v in map_new.items():
        for vv in v:
            x = f'"{int(k.imag)}, {int(k.real)}"'
            vvy =vv[0]
            si = frozenset([k, vvy])
            if si in seen:
                continue
            seen.add(si)
            y = f'"{int(vvy.imag)}, {int(vvy.real)}" [label={vv[1]}]'
            # print(x, '--', y)

    x = sorted(map_new.keys(), key=lambda z: z.imag)
    start = x[0]
    end = x[-1]
    return map_new, start, end


def part2(d):
    class S:
        def __init__(self, p, n, previous):
            self.p = p
            self.n = n
            self.previous = previous
        def key(self):
            return (self.p, frozenset(self.previous))
        def __lt__(self, other):
            return (self.n, self.p.real, self.p.imag) < (other.n, other.p.real, other.p.imag)
        def __repr__(self) -> str:
            return f'S({self.p}, {self.n}, {self.previous})'

    map_, start, end = re_map(d)

    q = [S(start, 0, set())]
    n_max = 0
    while q:
        s = q.pop()

        if s.p == end:
            n_max = max(n_max, s.n)

        for pp, n in map_[s.p]:
            previous = set(s.previous)
            if pp in previous:
                continue
            previous.add(s.p)
            new_s = S(pp, s.n + n, previous)
            q.append(new_s)

    return n_max

def main():
    d = get_input('23')
    # d = TEST.strip()

    p1 = part1(d)
    print(p1)

    p2 = part2(d)
    print(p2)


if __name__ == '__main__':
    main()
