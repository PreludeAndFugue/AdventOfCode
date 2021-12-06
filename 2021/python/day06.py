#!python3

'''
Lifecycle

    0 ◀─── 1 ◀─── 2 ◀─── 3 ◀─── 4 ◀─── 5 ◀─── 6 ◀─── 7 ◀─── 8
    │                                         ▲             ▲
    │                                         │             │
    └─────────────────────────────────────────┴─────────────┘
'''


from collections import Counter

from helpers import BASE

TEST01 = '''3,4,3,1,2'''


def parse(text):
    ns = map(int, text.split(','))
    fish = Counter(ns)
    return fish


def cycle(fish):
    return {
        0: fish[1],
        1: fish[2],
        2: fish[3],
        3: fish[4],
        4: fish[5],
        5: fish[6],
        6: fish[7] + fish[0],
        7: fish[8],
        8: fish[0]
    }


def cycle_n(fish, n):
    for _ in range(n):
        fish = cycle(fish)
    return fish


def part(fish, n):
    fish = cycle_n(fish, n)
    return sum(fish.values())


def main():
    test_fish = parse(TEST01)
    fish = parse(open(BASE + 'day06.txt', 'r').read())

    assert part(test_fish, 80) == 5934
    assert part(test_fish, 256) == 26984457539

    p1 = part(fish, 80)
    print(f'Part 1: {p1}')

    p2 = part(fish, 256)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
