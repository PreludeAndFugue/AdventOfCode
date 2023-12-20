
from collections import Counter
import heapq

from help import get_input

from day17 import TEST, TEST_2, LEFT, RIGHT, make_map

'''
Part 2
1256: too high
1216: too low
'''

TEST_3 = '''112999
911111'''

# part 1 -> 16
TEST_4 = '''11599
99199
99199
99199
99111'''

# part 1 -> 9
TEST_5 = '''11199
12199
99199
99131
99111'''

# part 2 -> 41
TEST_6 = '''111119
999919
999919
999919
999911'''

# part 2 -> 18
TEST_7 = '''111111111119999
999999999919999
999999999919999
999999999919999
999999999911111'''

# part 1 -> 68
TEST_8 = '''
11111111111111
11111111111111
11111111111111
66999999999999
66999999999999
66999999999999
66999999999999
66999999999999
11999999999999
91999999999999
11999999999999
59999999999999
11111111111111
11111111111111'''


def make_map_1(d):
    map_ = {}
    r_max = 0
    c_max = 0
    for r, line in enumerate(d.split('\n')):
        for c, n in enumerate(line):
            # print(r, c, n)
            map_[complex(r, c)] = int(n)
            r_max = max(r_max, r)
            c_max = max(c_max, c)
    return map_, complex(r_max, c_max)


class State:
    def __init__(self, h, p, d, l):
        self.h = h
        self.p = p
        self.d = d
        self.l = l

    @property
    def key(self):
        '''
        For set
        '''
        return self.p, self.d, self.l

    def __lt__(self, other):
        '''
        For heapq
        '''
        # return (self.h, -self.p.real, -self.p.imag) < (other.h, -other.p.real, -other.p.imag)
        return (self.h, self.p.real, self.p.imag) < (other.h, other.p.real, other.p.imag)

    def __repr__(self):
        return f'S({self.h}, {self.p}, {self.d}, {self.l})'


def get_next(state, map_):
    d = state.d
    p = state.p
    if state.l < 3:
        # continue straight on
        pp = p + d
        hh = map_.get(pp, None)
        if hh is not None:
            yield State(state.h + hh, pp, d, state.l + 1)

    # left and right
    for turn in (1j, -1j):
        dd = d*turn
        pp = p + dd
        hh = map_.get(pp, None)
        if hh is not None:
            yield State(state.h + hh, pp, dd, 1)


straight = set()
turning = set()

def get_next_2(state, map_):
    d = state.d
    p = state.p
    if state.l < 4:
        # can only continue straight
        pp = p + d
        hh = map_.get(pp, None)
        if hh is not None:
            straight.add(state.l)
            yield State(state.h + hh, pp, d, state.l + 1)
    else:
        # can still go straight
        if state.l < 10:
            pp = p + d
            hh = map_.get(pp, None)
            if hh is not None:
                straight.add(state.l)
                yield State(state.h + hh, pp, d, state.l + 1)

        # left and right
        for turn in (1j, -1j):
            dd = d*turn
            pp = p + dd
            hh = map_.get(pp, None)
            if hh is not None:
                turning.add(state.l)
                yield State(state.h + hh, pp, dd, 1)


def path(prev, p_end):
    current_p = p_end
    p = [p_end]
    while True:
        if current_p in prev:
            p.append(prev[current_p])
            current_p = prev[current_p]
        else:
            break
    return list(reversed(p))


d = get_input('17').strip()
# d = TEST.strip()
# d = TEST_2.strip()
# d = TEST_3.strip()
# d = TEST_4.strip()
# d = TEST_5.strip()
# d = TEST_6.strip()
# d = TEST_7.strip()
# d = TEST_8.strip()
# print(d)

map_, p_end = make_map_1(d)

p_start = complex(0, 0)
check = [State(0, p_start, complex(0, 1), 0)]
seen = set()

# dist = {}
# prev = {}
# for k in map_.keys():
#     dist[k] = 1_000_000_000_000
#     prev[k] = None
# dist[p_start] = 0

l_counter = Counter()

i = 0
while check:
    # print(check)
    state = heapq.heappop(check)

    # l_counter[state.l] += 1

    i += 1
    # print(i)
    if i % 100_000 == 0:
        print(state)
        print(len(check))

    # print(state)

    if state.p == p_end and state.l >= 4:
    # if state.p == p_end:
        print('done', state.h, state)
        break

    if state.key in seen:
        continue
    seen.add(state.key)

    # for new_state in get_next(state, map_):
    for new_state in get_next_2(state, map_):
        # print('\t', 'new state', new_state)
        # input()
        heapq.heappush(check, new_state)
        # seen.add(new_state)

        # print(new_state, new_state.h, dist[new_state.p])
        # if new_state.h < dist[new_state.p]:
        #     # print('\tless than', new_state.h, dist[new_state.p])
        #     # input()
        #     dist[new_state.p] = new_state.h
        #     prev[new_state.p] = state.p


# print(prev)
# print(path(prev, p_end))
# print(straight)
# print(turning)
# print(l_counter)