
from help import get_input

test1 = '''1
10
100
2024'''


def secret(n):
    b = 64*n
    n = n^b
    n = n % 16777216
    b = n//32
    n = n^b
    n = n % 16777216
    b = 2048*n
    n = n^b
    n = n % 16777216
    return n


source = test1.strip()
source = get_input(22)

ns = [int(x) for x in source.split('\n')]

t = 0
for n in ns:
    for i in range(2000):
        n = secret(n)
    t += n
print(t)
