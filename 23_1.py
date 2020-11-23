#!python3

from collections import namedtuple

INPUT = '23.txt'

Instruction = namedtuple('Instruction', ['name', 'register', 'increment'])

def make_instructions():
    instructions = []
    with open(INPUT, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('inc'):
                register = line.split(' ')[1]
                instructions.append(Instruction('inc', register, 0))
            elif line.startswith('hlf'):
                register = line.split(' ')[1]
                instructions.append(Instruction('hlf', register, 0))
            elif line.startswith('tpl'):
                register = line.split(' ')[1]
                instructions.append(Instruction('tpl', register, 0))
            elif line.startswith('jmp'):
                increment = int(line.split(' ')[1])
                instructions.append(Instruction('jmp', None, increment))
            elif line.startswith('jio'):
                part = line.split(' ', maxsplit=1)[1]
                register, increment = part.split(', ')
                increment = int(increment)
                instructions.append(Instruction('jio', register, increment))
            elif line.startswith('jie'):
                part = line.split(' ', maxsplit=1)[1]
                register, increment = part.split(', ')
                increment = int(increment)
                instructions.append(Instruction('jie', register, increment))
            else:
                assert False
    return instructions


def part1():
    registers = {'a': 1, 'b': 0}
    instructions = make_instructions()
    pointer = 0
    r = range(0, len(instructions))
    while True:
        if pointer not in r:
            return registers['b']
        instruction = instructions[pointer]
        if instruction.name == 'inc':
            registers[instruction.register] = registers[instruction.register] + 1
            pointer += 1
        elif instruction.name == 'hlf':
            registers[instruction.register] = registers[instruction.register] / 2
            pointer += 1
        elif instruction.name == 'tpl':
            registers[instruction.register] = 3 * registers[instruction.register]
            pointer += 1
        elif instruction.name == 'jmp':
            pointer += instruction.increment
        elif instruction.name == 'jio':
            value = registers[instruction.register]
            if value == 1:
                pointer += instruction.increment
            else:
                pointer += 1
        elif instruction.name == 'jie':
            value = registers[instruction.register]
            if value % 2 == 0:
                pointer += instruction.increment
            else:
                pointer += 1
        else:
            assert False


def main():
    b = part1()
    print(b)


if __name__ == '__main__':
    main()
