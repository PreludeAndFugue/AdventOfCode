#!python3


'''

Part 2
------

a: 132
b: 10
c: 20

a: 1320
b: 9
c: 18

a: 11880
b: 8
c: 16

a: 95040
b: 7
c: 14

a: 665280
b: 6
c: 12

a: 3991680
b: 5
c: 10

a: 19958400
b: 4
c: 8

a: 79833600
b: 3
c: 6



->
a: 239500800
b: 2

a: 479001600
b: 1

+ 79 * 97
-> 479,009,263
'''


from computer import Instruction, parse_instructions, compute


INPUT = 'day23.txt'
TEST_INPUT = '''cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a'''


def test1():
    registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    instructions = parse_instructions(TEST_INPUT)
    compute(instructions, registers)
    assert registers['a'] == 3


def part1():
    registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
    instructions = parse_instructions(open(INPUT, 'r').read())
    compute(instructions, registers)
    return registers['a']


def main():
    test1()
    p = part1()
    print(p)


if __name__ == '__main__':
    main()
