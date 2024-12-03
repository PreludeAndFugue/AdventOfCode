
from help import get_input

from itertools import combinations

test1 = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

def is_safe(ns):
    diffs = [n2 - n1 for n1, n2 in zip(ns, ns[1:])]
    d0 = diffs[0]
    if d0 == 0:
        return False
    is_positive = d0 > 0
    if abs(d0) > 3:
        return False
    for di in diffs[1:]:
        if di == 0:
            return False
        is_p = di > 0
        if is_p != is_positive:
            return False
        if abs(di) > 3:
            return False
    return True


def is_safe2(ns):
    if is_safe(ns):
        return True
    for c in combinations(ns, len(ns) - 1):
        if is_safe(list(c)):
            return True
    return False


safe = 0
safe2 = 0
for line in get_input(2).strip().split('\n'):
# for line in test1.strip().split('\n'):
    ns = [int(n) for n in line.split()]
    if is_safe(ns):
        safe += 1
    if is_safe2(ns):
        safe2 += 1

print(safe, safe2)

