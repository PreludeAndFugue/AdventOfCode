
from collections import Counter
from itertools import product

from help import get_input


def parse(d):
    for line in d.split('\n'):
        yield line.strip()


def part1(items):
    two_count = 0
    three_count = 0
    for item in items:
        count = Counter(item)
        values = set(count.values())
        if 2 in values:
            two_count += 1
        if 3 in values:
            three_count += 1

    return two_count * three_count


def get_diff(a, b):
    '''Find indices of differing chars.'''
    indices = []
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            indices.append(i)
    return indices


def part2(items):
    for a, b in product(items, repeat=2):
        diff = get_diff(a, b)
        if len(diff) == 1:
            return a


def main():
    '''Main entry point.'''
    d = get_input('02')
    items = list(parse(d))

    p1 = part1(items)
    print(p1)

    p2 = part2(items)
    print(p2)


if __name__ == '__main__':
    main()