#!python3

from collections import Counter


LOWER = 387638
UPPER = 919123


def is_valid(n, part1=True):
    s = str(n)
    for s1, s2 in zip(s, s[1:]):
        if s1 > s2:
            return False
    c = Counter(s)
    if part1:
        return max(c.values()) > 1
    else:
        return 2 in set(c.values())


def part(part1=True):
    count = 0
    for n in range(LOWER, UPPER + 1):
        if is_valid(n, part1):
            count += 1
    return count


def main():
    assert is_valid(111111)
    assert not is_valid(223450)
    assert not is_valid(123789)

    p1 = part(True)
    print(f'Part 1: {p1}')

    assert is_valid(112233, part1=False)
    assert not is_valid(123444, part1=False)
    assert is_valid(111122, part1=False)

    p2 = part(False)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
