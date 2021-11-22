#!python3

'''
Part2
-----
8: (42 | 42 8)
    -> 42?

11: (42 31 | 42 11 31)
    -> 42 ? 31 ?

0: 8 11
    -> 42? 42? 31?


Answer too high: 374
Answer too low: 358

'''

import re
from day19helper import make_re, make_partial_re

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

TEST_INPUT_3 = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
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


def test2():
    rules, tests = TEST_INPUT_3.strip().split('\n\n')
    regex = make_re(rules, 0, part2=True)
    count = 0
    for test in tests.strip().split('\n'):
        if regex.match(test):
            count += 1
    assert count == 12


def part2():
    rules, tests = open(INPUT, 'r').read().strip().split('\n\n')
    regex = make_re(rules, 0, part2=True)
    count = 0
    for test in tests.strip().split('\n'):
        if regex.match(test):
            count += 1
    return count


def main():
    # test1()

    # p = part1()
    # print(p)

    test2()

    p = part2()
    print(p)


if __name__ == "__main__":
    main()
