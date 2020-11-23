#!python3

'''Day 8, part 1.'''

import re

from data_8 import file_data, file_data_test


def convert_count(line):
    line = line[1:-1]
    line = re.sub(r'\\x[abcdef\d]{2}', 'X', line)
    line = re.sub(r"\\\\", "/", line)
    line = re.sub(r'\\"', '"', line)
    return len(line), line


def convert2(line):
    line = re.sub(r'\\', r'\\\\', line)
    line = re.sub(r'"', r'\"', line)
    return line


def test1():
    for line in file_data_test:
        line = line.strip('\n')
        print(len(line), line)
        print(convert_count(line))
        print()


def main():
    char_count = 0
    memory_count = 0
    for line in file_data:
        line = line.rstrip('\n')
        char_count += len(line)
        print(len(line), line)
        x, y = convert_count(line)
        memory_count += x
        print(x, y)
        print()

        assert(len(line) > x)

    print(char_count, memory_count, char_count - memory_count)


def main2():
    x = 0
    y = 0
    for line in file_data:
        line = line.rstrip('\n')
        print(len(line), line)
        x += len(line)
        line = convert2(line)
        print(len(line) + 2, line)
        y += len(line) + 2
        print()

    print(x, y, y - x)


if __name__ == '__main__':
    # test1()
    # main()
    main2()
