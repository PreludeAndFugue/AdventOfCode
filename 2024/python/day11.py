
from collections import defaultdict

from help import get_input

test1 = '''125 17'''

def update(n):
    if n == 0:
        return [1]
    s = str(n)
    l = len(s)
    if l % 2 == 0:
        s1 = s[:l//2]
        s2 = s[l//2:]
        return [int(s1), int(s2)]
    return [2024*n]


def update_all(map_):
    new_map = defaultdict(int)
    for n, c in map_.items():
        ns = update(n)
        for nn in ns:
            new_map[nn] += c
    return new_map


source = get_input(11)
# source = test1.strip()

ns = list(map(int, source.split()))
map_ = defaultdict(int)
for n in ns:
    map_[n] += 1

for _ in range(25):
    map_ = update_all(map_)
s = sum(v for v in map_.values())
print(s)