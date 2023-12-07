from collections import Counter
from functools import cmp_to_key

from help import get_input

TEST = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

CARDS = 'AKQJT98765432'
CARD_STRENGTHS = {c: n for n, c in enumerate(CARDS)}


def type_of(hand):
    '''
    0: five of a kind AAAAA
    1: four of a kind AA8AA
    2: full house 23332
    3: three of a kind TTT98
    4: two pair 23432
    5: one pair A23A4
    6: high card
    '''
    # print('type of', hand)
    counter = Counter(hand)
    l = len(counter)
    if l == 1:
        return 0
    n = counter.most_common(1)[0][1]
    # print('n', n, 'for', hand)
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


def compare(h1, item2):
    h1 = h1[0]
    h2 = item2[0]
    t1 = type_of(h1)
    t2 = type_of(h2)
    # print('type', h1, t1)
    # print('type', h2, t2)
    dt = t1 - t2
    if dt:
        # print('dt conclusive', h1, h2)
        return dt
    for c1, c2 in zip(h1, h2):
        # print('comparing cards for', h1, h2)
        n1 = CARD_STRENGTHS[c1]
        n2 = CARD_STRENGTHS[c2]
        dn = n1 - n2
        if dn:
            return dn
    raise ValueError


d = get_input('07').strip()
# d = TEST.strip()

items = []
for l in d.split('\n'):
    h, b = l.split(' ')
    b = int(b)
    items.append((h, b))


# print(items)
items.sort(key=cmp_to_key(compare), reverse=True)
# print(items)

total = 0
for i, item in enumerate(items, start=1):
    n = item[1]
    # print(n, i)
    total += i * n

print(total)