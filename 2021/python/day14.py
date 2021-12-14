#!python3

from collections import Counter, defaultdict

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
    new_template = defaultdict(int)
    for t, count in template.items():
        t_new = pairs[t]
        t1 = t[0]
        t2 = t[1]
        new_template[t1 + t_new] += count
        new_template[t_new + t2] += count
    return new_template


def part(template, pairs, n):
    test = Counter(t1 + t2 for t1, t2 in zip(template, template[1:]))
    for _ in range(n):
        test = step(test, pairs)
    count = defaultdict(int)
    for t, c in test.items():
        for t_i in t:
            count[t_i] += c
    count[template[0]] += 1
    count[template[-1]] += 1
    values = count.values()
    min_count = min(values) // 2
    max_count = max(values) // 2
    return max_count - min_count


def main():
    test_input = parse(TEST01)
    template, pairs = parse(open(BASE + 'day14.txt', 'r').read())

    t1 = part(*test_input, 10)
    assert t1 == 1588

    p1 = part(template, pairs, 10)
    print(f'Part 1 {p1}')

    t2 = part(*test_input, 40)
    assert t2 == 2188189693529

    p2 = part(template, pairs, 40)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
