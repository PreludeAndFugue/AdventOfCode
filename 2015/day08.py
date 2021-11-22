#!python3

'''Day 8'''

import re

INPUT = 'day08.txt'
TEST_INPUT = r'''""
"abc"
"aaa\"aaa"
"\x27"
'''


def convert_count(line):
    line = line[1:-1]
    line = re.sub(r'\\x[abcdef\d]{2}', 'X', line)
    line = re.sub(r"\\\\", "/", line)
    line = re.sub(r'\\"', '"', line)
    return len(line)


def convert2(line):
    line = re.sub(r'\\', r'\\\\', line)
    line = re.sub(r'"', r'\"', line)
    return line


def test1(data):
    assert part1(data) == 12


def part1(data):
    char_count = 0
    memory_count = 0
    for line in data:
        line = line.rstrip('\n')
        char_count += len(line)
        x = convert_count(line)
        memory_count += x
    return char_count - memory_count


def part2(data):
    x = 0
    y = 0
    for line in data:
        line = line.rstrip('\n')
        x += len(line)
        line = convert2(line)
        y += len(line) + 2
    return y - x


def main():
    data = open(INPUT, 'r').readlines()
    test_data = TEST_INPUT.split('\n')

    test1(test_data)

    p1 = part1(data)
    print(p1)

    p2 = part2(data)
    print(p2)


if __name__ == '__main__':
    main()
