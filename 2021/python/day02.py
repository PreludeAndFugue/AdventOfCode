#!python

import helpers


TEST01 = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''


def parse(text):
    for line in text.strip().split('\n'):
        line = line.strip()
        a, b = line.split()
        yield a, int(b)


def read():
    with open(helpers.BASE + 'day02.txt', 'r') as f:
        return parse(f.read())


def part1(instructions):
    depth = 0
    total_distance = 0
    for direction, distance in instructions:
        if direction == 'up':
            depth -= distance
        elif direction == 'down':
            depth += distance
        elif direction == 'forward':
            total_distance += distance
        else:
            ValueError
    return depth * total_distance


def part2(instructions):
    depth = 0
    total_distance = 0
    aim = 0
    for direction, distance in instructions:
        if direction == 'up':
            aim -= distance
        elif direction == 'down':
            aim += distance
        elif direction == 'forward':
            total_distance += distance
            depth += distance * aim
    return depth * total_distance


def main():
    test_instructions = list(parse(TEST01))
    instructions = list(read())

    answer = part1(test_instructions)
    assert answer == 150

    answer = part1(instructions)
    print(f'Part 1: {answer}')

    answer = part2(test_instructions)
    assert answer == 900

    answer = part2(instructions)
    print(f'Part 2: {answer}')


if __name__ == '__main__':
    main()
