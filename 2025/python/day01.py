
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
    for i in range(m):
        if d == 'L':
            n -= 1
            n %= 100
            if n == 0:
                c += 1
        elif d == 'R':
            n += 1
            n %= 100
            if n == 0:
                c += 1
        else:
            raise ValueError(f'Unknown direction: {d}')

print(c)
