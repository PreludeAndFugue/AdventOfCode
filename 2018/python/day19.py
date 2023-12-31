from help import get_input
from computer import *

TEST = '''
#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5
'''

OPCODES = {
    'addi': addi,
    'addr': addr,
    'muli': muli,
    'mulr': mulr,
    'bani': bani,
    'banr': banr,
    'bori': bori,
    'borr': borr,
    'seti': seti,
    'setr': setr,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr
}


def parse(d):
    lines = d.split('\n')
    ip_no = int(lines[0][4:])
    instructions = []
    for line in lines[1:]:
        line = line.split(' ')
        opcode = line[0]
        ns = list(map(int, line[1:]))
        instructions.append((opcode, *ns))

    return ip_no, instructions


def part1(ip_no, instructions):
    pointer_range = range(len(instructions))
    registers = {i: 0 for i in range(6)}
    pointer = 0
    while pointer in pointer_range:
        registers[ip_no] = pointer
        opcode_id, a, b, c = instructions[pointer]
        opcode = OPCODES[opcode_id]
        opcode(a, b, c, registers)
        pointer = registers[ip_no]
        pointer += 1
    print(registers)


def main():
    d = get_input('19').strip()
    # d = TEST.strip()
    ip_no, instructions = parse(d)

    part1(ip_no, instructions)


if __name__ == '__main__':
    main()
