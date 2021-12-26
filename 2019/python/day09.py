#!python3

from computer import IntcodeComputer, Console
from helpers import BASE


def part1(program):
    c = Console([1])
    ic = IntcodeComputer(program, c)
    ic.run()
    return c.readline()


def part2(program):
    c = Console([2])
    ic = IntcodeComputer(program, c)
    ic.run()
    return c.readline()


def main():
    program = list(map(int, open(BASE + 'day09.txt', 'r').read().strip().split(',')))

    p1 = part1(program)
    print(f'Part 1: {p1}')

    p2 = part2(program)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
