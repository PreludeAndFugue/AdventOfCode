#!python3

from computer import Instruction, parse_instructions, compute

INPUT = open('day12.txt', 'r').read()

TEST_INPUT = '''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''


def main():
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    instructions = parse_instructions(INPUT)
    print(instructions)
    a = compute(instructions, registers)
    print(a)


if __name__ == '__main__':
    main()
