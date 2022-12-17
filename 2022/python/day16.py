
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


def neighbour_state(state, M, P):
    pressure, valve, minute, opened = state
    if P[valve] > 0 and valve not in opened:
        new_openened = opened.copy()
        new_openened = new_openened | frozenset([valve])
        extra_pressure = (TOTAL_TIME_PART_1 - minute - 1) * P[valve]
        yield pressure + extra_pressure, valve, minute + 1, new_openened
    for neighbour in M[valve]:
        yield pressure, neighbour, minute + 1, opened


def neighbour_state_2(state, M, P):
    pressure, v1, v2, minute, opened = state
    extra_pressure = sum(P[v] for v in opened)
    can_open_v1 = P[v1] > 0 and v1 not in opened
    can_open_v2 = P[v2] > 0 and v2 not in opened
    if can_open_v1:
        if can_open_v2:
            pass
        else:
            pass
    else:
        if can_open_v2:
            pass
        else:
            pass


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

        test = state[0], state[1], state[2]
        if test in seen:
            continue
        seen.add(test)

        for n_state in neighbour_state(state, M, P):
            if n_state[2] <= TOTAL_TIME_PART_1:
                heapq.heappush(q, n_state)

    return pressure


def part2(M, P):
    '''
    State: total_pressure, my value, elephant valve, minute, opened valves
    '''
    start_state = 0, START, START, 0, frozenset()
    q = [start_state]
    seen = set()

    best_state = start_state

    while q:
        state = heapq.heappop(q)
        if state[0] > best_state[0]:
            best_state = state

        test = state[0], state[1], state[2]
        if test in seen:
            continue
        seen.add(test)

        for n_state in neighbour_state_2(state, M, P):
            if n_state[3] <= TOTAL_TIME_PART_2:
                heapq.heappush(q, n_state)


def main():
    s = get_input('16')
    # s = TEST1.strip()
    M, P = parse(s)

    p1 = part1(M, P)

    print('Part 1:', p1)


if __name__ == '__main__':
    main()
