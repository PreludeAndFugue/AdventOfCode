#!python3

from collections import deque
from itertools import combinations

INPUT = 'day09.txt'

TEST_INPUT = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
'''

PREAMBLE = 25
TEST_PREAMBLE = 5


def get_numbers(input):
    for n in input.strip().split('\n'):
        yield int(n)


def pair_sums(numbers):
    result = set()
    for m, n in combinations(numbers, 2):
        result.add(m + n)
    return result


def _part1(numbers, preamble):
    dq = deque()
    for _ in range(preamble):
        dq.append(next(numbers))
    ps = pair_sums(dq)
    for n in numbers:
        if n not in ps:
            return n
        dq.popleft()
        dq.append(n)
        ps = pair_sums(dq)


def test1():
    numbers = get_numbers(TEST_INPUT)
    return _part1(numbers, TEST_PREAMBLE)


def part1():
    numbers = get_numbers(open(INPUT, 'r').read())
    return _part1(numbers, PREAMBLE)


def _part2(numbers, value):
    for i, _ in enumerate(numbers):
        for j, _ in enumerate(numbers[i + 1:], start=i + 1):
            s = sum(numbers[i:j + 1])
            if s == value:
                sub = numbers[i: j + 1]
                return min(sub) + max(sub)
            if s > value:
                break


def test2():
    k = test1()
    numbers = list(get_numbers(TEST_INPUT))
    return _part2(numbers, k)


def part2():
    k = part1()
    numbers = list(get_numbers(open(INPUT, 'r').read()))
    return _part2(numbers, k)


def main():
    assert test1() == 127

    p = part1()
    print(p)

    assert test2() == 62

    p = part2()
    print(p)


if __name__ == "__main__":
    main()
