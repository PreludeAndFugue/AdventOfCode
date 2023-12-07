from collections import Counter
from functools import cmp_to_key

from help import get_input

TEST = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

CARD_STRENGTHS_1 = {c: n for n, c in enumerate('AKQJT98765432')}
CARD_STRENGTHS_2 = {c: n for n, c in enumerate('AKQT98765432J')}


def type_of(hand):
    '''
    0: five of a kind AAAAA
    1: four of a kind AA8AA
    2: full house 23332
    3: three of a kind TTT98
    4: two pair 23432
    5: one pair A23A4
    6: high card 23456
    '''
    counter = Counter(hand)
    l = len(counter)
    if l == 1:
        return 0
    n = counter.most_common(1)[0][1]
    if l == 2:
        if n == 4:
            return 1
        else:
            return 2
    if l == 3:
        if n == 3:
            return 3
        else:
            return 4
    if l == 4:
        return 5
    return 6


def type_of_2(hand):
    counter = Counter(hand)
    j = counter['J']
    if j == 0:
        return type_of(hand)
    l = len(counter)
    if l == 1:
        return 0
    n = counter.most_common(1)[0][1]
    if l == 2:
        if n == 4:
            # 4 of a kind -> 5 of a kind
            return 0
        else:
            # full house -> 5 of a kind
            return 0
    if l == 3:
        if n == 3:
            # 3 of a kind -> 4 of a kind
            return 1
        else:
            if j == 2:
                # two pair (jack pair) -> 4 of a kind
                return 1
            elif j == 1:
                # two pair (single jack) -> full house
                return 2
            else:
                raise ValueError
    if l == 4:
        # one pair -> three of a kind
        return 3
    # high card -> one pair
    return 5


def make_compare(type_of_fn, strengths):
    def compare(item1, item2):
        h1 = item1[0]
        h2 = item2[0]
        t1 = type_of_fn(h1)
        t2 = type_of_fn(h2)
        dt = t1 - t2
        if dt:
            return dt
        for c1, c2 in zip(h1, h2):
            n1 = strengths[c1]
            n2 = strengths[c2]
            dn = n1 - n2
            if dn:
                return dn
        raise ValueError
    return compare


def winnings(items, type_of_fn, strengths):
    compare = make_compare(type_of_fn, strengths)
    items.sort(key=cmp_to_key(compare), reverse=True)
    return sum(i * item[1] for i, item in enumerate(items, start=1))


d = get_input('07').strip()
# d = TEST.strip()

items = []
for l in d.split('\n'):
    h, b = l.split(' ')
    b = int(b)
    items.append((h, b))

p1 = winnings(items, type_of, CARD_STRENGTHS_1)
print(p1)

p2 = winnings(items, type_of_2, CARD_STRENGTHS_2)
print(p2)
