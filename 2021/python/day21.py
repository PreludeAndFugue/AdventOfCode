#!python3

from collections import Counter
from functools import cache
from itertools import cycle, product


def die():
    i = cycle(range(1, 101))
    while True:
        yield next(i), next(i), next(i)


def dirac():
    return list(product((1, 2, 3), repeat=3))


DIRAC_SUM = Counter(sum(roll) for roll in dirac())


def move(p, n):
    return (p - 1 + n) % 10 + 1


def part1(p1_start, p2_start):
    d = die()
    p1 = p1_start
    p2 = p2_start
    s1 = 0
    s2 = 0
    is_p1 = True
    roll_count = 0
    while True:
        roll = sum(next(d))
        roll_count += 3
        if is_p1:
            p1 = move(p1, roll)
            s1 += p1
            if s1 >= 1000:
                break
        else:
            p2 = move(p2, roll)
            s2 += p2
            if s2 >= 1000:
                break
        is_p1 = not is_p1
    return min(s1, s2) * roll_count


@cache
def part2(p1, p2, s1, s2, is_p1):
    if s1 >= 21:
        return 1, 0
    elif s2 >= 21:
        return 0, 1
    else:
        if is_p1:
            w11 = 0
            w22 = 0
            for s, n in DIRAC_SUM.items():
                p1_1 = move(p1, s)
                s1_1 = s1 + p1_1
                w1_1, w2_1 = part2(p1_1, p2, s1_1, s2, not is_p1)
                w11 += n * w1_1
                w22 += n * w2_1
            return w11, w22
        else:
            w11 = 0
            w22 = 0
            for s, n in DIRAC_SUM.items():
                p2_1 = move(p2, s)
                s2_1 = s2 + p2_1
                w1_1, w2_1 = part2(p1, p2_1, s1, s2_1, not is_p1)
                w11 += n * w1_1
                w22 += n * w2_1
            return w11, w22


def main():
    t1 = part1(4, 8)
    assert t1 == 739785

    p1 = part1(8, 9)
    print(f'Part 1: {p1}')

    t2_1, t2_2 = part2(4, 8, 0, 0, True)
    assert t2_1 == 444356092776315
    assert t2_2 == 341960390180808

    p2 = max(part2(8, 9, 0, 0, True))
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
