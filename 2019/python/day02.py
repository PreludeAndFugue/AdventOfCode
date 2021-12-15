#!python

from computer import IntcodeComputer
from helpers import BASE


def part1(program):
    program[1] = 12
    program[2] = 2
    c = IntcodeComputer(program)
    c.run()
    return c.memory[0]


def part2(program):
    for noun in range(100):
        for verb in range(100):
            p = program.copy()
            p[1] = noun
            p[2] = verb
            c = IntcodeComputer(p)
            c.run()
            o = c.memory[0]
            if o == 19690720:
                return 100 * noun + verb


def main():
    c1 = IntcodeComputer([1,0,0,0,99])
    c1.run()
    assert c1.memory == [2,0,0,0,99]

    c2 = IntcodeComputer([2,3,0,3,99])
    c2.run()
    assert c2.memory == [2,3,0,6,99]

    c3 = IntcodeComputer([2,4,4,5,99,0])
    c3.run()
    assert c3.memory == [2,4,4,5,99,9801]

    c4 = IntcodeComputer([1,1,1,4,99,5,6,0,99])
    c4.run()
    assert c4.memory == [30,1,1,4,2,5,6,0,99]

    program = list(map(int, open(BASE + 'day02.txt', 'r').read().strip().split(',')))

    p1 = part1(program.copy())
    print(f'Part 1: {p1}')

    p2 = part2(program.copy())
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
