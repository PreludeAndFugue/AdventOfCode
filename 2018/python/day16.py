
from help import get_input

def parse(d):
    a, b = d.split('\n\n\n')
    a = a.split('\n\n')
    c = []
    for x in a:
        x1, x2, x3 = x.split('\n')
        x1 = x1[9:-1].split(', ')
        x1 = list(map(int, x1))
        x2 = list(map(int, x2.split()))
        x3 = x3[9:-1].split(', ')
        x3 = list(map(int, x3))
        c.append((x1, x2, x3))

    b = [b.split() for b in b.split('\n')]
    b = [list(map(int, x)) for x in b]

    return c, b


def addr(a, b, c, registers):
    registers[c] = registers[a] + registers[b]

def addi(a, b, c, registers):
    registers[c] = registers[a] + b

def mulr(a, b, c, registers):
    registers[c] = registers[a] * registers[b]

def muli(a, b, c, registers):
    registers[c] = registers[a] * b

def banr(a, b, c, registers):
    registers[c] = registers[a] & registers[b]

def bani(a, b, c, registers):
    registers[c] = registers[a] & b

def borr(a, b, c, registers):
    registers[c] = registers[a] | registers[b]

def bori(a, b, c, registers):
    registers[c] = registers[a] | b

def setr(a, b, c, registers):
    registers[c] = registers[a]

def seti(a, b, c, registers):
    registers[c] = a

def gtir(a, b, c, registers):
    registers[c] = 1 if a > registers[b] else 0

def gtri(a, b, c, registers):
    registers[c] = 1 if registers[a] > b else 0

def gtrr(a, b, c, registers):
    registers[c] = 1 if registers[a] > registers[b] else 0

def eqir(a, b, c, registers):
    registers[c] = 1 if a == registers[b] else 0

def eqri(a, b, c, registers):
    registers[c] = 1 if registers[a] == b else 0

def eqrr(a, b, c, registers):
    registers[c] = 1 if registers[a] == registers[b] else 0


opcodes = [
    addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr,
    eqir, eqri, eqrr
]


def part1(tests):
    answer = 0
    for before, op, after in tests:
        count = 0
        for opcode in opcodes:
            registers = {i: before[i] for i in range(4)}
            _, a, b, c = op
            opcode(a, b, c, registers)
            result = [registers[i] for i in range(4)]
            if result == after:
                count += 1
        if count >= 3:
            answer += 1

    return answer


def main():
    d = get_input('16').strip()
    tests, instructions = parse(d)

    p1 = part1(tests)
    print(p1)


if __name__ == '__main__':
    main()
