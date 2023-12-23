
from collections import deque
import heapq

from help import get_input

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

def make_map(d):
    map_ = {}
    for r, l in enumerate(d.split('\n')):
        for c, ch in enumerate(l):
            if ch != '#':
                map_[complex(c, r)] = ch

    x = {k: v for k, v in map_.items() if v == '.'}
    x = sorted(x.keys(), key=lambda z: z.imag)
    start = x[0]
    end = x[-1]
    return map_, start, end


class State:
    def __init__(self, n, p, d):
        '''
        n: number of steps
        p: position
        d: direction
        '''
        self.n = n
        self.p = p
        self.d = d

    def seen_key(self):
        return self.n, self.p

    def __lt__(self, other):
        return (self.n, self.p.real, self.p.imag) < (other.n, other.p.real, other.p.imag)

    def __repr__(self):
        D = {
            complex(1, 0): '>',
            complex(-1, 0): '<',
            complex(0, 1): 'v',
            complex(0, -1): '^'
        }
        d = D[self.d]
        return f'S({self.n}, {self.p}, {d})'


def get_next(state, map_):
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
            continue
        pp = state.p + d
        ch = map_.get(pp, None)
        if ch is not None:
            yield State(state.n + 1, pp, d)


def part1(d):
    map_, start, end = make_map(d)
    seen = set()
    q = deque([State(0, start, complex(0, 1))])
    # q = [State(0, start, complex(0, 1))]
    # heapq.heapify(q)

    end_n = []

    while q:
        # state = heapq.heappop(q)
        state = q.pop()

        # print(state)
        # input()

        if state.p == end:
            # print(state)
            end_n.append(state.n)

        k = state.seen_key()
        if k in seen:
            continue
        seen.add(k)

        for new_state in get_next(state, map_):
            # q.append((d + 1, pp))
            # heapq.heappush(q, new_state)
            q.append(new_state)

    return max(end_n)


def main():
    d = get_input('23')
    # d = TEST.strip()

    p1 = part1(d)
    print(p1)


if __name__ == '__main__':
    main()
