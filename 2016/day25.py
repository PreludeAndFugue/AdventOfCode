#!python3

'''
Greater than 37_000_000.
'''

from computer import parse_instructions, compute

INPUT = 'day25.txt'


def part1():
    # registers = {'a': 1, 'b': 0, 'c': 0, 'd': 0}
    instructions = parse_instructions(open(INPUT, 'r').read())
    result = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

    for a in range(20_000, 30_000):
        registers = {'a': a, 'b': 0, 'c': 0, 'd': a + 15 * 170}
        n = compute(instructions, registers)
        # print(a)
        # print(n)
        # print()
        if n == result:
            print(a)
            break


def main():
    p = part1()
    print(p)


if __name__ == "__main__":
    main()
