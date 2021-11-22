#!python3

'''Day 5'''

translation = str.maketrans('aeiou', 'aeiou', 'bcdfghjklmnpqrstvwxyz')


INPUT = 'day05.txt'

TEST_DATA = [
    'ugknbfddgicrmopn',
    'aaa',
    'jchzalrnumimnmhp',
    'haegwjzuvuyypxyu',
    'dvszwmarrgswjxmb'
]
TEST_RESULT = [True, True, False, False, False]

TEST_DATA_2 = [
    'qjhvhtzxzqqjkmpb',
    'xxyxx',
    'uurcxstgmygtbstg',
    'ieodomkazucvgmuy'
]
TEST_RESULT_2 = [True, True, False, False]


def parse_input(input):
    return input.strip().split('\n')


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


def is_nice1(s):
    if not has_double(s):
        return False
    if not has_three_vowels(s):
        return False
    if has_illegal_strings(s):
        return False
    return True


def part1(input):
    return sum(is_nice1(s) for s in input)


def test1():
    for x, result in zip(TEST_DATA, TEST_RESULT):
        assert is_nice1(x) == result


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


def is_nice2(s):
    if not pair_repeat(s):
        return False
    if not repeat3(s):
        return False
    return True


def part2(input):
    result = sum(is_nice2(s) for s in input)
    return result


def test2():
    for x, result in zip(TEST_DATA_2, TEST_RESULT_2):
        assert is_nice2(x) == result


def main():
    input = parse_input(open(INPUT, 'r').read())

    test1()

    p1 = part1(input)
    print(p1)

    test2()

    p2 = part2(input)
    print(p2)


if __name__ == "__main__":
    main()
