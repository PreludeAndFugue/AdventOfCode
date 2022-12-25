
from collections import deque

from help import get_input
from day16 import TEST1, START, TOTAL_TIME_PART_1, TOTAL_TIME_PART_2, parse


def get_neighbour(p, v, t, opened, M, P):
    for o in opened:
        p += P[o]
    if P[v] > 0 and v not in opened:
        new_opened = opened.copy()
        new_opened |= frozenset([v])
        yield p, v, t + 1, new_opened
    for neighbour in M[v]:
        yield p, neighbour, t + 1, opened


def get_neighbour_2(p, v1, v2, t, opened, M, P):
    for o in opened:
        p += P[o]
    can_open_v1 = P[v1] > 0 and v1 not in opened
    can_open_v2 = P[v2] > 0 and v2 not in opened

    if can_open_v1:
        if v2 != v1 and can_open_v2:
            new_opened = opened.copy()
            new_opened |= frozenset([v1, v2])
            yield p, v1, v2, t + 1, new_opened
        else:
            new_opened = opened.copy()
            new_opened |= frozenset([v1])
            for neighbour2 in M[v2]:
                yield p, v1, neighbour2, t + 1, new_opened
    else:
        if can_open_v2:
            new_opened = opened.copy()
            new_opened |= frozenset([v2])
            for neighbour1 in M[v1]:
                yield p, neighbour1, v2, t + 1, new_opened
        else:
            for neighbour1 in M[v1]:
                for neighbour2 in M[v2]:
                    yield p, neighbour1, neighbour2, t + 1, opened


def part1(M, P):
    # pressure, valve, time, opened
    # p, v, t, opened
    q = deque([(0, START, 0, frozenset())])
    seen = set()
    p_best = 0
    while q:
        p, v, t, opened = q.pop()

        # print(p, v, t, opened)
        # input()

        if p > p_best:
            p_best = p

        test = p, v, t, opened
        if test in seen:
            continue
        seen.add(test)

        for pn, vn, tn, on in get_neighbour(p, v, t, opened, M, P):
            if tn <= TOTAL_TIME_PART_1:
                q.append((pn, vn, tn, on))

    return p_best


def part2(M, P):
    max_step_p = sum(P.values())

    start = 0, START, START, 0, frozenset()
    q = deque([start])
    seen = set()
    p_best = 0
    # i = 0
    while q:
        p, v1, v2, t, opened = q.pop()

        max_gain = max_step_p * (TOTAL_TIME_PART_2 - t)
        if p + max_gain < p_best:
            continue

        # i += 1
        # if i % 500_000 == 0:
        #     print(p, v1, v2, t, opened)
        #     print(p_best)

        p_best = max(p, p_best)

        test = frozenset([v1, v2]), t, opened
        if test in seen:
            continue
        seen.add(test)

        for new_state in get_neighbour_2(p, v1, v2, t, opened, M, P):
            tn = new_state[3]
            if tn <= TOTAL_TIME_PART_2:
                q.append(new_state)

    return p_best


def main():
    s = get_input('16')
    # s = TEST1.strip()
    M, P = parse(s)

    # print(M)
    # print(P)

    # p1 = part1(M, P)
    p2 = part2(M, P)

    # print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()