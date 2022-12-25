
from functools import cache

from help import get_input, algorithm_u
from day16 import TEST1, START, TOTAL_TIME_PART_1, TOTAL_TIME_PART_2, parse, new_map

'''
Part 2:
-------
2707: too low
2708: too low
'''

M1 = None
P = None


@cache
def part1(v, p, t, opened):
    '''Start time at max.'''
    global M1, P
    # print('checking state', v, p, t, opened)
    if t == TOTAL_TIME_PART_1:
        yield p
    if v not in opened:
        new_opened = opened.copy()
        new_opened |= frozenset([v])
        new_p = (TOTAL_TIME_PART_1 - t - 1) * P[v]
        yield from part1(v, p + new_p, t + 1, new_opened)
    for vn, d in M1[v]:
        new_t = t + d
        if new_t <= TOTAL_TIME_PART_1:
            yield from part1(vn, p, new_t, opened)


@cache
def part2(v, p, t, opened, can_open):
    global M1, P
    # yield 0
    # print('checking state', v, p, t, opened, can_open)
    # input()
    if t == TOTAL_TIME_PART_2:
        yield p

    if opened == can_open:
        yield p

    if v in can_open and v not in opened:
        new_opened = opened.copy()
        new_opened |= frozenset([v])
        new_p = (TOTAL_TIME_PART_2 - t - 1) * P[v]
        yield from part2(v, p + new_p, t + 1, new_opened, can_open)
    for vn, d in M1[v]:
        if vn in opened:
            continue
        new_t = t + d
        if new_t <= TOTAL_TIME_PART_2:
            yield from part2(vn, p, new_t, opened, can_open)


def run_part2():
    start = frozenset([START])
    valves = [k for k, v in P.items() if v > 0 and k != START]
    m_max = 0
    i = 0


    seen = set()
    for a, b in algorithm_u(valves, 2):
        i += 1
        if len(a) != 8:
            continue
        print(i, a, b)

        s = frozenset(b)
        if s in seen:
            print('seen')
            continue
        seen.add(s)

        can_open1 = frozenset(a)
        can_open2 = frozenset(b)
        x = max(part2(START, 0, 0, start, can_open1))
        y = max(part2(START, 0, 0, start, can_open2))
        m_max = max(m_max, x + y)
        print(m_max)
    print(m_max)


def main():
    global M1, P
    s = get_input('16')
    # s = TEST1.strip()
    M, P = parse(s)
    M1 = new_map(M, P)
    for k, v in M1.items():
        print(k)
        print(v)

    # p1 = max(part1(START, 0, 0, frozenset([START])))
    # print('Part 1:', p1)

    run_part2()




if __name__ == '__main__':
    main()
