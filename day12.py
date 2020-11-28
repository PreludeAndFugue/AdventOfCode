#!python3


from collections import namedtuple

INPUT = open('day12.txt', 'r').read()

TEST_INPUT = '''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''

Instruction = namedtuple('Instruction', ['name', 'x1', 'x2'])


def parse(instruction_input):
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



def compute(instructions):
    '''Run a program.'''
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
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



def main():
    instructions = parse(INPUT)
    print(instructions)
    a = compute(instructions)
    print(a)



if __name__ == '__main__':
    main()
