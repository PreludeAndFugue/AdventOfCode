
from collections import defaultdict, deque
import heapq
import re

from help import get_input

'''
Part1
-----
1762: too low
1857: too low, same as other answer
1915: tool low, same as other answer
'''

TEST1 = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''

regex = re.compile('Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)')

START = 'AA'
TOTAL_TIME_PART_1 = 30
TOTAL_TIME_PART_2 = 26

def parse(s):
    M = {}
    P = {}
    for line in s.split('\n'):
        m = regex.match(line)
        assert m is not None
        valve = m[1]
        rate = int(m[2])
        other_valves = m[3].split(', ')
        M[valve] = other_valves
        P[valve] = rate
    return M, P


def new_map(M, P):
    M1 = defaultdict(list)
    V = [v for v, p in P.items() if p > 0]
    V = [START] + V
    for vstart in V:
        q = [(0, vstart)]
        seen = set()

        # print(vstart, q, seen)

        while q:
            t, v = heapq.heappop(q)

            if v in seen:
                continue
            seen.add(v)


            if P[v] > 0 and v != vstart:
                M1[vstart].append((v, t))

            for nv in M[v]:
                q.append((t + 1, nv))

    return M1


def neighbour_state(state, M1, P):
    '''
    Excluded is a previous valve that we don't want to consider again as a neighbour.
    '''
    pressure, valve, minute, opened = state
    if P[valve] > 0 and valve not in opened:
        new_openened = opened.copy()
        new_openened = new_openened | frozenset([valve])
        extra_pressure = (TOTAL_TIME_PART_1 - minute - 1) * P[valve]
        yield pressure + extra_pressure, valve, minute + 1, new_openened
    for neighbour, dt in M1[valve]:
        yield pressure, neighbour, minute + dt, opened


def neighbour_state_2(state, M1, P):
    p, v1, v2, t, o = state

    s1 = p, v1, t, o
    for n1 in neighbour_state(s1, M1, P):
        p1a, n1a, t1a, o1a = n1

        o2 = o | o1a
        s2 = p1a, v2, t, o2
        for n2 in neighbour_state(s2, M1, P):
            p2a, n2a, t2a, o2a = n2

            t_new = max(t1a, t2a)
            new_state = p2a, n1a, n2a, t_new, o2a

            yield new_state


def part1(M, P):
    '''
    State: total_pressure, current valve, minute, opened valves
    '''
    start_state = 0, START, 0, frozenset()
    q = [start_state]
    seen = set()
    pressure = 0

    while q:
        state = heapq.heappop(q)
        if state[0] > pressure:
            pressure = state[0]
            # print('New max', pressure)

        test = state[1], state[2], state[3]
        if test in seen:
            continue
        seen.add(test)

        for n_state in neighbour_state(state, M, P):
            if n_state[2] <= TOTAL_TIME_PART_1:
                heapq.heappush(q, n_state)

    return pressure


def part2(M, P):
    '''
    State: total_pressure, my valve, elephant valve, minute, opened valves
    '''
    start_state = 0, START, START, 0, frozenset()
    q = [start_state]
    seen = set()
    pressure = 0

    i = 0

    while q:
        state = heapq.heappop(q)

        i += 1
        if i % 100_000 == 0:
            print(state, len(q))

        if state[0] > pressure:
            pressure = state[0]

        test = state[1], state[2], state[3], state[4]
        if test in seen:
            continue
        seen.add(test)

        for n_state in neighbour_state_2(state, M, P):
            if n_state[3] <= TOTAL_TIME_PART_2:
                heapq.heappush(q, n_state)

    return pressure


def main():
    # s = get_input('16')
    s = TEST1.strip()
    M, P = parse(s)
    M1 = new_map(M, P)

    p1 = part1(M1, P)
    # p2 = part2(M1, P)

    print('Part 1:', p1)
    # print('Part 2:', p2)


if __name__ == '__main__':
    main()
