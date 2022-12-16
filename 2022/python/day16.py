
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
    total_pressure, valve, minute, opened_valves = state
    new_pressure = sum(P[v] for v in opened_valves)
    if P[valve] > 0 and valve not in opened_valves:
        new_open = opened_valves.copy()
        new_open = new_open | frozenset([valve])
        yield total_pressure + new_pressure, valve, minute + 1, new_open
    for neighbour in M[valve]:
        yield total_pressure + new_pressure, neighbour, minute + 1, opened_valves


def neighbour_state_2(state, M, P):
    pressure, v1, v2, minute, opened = state
    extra_pressure = sum(P[v] for v in opened)
    can_open_v1 = P[v1] > 0 and v1 not in opened
    can_open_v2 = P[v2] > 0 and v2 not in opened
    if can_open_v1:
        if can_open_v2:

        else:

    else:
        if can_open_v2:

        else:
            


def part1(M, P):
    '''
    State: total_pressure, current valve, minute, opened valves
    '''
    start_state = 0, START, 0, frozenset()
    q = [start_state]
    seen = set()

    best_state = start_state

    i = 0

    while q:
        state = heapq.heappop(q)
        if state[0] > best_state[0]:
            best_state = state

        i += 1
        if i % 1_000_000 == 0:
            print(len(q))
            print(best_state)

        test = state[0], state[1], state[3]
        if test in seen:
            continue
        seen.add(test)

        for n_state in neighbour_state(state, M, P):
            if n_state[2] <= TOTAL_TIME_PART_1:
                heapq.heappush(q, n_state)

    print('best state', best_state)
    return best_state[0]


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
