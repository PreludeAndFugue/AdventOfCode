#!python3

'''2.1'''

from collections import Counter

INPUT = '2.txt'

two_count = 0
three_count = 0

with open(INPUT) as f:
    for line in f:
        count = Counter(line)
        values = set(count.values())
        if 2 in values:
            two_count += 1
        if 3 in values:
            three_count += 1

print(two_count)
print(three_count)
print(two_count * three_count)
