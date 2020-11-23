#!python3

'''Day 5, part 2.'''

import data_5

test_data = [
    'qjhvhtzxzqqjkmpb',
    'xxyxx',
    'uurcxstgmygtbstg',
    'ieodomkazucvgmuy'
]

def pair_repeat(s):
    '''Pair repeat.

    >>> pair_repeat('aaa')
    False
    >>> pair_repeat('aaaa')
    True
    >>> pair_repeat('xyxy')
    True
    >>> pair_repeat('aabcdefgaa')
    True
    >>> pair_repeat('ieodomkazucvgmuy')
    False
    >>> pair_repeat('abc')
    False
    >>> pair_repeat('abcaa')
    False
    '''
    count = len(s)
    for i in range(count - 2):
        x = s[i:i + 2]
        if s.count(x) > 1:
            return True
    return False


def repeat3(s):
    '''Find repeat3 pattern: aba

    >>> repeat3('xyx')
    True
    >>> repeat3('xyxy')
    True
    >>> repeat3('uurcxstgmygtbstg')
    False
    >>> repeat3('ieodomkazucvgmuy')
    True
    >>> repeat3('abcdefeghi')
    True
    >>> repeat3('aaa')
    True
    >>> repeat3('abba')
    False
    >>> repeat3('abbab')
    True
    '''
    count = len(s)
    if count < 3:
        return False
    if count == 3:
        return s[0] == s[2]
    for i in range(count - 2):
        x = s[i:i + 3]
        if x[0] == x[2]:
            return True
    return False


def is_nice(s):
    if not pair_repeat(s):
        return False
    if not repeat3(s):
        return False
    return True


result = sum(is_nice(s) for s in data_5.strings)
print(result)


for s in test_data:
    print(s, is_nice(s))
