#!python3

'''Day 21, part 1.'''

from data_21 import (
    find_match, join_patterns, patterns, pattern_parts, start, test_patterns,
    test_start, Pattern
)


def test():
    pattern = test_start

    for i in range(2):
        parts = pattern_parts(pattern)
        parts = [find_match(part, test_patterns).replacement for part in parts]
        pattern = join_patterns(parts)

    print(pattern)
    print(pattern.count('#'))


def main():
    pattern = start

    for i in range(18):
        # print(pattern)
        parts = pattern_parts(pattern)
        # print('parts1', parts)

        parts = [find_match(part, patterns).replacement for part in parts]
        # print('parts2', parts)
        pattern = join_patterns(parts)
        # print('\n')

    # print(pattern)
    print(pattern.count('#'))


if __name__ == '__main__':
    # test()
    main()
