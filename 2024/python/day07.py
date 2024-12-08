
from itertools import product
from operator import add, mul

from help import get_input

test1 = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''


def concat(n1, n2):
    if n2 < 10:
        return 10*n1 + n2
    elif n2 < 100:
        return 100*n1 + n2
    elif n2 < 1000:
        return 1000*n1 + n2
    else:
        raise ValueError
    # return int(str(n1) + str(n2))


OPERATORS = (mul, add, concat)


def parse(source):
    for line in source.split('\n'):
        a, b = line.split(': ')
        a = int(a)
        b = list(map(int, b.split()))
        yield a, b


def check(m, ns, operators):
    result = ns[0]
    for n, op in zip(ns[1:], operators):
        result = op(result, n)
        if result > m:
            return False
    return result == m


# source = test1.strip()
source = get_input(7)

p1 = 0
for m, ns in parse(source):
    repeat = len(ns) - 1
    for operators in product(OPERATORS, repeat=repeat):
        if check(m, ns, operators):
            p1 += m
            break

print(p1)
