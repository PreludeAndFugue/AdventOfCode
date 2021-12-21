#!python3

from computer import IntcodeComputer
from helpers import BASE


TEST01 = '''3,0,4,0,99'''

TEST02 = '''1002,4,3,4,33'''


def tests():
    # t1 = list(map(int, TEST01.split(',')))
    # c1 = IntcodeComputer(t1)
    # c1.run()

    t2 = list(map(int, TEST02.split(',')))
    c2 = IntcodeComputer(t2)
    c2.run()
    assert c2.memory[-1] == 99


def part1():
    tests()

    program = list(map(int, open(BASE + 'day05.txt').read().strip().split(',')))
    c = IntcodeComputer(program)
    c.run()


def main():
    part1()


if __name__ == '__main__':
    main()
