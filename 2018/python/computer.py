
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
