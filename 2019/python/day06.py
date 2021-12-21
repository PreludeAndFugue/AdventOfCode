#!python3

from collections import defaultdict

from helpers import BASE

TEST01 = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L'''


def parse(string):
    orbits = defaultdict(list)
    for line in string.strip().split('\n'):
        a, b = line.split(')')
        orbits[a].append(b)
    return orbits


def part1(orbits):
    count = 0
    seen = set()
    to_search = [('COM', 0)]
    while to_search:
        p, depth = to_search.pop(0)
        if p not in seen:
            count += depth
            for child in orbits[p]:
                to_search.append((child, depth + 1))
    return count


def main():
    test_orbits = parse(TEST01)
    t1 = part1(test_orbits)
    assert t1 == 42

    orbits = parse(open(BASE + 'day06.txt', 'r').read())

    p1 = part1(orbits)
    print(f'Part 1: {p1}')


if __name__ == '__main__':
    main()
