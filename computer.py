#!python3

from collections import namedtuple

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
            i = Instruction(parts[0], parts[1], int(parts[2]))
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
            if i.x1.isnumeric():
                n = int(i.x1)
                registers[i.x2] = n
            else:
                registers[i.x2] = registers[i.x1]
            pointer += 1
        elif i.name == 'jnz':
            if i.x1.isnumeric():
                n = int(i.x1)
                if n != 0:
                    pointer += i.x2
                else:
                    pointer += 1
            else:
                if registers[i.x1] != 0:
                    pointer += i.x2
                else:
                    pointer += 1
