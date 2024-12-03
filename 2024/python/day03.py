
from help import get_input

import re

test1 = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''
test2 = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

source = get_input(3)
# source = test1.strip()
# source = test2.strip()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
regex = re.compile(pattern)

total = 0
do_mul = True
for line in source.split('\n'):
    for x in regex.finditer(line):
        item = x.group()
        if item == "don't()":
            do_mul = False
        elif item == "do()":
            do_mul = True
        else:
            if not do_mul:
                continue
            m = int(x.group(1))
            n = int(x.group(2))
            total += m * n

print(total)