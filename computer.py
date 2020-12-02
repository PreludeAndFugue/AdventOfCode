#!python3

'''
Instructions:
- inc
- dec
- cpy
- jnz
- tgl
'''

from collections import namedtuple


class ComputeError(Exception):
    pass


Instruction = namedtuple('Instruction', ['name', 'x1', 'x2'])


def parse_instructions(instruction_input):
    '''Create a program from input.'''
    instructions = {}
    for n, line in enumerate(instruction_input.strip().split('\n')):
        parts = line.strip().split()
        print(line, parts)
        if line.startswith('cpy'):
            i = Instruction(parts[0], parts[1], parts[2])
            instructions[n] = i
        elif line.startswith('inc'):
            i = Instruction(parts[0], parts[1], None)
            instructions[n] = i
        elif line.startswith('dec'):
            i = Instruction(parts[0], parts[1], None)
            instructions[n] = i
        elif line.startswith('jnz'):
            i = Instruction(parts[0], parts[1], parts[2])
            instructions[n] = i
        elif line.startswith('tgl'):
            i = Instruction(parts[0], parts[1], None)
            instructions[n] = i
        else:
            raise IOError
    return instructions


def compute(instructions, registers):
    '''Run a program.'''
    pointer = 0
    while True:
        if pointer not in instructions:
            return registers['a']
        i = instructions[pointer]

        if i.name == 'inc':
            registers[i.x1] += 1
            pointer += 1
        elif i.name == 'dec':
            registers[i.x1] -= 1
            pointer += 1
        elif i.name == 'cpy':
            if i.x1.isalpha():
                registers[i.x2] = registers[i.x1]
            else:
                n = int(i.x1)
                registers[i.x2] = n
            pointer += 1
        elif i.name == 'jnz':
            if i.x2.isalpha():
                offset = registers[i.x2]
            else:
                offset = int(i.x2)
            if i.x1.isnumeric():
                n = int(i.x1)
                if n != 0:
                    pointer += offset
                else:
                    pointer += 1
            else:
                if registers[i.x1] != 0:
                    pointer += offset
                else:
                    pointer += 1
        elif i.name == 'tgl':
            offset = registers[i.x1]
            position = pointer + offset

            if position not in instructions:
                pointer += 1
            else:
                other_i = instructions[pointer + offset]
                instructions[pointer + offset] = _toggle(other_i)
                pointer += 1

            _print_instructions(instructions)
            print(pointer)
            print(registers)
        else:
            raise ComputeError(f'{i}, {registers}')


def _toggle(instruction):
    if instruction.name == 'inc':
        return Instruction('dec', instruction.x1, instruction.x2)
    elif instruction.name == 'dec' or instruction.name == 'tgl':
        return Instruction('inc', instruction.x1, instruction.x2)
    elif instruction.name == 'jnz':
        return Instruction('cpy', instruction.x1, instruction.x2)
    elif instruction.name == 'cpy':
        return Instruction('jnz', instruction.x1, instruction.x2)
    else:
        raise ComputeError('unfinished')


def _print_instructions(instructions):
    keys = sorted(instructions.keys())
    for k in keys:
        print(k, instructions[k])
