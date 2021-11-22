#!python3

'''Day 8, part 2.'''

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
    max_value = 0

    for instruction in instructions:
        registers.update(instruction)
        current_max = find_max(registers)
        if current_max > max_value:
            max_value = current_max

    print(registers)
    print(max_value)


if __name__ == '__main__':
    main()
