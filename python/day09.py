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


def main():
    assert test1() == 127

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
