#!python3

from collections import defaultdict
import re

INPUT = 'day07.txt'

TEST_INPUT = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''

TEST_INPUT2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
'''

PATTERN = r'(\d+)\s(\w+\s\w+)'
BAG = re.compile(PATTERN)


def parse_contents(contents):
    '''
    Parse string of form
        1 bright white bag, 2 muted yellow bags
    to a dict
        {'bright white': 1, 'muted yellow': 2}
    '''
    bags = {}
    for m in re.finditer(PATTERN, contents):
        n = int(m.group(1))
        bags[m.group(2)] = n
    return bags


def get_input(input):
    contains = {}
    for line in input.strip().split('\n'):
        bag, contents = line.split(' contain ')
        bag = bag.rsplit(' ', 1)[0]
        c = parse_contents(contents)
        contains[bag] = c
    return contains


def get_reverse(bags):
    '''Reverses the relationship in `get_input`.'''
    result = defaultdict(list)
    for bag, contents in bags.items():
        for b in contents.keys():
            result[b].append(bag)
    return result


def is_contained_in_count(bag, reverse_bags):
    '''Part 1 counter.

    Just a simple search algorithm.
    '''
    to_check = reverse_bags[bag]
    seen = set()
    while to_check:
        item = to_check.pop()
        if item in seen:
            continue
        seen.add(item)
        for b in reverse_bags[item]:
            to_check.append(b)
    return len(seen)


def contains_count_helper(bag, count, bags):
    others = bags[bag]
    if not others:
        yield 0
    for b, c in others.items():
        yield count * c
        yield from contains_count_helper(b, count * c, bags)


def contains_count(bag, bags):
    '''Part 2 counter.'''
    return sum(contains_count_helper(bag, 1, bags))


def test1(bags):
    reverse_bags = get_reverse(bags)
    c = is_contained_in_count('shiny gold', reverse_bags)
    assert c == 4


def part1(bags):
    reverse_bags = get_reverse(bags)
    return is_contained_in_count('shiny gold', reverse_bags)


def test2(bags1, bags2):
    n = contains_count('shiny gold', bags1)
    assert n == 32

    n = contains_count('shiny gold', bags2)
    assert n == 126


def part2(bags):
    return contains_count('shiny gold', bags)


def main():
    bags = get_input(open(INPUT, 'r').read())
    test_bags_1 = get_input(TEST_INPUT)
    test_bags_2 = get_input(TEST_INPUT2)

    test1(test_bags_1)

    p = part1(bags)
    print(p)

    test2(test_bags_1, test_bags_2)

    p = part2(bags)
    print(p)


if __name__ == "__main__":
    main()
