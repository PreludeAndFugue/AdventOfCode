#!python3


from collections import Counter, deque
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
    results = []
    for line in input.strip().split('\n'):
        results.append(int(line))
    return results


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
    numbers.append(0)
    m = max(numbers) + 3
    numbers.append(m)
    numbers.sort()
    n = diff_calculator(numbers)
    return n


def test2():
    numbers = get_numbers(TEST_INPUT_2)
    numbers.append(0)
    m = max(numbers) + 3
    numbers.append(m)
    numbers.sort()
    n = diff_calculator(numbers)
    return n


def part1():
    numbers = get_numbers(open(INPUT, 'r').read())
    numbers.append(0)
    m = max(numbers) + 3
    numbers.append(m)
    numbers.sort()
    n = diff_calculator(numbers)
    return n


def main():
    assert test1() == 35
    assert test2() == 220

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
