
from help import get_input

TEST1 = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''


source = get_input(1)
# source = TEST1.strip()
# print(source)

n = 50
c = 0
for line in source.split('\n'):
    # print(line)
    d = line[0]
    m = int(line[1:])
    if d == 'L':
        n -= m
        n %= 100
    elif d == 'R':
        n += m
        n %= 100
    if n == 0:
        c += 1
print(c)
