#!python3

'''Day 5, part 1.'''

import data_5

translation = str.maketrans('aeiou', 'aeiou', 'bcdfghjklmnpqrstvwxyz')

test_data = [
    'ugknbfddgicrmopn',
    'aaa',
    'jchzalrnumimnmhp',
    'haegwjzuvuyypxyu',
    'dvszwmarrgswjxmb'
]

def has_double(s):
    for x, y in zip(s[:-1], s[1:]):
        if x == y:
            return True
    return False


def has_three_vowels(s):
    s = s.translate(translation)
    return len(s) >= 3


def has_illegal_strings(s):
    for x in ['ab', 'cd', 'pq', 'xy']:
        if x in s:
            return True
    return False


def is_nice(s):
    if not has_double(s):
        return False
    if not has_three_vowels(s):
        return False
    if has_illegal_strings(s):
        return False
    return True



result = sum(is_nice(s) for s in data_5.strings)
print(result)

for x in test_data:
    print(x, is_nice(x))

