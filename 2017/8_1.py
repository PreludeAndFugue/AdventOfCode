#!python3

'''Day 8, part 1.'''

import data_8


def find_max(registers):
    '''Find the max register value.'''
    max_value = 0
    for k, v in registers:
        if v > max_value:
            max_value = v
    return max_value


def main():
    '''Main entry point'''
    instructions = data_8.instructions
    registers = data_8.Registers()
    for instruction in instructions:
        registers.update(instruction)

    print(registers)

    max_value = find_max(registers)
    print(max_value)


if __name__ == '__main__':
    main()
