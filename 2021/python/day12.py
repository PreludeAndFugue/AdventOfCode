#!python3

from collections import defaultdict, Counter

from helpers import BASE

TEST01 = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

TEST02 = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''

TEST03 = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''


def parse(string):
    map_ = defaultdict(list)
    for line in string.strip().split('\n'):
        x = line.split('-')
        a, b = x
        if a == 'start':
            map_[a].append(b)
        elif a == 'end':
            map_[b].append(a)
        else:
            if b != 'start':
                map_[a].append(b)
            if b != 'end':
                map_[b].append(a)
    return map_


def extend_path_1(path, map_):
    end = path[-1]
    for n in map_[end]:
        if n == 'end' or n.isupper():
            yield path + (n,)
        elif n.islower() and n not in path:
            yield path + (n,)


def are_lower_counts_one(path):
    elements = (e for e in path if e.islower() and e != 'start' and e != 'end')
    counts = Counter(elements)
    return all(c == 1 for c in counts.values())


def extend_path_2(path, map_):
    end = path[-1]
    for n in map_[end]:
        if n == 'end' or n.isupper():
            yield path + (n,)
        else:
            if n not in path:
                yield path + (n,)
            elif are_lower_counts_one(path):
                yield path + (n,)


def find_paths(map_, extender):
    results = []
    seen = set()
    to_check = [('start',)]
    while to_check:
        path = to_check.pop()
        if path in seen:
            continue
        seen.add(path)
        if path[-1] == 'end':
            results.append(path)
        extended = list(extender(path, map_))
        to_check.extend(extended)
    return results


def part1(map_):
    return len(find_paths(map_, extend_path_1))


def part2(map_):
    return len(find_paths(map_, extend_path_2))


def main():
    test1 = parse(TEST01)
    test2 = parse(TEST02)
    test3 = parse(TEST03)

    map_ = parse(open(BASE + 'day12.txt').read())

    t1 = part1(test1)
    assert t1 == 10
    t2 = part1(test2)
    assert t2 == 19
    t3 = part1(test3)
    assert t3 == 226

    p1 = part1(map_)
    print(f'Part 1: {p1}')

    t1 = part2(test1)
    assert t1 == 36
    t2 = part2(test2)
    assert t2 == 103
    t3 = part2(test3)
    assert t3 == 3509

    p2 = part2(map_)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
