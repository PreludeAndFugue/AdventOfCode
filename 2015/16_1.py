#!python3

'''Day 16, part 1.'''

import re

from data_16 import data

BASE = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''

regex = '(\w+): (\d)'


def parse_base(base):
    data = {}
    for row in base.strip().split('\n'):
        name, n = re.match(regex, row).groups()
        data[name] = int(n)
    return data


def match(items, base):
    results = []
    for k, v in items.items():
        if k in ('cats', 'trees'):
            results.append(v > base[k])
        if k in ('pomeranians', 'goldfish'):
            results.append(v < base[k])
        else:
            results.append(v == base[k])
    return all(results)


def main1(base):
    results = []
    for i, items in data:
        if all(base[k] == v for k, v in items.items()):
            results.append((i, items))
    print(results)


def main2(base):
    results = []
    for i, items in data:
        if match(items, base):
            results.append((i, items))
    print(results)


if __name__ == '__main__':
    base = parse_base(BASE)
    # print(base)

    main1(base)

    main2(base)
