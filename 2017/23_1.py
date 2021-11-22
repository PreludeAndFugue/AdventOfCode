#!python3

'''Day 23, part 1.'''

from collections import defaultdict

from data_23 import instructions, instructions2, Program


def main1():
    print(instructions)
    program = Program(instructions, defaultdict(int))
    program.run()
    print(program.mul_count)


def main2():
    registers = defaultdict(int)
    registers['a'] = 1
    program = Program(instructions, registers)
    program.run()


if __name__ == '__main__':
    # main1()
    main2()
