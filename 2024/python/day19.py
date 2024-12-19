
from functools import cache

from help import get_input

test1 = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''


def parse(source):
    a, b = source.split('\n\n')
    a = a.split(', ')
    b = b.split('\n')
    return a, b


@cache
def check(design):
    if design == '':
        return True
    checks = []
    for p in patterns:
        if design.startswith(p):
            d = design[len(p):]
            c = check(d)
            checks.append(c)
    return any(checks)


source = test1.strip()
source = get_input(19)

patterns, designs = parse(source)

t = 0
for d in designs:
    c = check(d)
    if c:
        t += 1

print(t)
