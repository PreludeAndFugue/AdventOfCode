
from help import get_input

test1 = '''3   4
4   3
2   5
1   3
3   9
3   3'''

source = get_input(1)
# source = test1.strip()
aa = []
bb = []
for line in source.split('\n'):
    a, b = map(int, (line.split('   ')))
    aa.append(a)
    bb.append(b)
aa.sort()
bb.sort()

s = sum(abs(a - b) for a, b in zip(aa, bb))
print(s)
