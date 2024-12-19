
from help import get_input

test1 = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''


def parse(source):
    abc, p = source.split('\n\n')
    a, b, c = abc.split('\n')
    a = int(a.split(': ')[1])
    b = int(b.split(': ')[1])
    c = int(c.split(': ')[1])
    p = list(map(int, p.split(': ')[1].split(',')))
    return {'A': a, 'B': b, 'C': c}, p


def combo(n, registers):
    if 0 <= n <= 3:
        return n
    elif n == 4:
        return registers['A']
    elif n == 5:
        return registers['B']
    elif n == 6:
        return registers['C']
    else:
        raise ValueError


def adv(operand, registers):
    '''combo operand'''
    n = registers['A']
    d = combo(operand, registers)
    d = pow(2, d)
    registers['A'] = n // d


def bxl(operand, registers):
    '''literal operand'''
    b = registers['B']
    registers['B'] = b ^ operand


def bst(operand, registers):
    '''combo operand'''
    n = combo(operand, registers) % 8
    registers['B'] = n


def jnz(operand, registers):
    '''literal operand'''
    if registers['A'] == 0:
        return -1
    else:
        # print('jnz -> jump', operand)
        return operand


def bxc(operand, registers):
    '''ignore operand'''
    b = registers['B']
    c = registers['C']
    registers['B'] = b ^ c


def out(operand, registers):
    '''combo operand'''
    n = combo(operand, registers)
    return n % 8


def bdv(operand, registers):
    '''combo operand'''
    n = registers['A']
    d = combo(operand, registers)
    d = pow(2, d)
    registers['B'] = n // d


def cdv(operand, registers):
    '''combo operand'''
    n = registers['A']
    d = combo(operand, registers)
    d = pow(2, d)
    registers['C'] = n // d


opcodes = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}


def run(registers, program):
    pointer = 0
    result = []
    while True:
        try:
            opcode = program[pointer]
        except IndexError:
            break
        operand = program[pointer + 1]
        # print(pointer, ':', opcode, operand)
        match opcode:
            case 0 | 1 | 2 | 4 | 6 | 7:
                opcodes[opcode](operand, registers)
                pointer += 2
            case 3:
                n = jnz(operand, registers)
                if n != -1:
                    pointer = n
                else:
                    pointer += 2
            case 5:
                n = out(operand, registers)
                result.append(str(n))
                pointer += 2
                # print(result)
        # print(registers)
        # input()
    return ','.join(result)



# source = test1.strip()
source = get_input(17)
registers, program = parse(source)

print(registers)
print(program)

r = run(registers, program)
print(r)
