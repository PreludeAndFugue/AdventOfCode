
from help import get_input

from collections import defaultdict
from functools import cmp_to_key

test1 = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''


def parse(source):
    map_ = defaultdict(set)
    a, b = source.split('\n\n')
    for line in a.split('\n'):
        x, y = line.split('|')
        x = int(x)
        y = int(y)
        map_[x].add(y)

    ns = []
    for line in b.split('\n'):
        n = list(map(int, line.split(',')))
        ns.append(n)

    return map_, ns


def check(map_, ns):
    for n1, n2 in zip(ns, ns[1:]):
        m = map_.get(n1, [])
        if n2 not in m:
            return False
    return True


def part1():
    source = get_input(5)
    # source = test1.strip()

    map_, ns = parse(source)

    count = 0
    for n in ns:
        if check(map_, n):
            i = len(n) // 2
            count += n[i]

    print(count)


def part2():
    # source = test1.strip()
    source = get_input(5)
    map_, ns = parse(source)

    incorrect = []
    for n in ns:
        if not check(map_, n):
            incorrect.append(n)

    result = 0
    for n in incorrect:
        len_n = len(n)
        change = True
        while change:
            j = 1
            change = False
            while j < len_n:
                n1 = n[j - 1]
                n2 = n[j]
                m = map_.get(n1, [])
                if n2 not in m:
                    change = True
                    n[j - 1] = n2
                    n[j] = n1
                j += 1
        k = len_n // 2

        result += n[k]
    print(result)


def part1a():
    '''
    Use built-in sort to solve problems.
    '''
    source = test1.strip()
    map_, ns = parse(source)

    def sorter(n1, n2):
        m = map_.get(n1, [])
        if n2 in m:
            return -1
        else:
            return 1

    sort_key = cmp_to_key(sorter)

    a1 = 0
    a2 = 0
    for n in ns:
        m = sorted(n, key=sort_key)
        mid = m[len(n) // 2]
        if m == n:
            a1 += mid
        else:
            a2 += mid

    print(a1)
    print(a2)


# part1()
# part2()
part1a()
