#!python3

from collections import Counter

from helpers import BASE

TEST01 = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''


def parse(string):
    template, pairs = string.strip().split('\n\n')
    pairs = [p.split(' -> ') for p in pairs.split('\n')]
    pairs = {p[0]: p[1] for p in pairs}
    return template, pairs


def step(template, pairs):
    insertions = []
    for t1, t2 in zip(template, template[1:]):
        pair_insertion = pairs[t1 + t2]
        insertions.append(pair_insertion)
    new_template = []
    for t, i, in zip(template, insertions):
        new_template.append(t)
        new_template.append(i)
    new_template.append(template[-1])
    return ''.join(new_template)


def part1(template, pairs):
    for _ in range(10):
        template = step(template, pairs)
    count = Counter(template)
    values = count.values()
    min_count = min(values)
    max_count = max(values)
    return max_count - min_count


def main():
    test_input = parse(TEST01)
    template, pairs = parse(open(BASE + 'day14.txt', 'r').read())

    t1 = part1(*test_input)
    assert t1 == 1588

    p1 = part1(template, pairs)
    print(f'Part 1 {p1}')


if __name__ == '__main__':
    main()
