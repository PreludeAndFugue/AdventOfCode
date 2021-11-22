#!python3

from collections import defaultdict
from functools import reduce
from operator import mul

ITEMS = [
    1,
    2,
    3,
    5,
    7,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
]

THIRD = 512
QUARTER = 384

TEST_ITEMS = [
    1, 2, 3, 4, 5, 7, 8, 9, 10, 11
]
TEST_THIRD = 20
TEST_QUARTER = 15


def get_third(selection, other_items, total):
    for i, n in enumerate(other_items):
        new_selection = selection + [n]
        if sum(new_selection) < total:
            new_other_items = other_items[i + 1:]
            yield from get_third(new_selection, new_other_items, total)
        elif sum(new_selection) == total:
            yield new_selection


def remove_third(items, third):
    third = set(third)
    return [n for n in items if n not in third]


def is_three_thirds(items, total):
    test = get_third([], items, total)
    try:
        next(test)
        return True
    except:
        return False


def is_four_quarters(items, total):
    second_quarter = get_third([], items, total)
    for s in second_quarter:
        others = remove_third(items, s)
        third_quarter = get_third([], others, total)
        try:
            next(third_quarter)
            return True
        except:
            continue
    return False


def part1():
    items = list(reversed(ITEMS))
    total = THIRD
    results = defaultdict(list)
    min_length = 1_000_000
    for third in get_third([], items, total):
        length = len(third)
        if length > min_length:
            continue

        min_length = length
        others = remove_third(items, third)
        # print(third, others)

        if is_three_thirds(others, total):
            # print('yes')
            results[length].append(third)

    m = min(results.keys())
    n = results[m]
    n = [reduce(mul, x, 1) for x in n]
    print(min(n))


def part2():
    items = list(reversed(ITEMS))
    total = QUARTER
    results = defaultdict(list)
    min_length = 1_000_000
    for quarter in get_third([], items, total):
        length = len(quarter)
        if length > min_length:
            continue

        min_length = length
        others = remove_third(items, quarter)

        if is_four_quarters(others, total):
            results[length].append(quarter)

    m = min(results.keys())
    n = results[m]
    n = [reduce(mul, x, 1) for x in n]
    print(min(n))



def main():
    # part1()
    part2()


if __name__ == '__main__':
    main()
