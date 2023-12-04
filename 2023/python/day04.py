
from collections import Counter
from help import get_input

TEST = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''


def parse(d):
    for l in d:
        a, b = l.split(' | ')
        a1, a2 = a.split(':')
        card_no = int(a1.strip().split()[1])
        winning_numbers = set(x for x in a2.strip().split())
        numbers = set(x for x in b.strip().split())
        yield card_no, winning_numbers, numbers


def part1(cards):
    t = 0
    for _, winning_numbers, numbers in cards:
        n = len(numbers & winning_numbers)
        p = 0 if n == 0 else 2**(n - 1)
        t += p
    return t


def part2(cards):
    counter = Counter()
    for card_no, winning_numbers, numbers in cards:
        counter[card_no] += 1
        card_no_count = counter[card_no]
        n = len(numbers & winning_numbers)
        if n > 0:
            for i in range(card_no + 1, card_no + n + 1):
                counter[i] += card_no_count
    return sum(counter.values())


def part2_recursive(card_no, cards):
    '''Recursion with generators'''
    _, winning_numbers, numbers = cards[card_no - 1]
    yield 1
    n = len(numbers & winning_numbers)
    if n > 0:
        for i in range(card_no + 1, card_no + n + 1):
            yield from part2_recursive(i, cards)


def part2_recursive_1(card_no, cards):
    '''Recursion without generators'''
    _, winning_numbers, numbers = cards[card_no - 1]
    n = len(numbers & winning_numbers)
    if n == 0:
        return 1
    t = 1
    for i in range(card_no + 1, card_no + n + 1):
        t += part2_recursive_1(i, cards)
    return t


def main():
    d = get_input('04').strip().split('\n')
    # d = TEST.strip().split('\n')
    cards = list(parse(d))

    p1 = part1(cards)
    print(p1)

    p2 = part2(cards)
    print(p2)

    r = sum(sum(part2_recursive(card_no, cards)) for card_no, _, _ in cards)
    print('p2:', r)

    r1 = sum(part2_recursive_1(card_no, cards) for card_no, _, _ in cards)
    print('p2:', r1)


if __name__ == '__main__':
    main()
