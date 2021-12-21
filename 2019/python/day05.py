#!python3

from computer import IntcodeComputer
from helpers import BASE


TEST01 = '''3,0,4,0,99'''

TEST02 = '''1002,4,3,4,33'''

TEST03 = '''3,9,8,9,10,9,4,9,99,-1,8'''

TEST04 = '''3,9,7,9,10,9,4,9,99,-1,8'''

TEST05 = '''3,3,1108,-1,8,3,4,3,99'''

TEST06 = '''3,3,1107,-1,8,3,4,3,99'''

TEST07 = '''3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'''

TEST08 = '''3,3,1105,-1,9,1101,0,0,12,4,12,99,1'''

TEST09 = '''3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'''


def tests():
    # t1 = list(map(int, TEST01.split(',')))
    # c1 = IntcodeComputer(t1)
    # c1.run()

    # t2 = list(map(int, TEST02.split(',')))
    # c2 = IntcodeComputer(t2)
    # c2.run()
    # assert c2.memory[-1] == 99

    # t3 = list(map(int, TEST03.split(',')))
    # c3 = IntcodeComputer(t3)
    # c3.run()

    # t4 = list(map(int, TEST04.split(',')))
    # c4 = IntcodeComputer(t4)
    # c4.run()

    # t5 = list(map(int, TEST05.split(',')))
    # c5 = IntcodeComputer(t5)
    # c5.run()

    # t6 = list(map(int, TEST06.split(',')))
    # c6 = IntcodeComputer(t6)
    # c6.run()

    # t7 = list(map(int, TEST07.split(',')))
    # c7 = IntcodeComputer(t7)
    # c7.run()

    # t8 = list(map(int, TEST08.split(',')))
    # c8 = IntcodeComputer(t8)
    # c8.run()

    t9 = list(map(int, TEST09.split(',')))
    c9 = IntcodeComputer(t9)
    c9.run()


def part1():
    # tests()

    program = list(map(int, open(BASE + 'day05.txt').read().strip().split(',')))
    c = IntcodeComputer(program)
    c.run()


def main():
    part1()


if __name__ == '__main__':
    main()
