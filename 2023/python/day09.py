
from help import get_input

TEST = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''


def get_diffs(ns):
    diffs = [n2 - n1 for n1, n2 in zip(ns, ns[1:])]
    if not any(diffs):
        return 0
    return diffs[-1] + get_diffs(diffs)


d = get_input('09').strip()
# d = TEST.strip()

p1 = 0
p2 = 0
for l in d.split('\n'):
    ns1 = [int(n) for n in l.split()]
    ns2 = list(reversed(ns1))
    p1 += ns1[-1] + get_diffs(ns1)
    p2 += ns2[-1] + get_diffs(ns2)

print(p1)
print(p2)
