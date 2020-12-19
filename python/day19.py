#!python3

from day19helper import make_re

INPUT = 'day19.txt'

TEST_INPUT_1 = '''0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"
'''

TEST_INPUT_2 = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
'''
TEST_RE = '''ababbb
bababa
abbbab
aaabbb
aaaabbb
'''


def test1():
    regex = make_re(TEST_INPUT_2, 0)
    s = sum(1 if regex.match(t) else 0 for t in TEST_RE.strip().split('\n'))
    assert s == 2


def part1():
    rules, tests = open(INPUT, 'r').read().strip().split('\n\n')
    regex = make_re(rules.strip(), 0)
    count = 0
    for test in tests.strip().split('\n'):
        if regex.match(test):
            count += 1
    return count


def main():
    test1()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
