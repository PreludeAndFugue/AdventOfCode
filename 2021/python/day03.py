#!python

import helpers


TEST01 = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''.strip().split()


def part1(numbers):
    gamma = []
    epsilon = []
    for x in zip(*numbers):
        y = sum(1 if b == '1' else -1 for b in x)
        if y > 0:
            gamma.append('1')
            epsilon.append('0')
        elif y < 0:
            gamma.append('0')
            epsilon.append('1')
        else:
            raise ValueError
    gamma = int(''.join(gamma), base=2)
    epsilon = int(''.join(epsilon), base=2)
    return gamma * epsilon


def filter_numbers(numbers, index, most_common):
    a = '1' if most_common else '0'
    b = '0' if most_common else '1'
    x = sum(1 if n[index] == '1' else -1 for n in numbers)
    if x >= 0:
        return [n for n in numbers if n[index] == a]
    elif x < 0:
        return [n for n in numbers if n[index] == b]


def find_number(numbers, most_common):
    index = 0
    while len(numbers) > 1:
        numbers = filter_numbers(numbers, index, most_common)
        index += 1
    return int(numbers[0], base=2)


def part2(numbers):
    oxygen = find_number(numbers, True)
    co2 = find_number(numbers, False)
    return oxygen * co2


def main():
    test_numbers = TEST01
    numbers = open(helpers.BASE + 'day03.txt', 'r').read().strip().split()

    t1 = part1(test_numbers)
    assert t1 == 198

    p1 = part1(numbers)
    print(f'Part 1: {p1}')

    t2 = part2(test_numbers)
    assert t2 == 230

    p2 = part2(numbers)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
