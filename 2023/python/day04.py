
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
        winning_numbers = set(int(x) for x in a2.strip().split())
        numbers = set(int(x) for x in b.strip().split())
        yield card_no, winning_numbers, numbers


def part1(cards):
    t = 0
    for _, winning_numbers, numbers in cards:
        n = len(numbers.intersection(winning_numbers))
        p = 0 if n == 0 else 2**(n - 1)
        t += p
    return t


def part2(cards):
    counter = Counter()
    for card_no, winning_numbers, numbers in cards:
        counter[card_no] += 1
        card_no_count = counter[card_no]
        n = len(numbers.intersection(winning_numbers))
        if n > 0:
            for i in range(card_no + 1, card_no + n + 1):
                counter[i] += card_no_count
    return sum(counter.values())


def main():
    d = get_input('04').strip().split('\n')
    # d = TEST.strip().split('\n')
    cards = list(parse(d))

    p1 = part1(cards)
    print(p1)

    p2 = part2(cards)
    print(p2)




if __name__ == '__main__':
    main()
