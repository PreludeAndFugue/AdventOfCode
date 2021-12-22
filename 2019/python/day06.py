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

TEST02 = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''


def parse(string):
    orbits = defaultdict(list)
    for line in string.strip().split('\n'):
        a, b = line.split(')')
        orbits[a].append(b)
    return orbits


def reverse_orbits(orbits):
    r = {}
    for k, v in orbits.items():
        for m in v:
            r[m] = k
    return r


def path(p, orbits):
    result = []
    while p:
        p = orbits.get(p, None)
        result.append(p)
    return result


def part1(orbits):
    count = 0
    to_search = [('COM', 0)]
    while to_search:
        p, depth = to_search.pop(0)
        count += depth
        for child in orbits[p]:
            to_search.append((child, depth + 1))
    return count


def part2(orbits):
    r = reverse_orbits(orbits)
    s_path = path('SAN', r)
    y_path = path('YOU', r)
    for i, m in enumerate(y_path):
        if m in s_path:
            return i + s_path.index(m)


def main():
    test_orbits_1 = parse(TEST01)
    t1 = part1(test_orbits_1)
    assert t1 == 42

    orbits = parse(open(BASE + 'day06.txt', 'r').read())

    p1 = part1(orbits)
    print(f'Part 1: {p1}')

    test_orbits_2 = parse(TEST02)
    t2 = part2(test_orbits_2)
    assert t2 == 4

    p2 = part2(orbits)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
