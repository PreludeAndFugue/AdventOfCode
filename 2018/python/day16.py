
from collections import defaultdict

from help import get_input
from computer import *

def parse(d):
    a, b = d.split('\n\n\n\n')
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


def part1(tests):
    answer = 0
    opcode_ids = defaultdict(set)
    for before, op, after in tests:
        count =0
        for i, opcode in enumerate(opcodes):
            registers = {i: before[i] for i in range(4)}
            opcode_id, a, b, c = op
            opcode(a, b, c, registers)
            result = [registers[i] for i in range(4)]
            if result == after:
                count += 1
                opcode_ids[opcode_id].add(i)
        if count >= 3:
            answer += 1
    return answer, opcode_ids


def part2(opcode_dict, instructions):
    result = {}
    kk = None
    vv = None
    for _ in range(16):
        for k, v in opcode_dict.items():
            if len(v) == 1:
                kk = k
                vv = v.pop()
                result[k] = vv
                break
        del opcode_dict[kk]
        for v in opcode_dict.values():
            if vv in v:
                v.remove(vv)
    new_opcodes = {}
    for k, v in result.items():
        new_opcodes[k] = opcodes[v]

    registers = {i: 0 for i in range(4)}
    for instruction in instructions:
        i, a, b, c = instruction
        opcode = new_opcodes[i]
        opcode(a, b, c, registers)
    return registers[0]


def main():
    d = get_input('16').strip()
    tests, instructions = parse(d)

    p1, opcode_dict = part1(tests)
    print(p1)

    p2 = part2(opcode_dict, instructions)
    print(p2)


if __name__ == '__main__':
    main()
