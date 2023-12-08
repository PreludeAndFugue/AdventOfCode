
from itertools import cycle

from help import get_input

TEST1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''

TEST2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''


d = get_input('08').strip()
# d = TEST1.strip()
# d = TEST2.strip()
directions, b = d.split('\n', maxsplit=1)
directions = directions.strip()

m = {}
for l in b.strip().split('\n'):
    p = l.split(' = ')
    x, y = p[0], p[1]
    y = y.replace('(', '')
    y = y.replace(')', '')
    y = y.split(', ')
    m[x] = y

ns = {'L': 0, 'R': 1}
p = 'AAA'
c = 0
for d in cycle(directions):
    p = m[p][ns[d]]
    c += 1
    print(p, d, c)
    if p == 'ZZZ':
        break
