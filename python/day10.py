#!python3


from collections import Counter, deque
from math import prod
from time import perf_counter


INPUT = 'day10.txt'
TEST_INPUT_1 = '''
16
10
15
5
1
11
7
19
6
12
4
'''

TEST_INPUT_2 = '''
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
'''

def get_numbers(input):
    results = [0]
    for line in input.strip().split('\n'):
        results.append(int(line))
    m = max(results) + 3
    results.append(m)
    return sorted(results)


def get_diffs(path):
    diffs = []
    for m, n in zip(path, path[1:]):
        diffs.append(n - m)
    return diffs


def diff_calculator(path):
    diffs = get_diffs(path)
    counts = Counter(diffs)
    return counts[1] * counts[3]


def test1():
    numbers = get_numbers(TEST_INPUT_1)
    n = diff_calculator(numbers)
    assert n == 35


def test2():
    numbers = get_numbers(TEST_INPUT_2)
    n = diff_calculator(numbers)
    assert n == 220


def part1():
    numbers = get_numbers(open(INPUT, 'r').read())
    n = diff_calculator(numbers)
    return n


def test3():
    n1 = sorted(get_numbers(TEST_INPUT_1))
    connections1 = make_connections(n1)
    r1 = recursive_count(connections1, 0, {})
    assert r1 == 8

    n2 = sorted(get_numbers(TEST_INPUT_2))
    connections2 = make_connections(n2)
    r2 = recursive_count(connections2, 0, {})
    assert r2 == 19208


def make_connections(numbers):
    connections = {}
    for i, n in enumerate(numbers):
        connect = []
        for k in numbers[i + 1:]:
            if k - n <= 3:
                connect.append(k)
            else:
                break
        if not connect:
            continue
        connections[n] = connect
    return connections


def recursive_count(connections, n, cache):
    if n not in connections:
        return 1
    elif n in cache:
        return cache[n]
    else:
        values = connections[n]
        x = sum(recursive_count(connections, v, cache) for v in values)
        cache[n] = x
        return x


def part2():
    numbers = get_numbers(open(INPUT, 'r').read())
    connections = make_connections(numbers)
    r = recursive_count(connections, 0, {})
    return r


def main():
    test1()
    test2()

    p = part1()
    print(p)

    test3()

    p = part2()
    print(p)


if __name__ == "__main__":
    main()
