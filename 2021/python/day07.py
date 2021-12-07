#!python3

from helpers import BASE

TEST01 = '''16,1,2,0,4,2,7,1,2,14'''


def total_cost_1(position, crabs):
    d = 0
    for c in crabs:
        d += abs(c - position)
    return d


def total_cost_2(position, crabs):
    d = 0
    for c in crabs:
        n = abs(c - position)
        d += n * (n + 1) / 2
    return int(d)


def part(crabs, cost_function):
    positions = range(min(crabs), max(crabs) + 1)
    cost_positions = [cost_function(p, crabs) for p in positions]
    return min(cost_positions)


def main():
    test_ns = list(map(int, TEST01.strip().split(',')))
    ns = list(map(int, open(BASE + 'day07.txt', 'r').read().strip().split(',')))

    t1 = part(test_ns, total_cost_1)
    assert t1 == 37

    p1 = part(ns, total_cost_1)
    print(f'Part 1: {p1}')

    t2 = part(test_ns, total_cost_2)
    assert t2 == 168

    p2 = part(ns, total_cost_2)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
