
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


d = get_input('17').strip()
# d = TEST.strip()
# d = TEST_2.strip()
# d = TEST_3.strip()
# print(d)

map_, p_end = make_map_1(d)


def done_1(state):
    return state.p == p_end


def done_2(state):
    return state.p == p_end and state.l >= 4


def run(done, next_):
    p_start = complex(0, 0)
    # Need to set up two starting states for part 2.
    check = [State(0, p_start, complex(0, 1), 0), State(0, p_start, complex(1, 0), 0)]
    seen = set()

    while check:
        state = heapq.heappop(check)

        if done(state):
            # print('done', state.h, state)
            return state.h

        if state.key in seen:
            continue
        seen.add(state.key)

        for new_state in next_(state, map_):
            heapq.heappush(check, new_state)


p1 = run(done_1, get_next)
print(p1)

p2 = run(done_2, get_next_2)
print(p2)
