#!python3

from collections import namedtuple
from copy import deepcopy


INPUT = 'day08.txt'
TEST_INPUT = '''
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''


Instruction = namedtuple('Instruction', ['name', 'value'])


def get_instructions(input):
    instructions = []
    for line in input.strip().split('\n'):
        name, value = line.strip().split(' ')
        value = int(value)
        i = Instruction(name, value)
        instructions.append(i)
    return instructions


class Computer(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.accumulator = 0
        self.pointer = 0
        self.pointer_history = set()


    def run(self):
        while True:
            if self.pointer == len(self.instructions):
                return self.accumulator, True

            instruction = self.instructions[self.pointer]
            if self.pointer in self.pointer_history:
                return self.accumulator, False
            self.pointer_history.add(self.pointer)

            if instruction.name == 'nop':
                self._nop()
            elif instruction.name == 'acc':
                self._acc(instruction)
            elif instruction.name == 'jmp':
                self._jmp(instruction)
            else:
                raise IOError

        raise IOError('Missing infinite loop')


    def _nop(self):
        self.pointer += 1


    def _acc(self, instruction):
        self.accumulator += instruction.value
        self.pointer += 1


    def _jmp(self, instruction):
        self.pointer += instruction.value


def swap_instruction(instruction):
    if instruction.name == 'nop':
        return Instruction('jmp', instruction.value)
    elif instruction.name == 'jmp':
        return Instruction('nop', instruction.value)
    else:
        raise IOError('Invalid instruction')



def test1(instructions):
    computer = Computer(instructions)
    n, _ = computer.run()
    assert n == 5


def part1(instructions):
    computer = Computer(instructions)
    n, _ = computer.run()
    return n


def _part2(instructions):
    for i, instruction in enumerate(instructions):
        if instruction.name == 'acc':
            continue
        new_instruction = swap_instruction(instruction)
        computer_instructions = deepcopy(instructions)
        computer_instructions[i] = new_instruction
        computer = Computer(computer_instructions)
        n, result = computer.run()
        if result:
            return n


def test2(instructions):
    n = _part2(instructions)
    assert n == 8


def part2(instructions):
    n = _part2(instructions)
    return n


def main():
    test_instructions = get_instructions(TEST_INPUT)
    instructions = get_instructions(open(INPUT, 'r').read())

    test1(test_instructions)

    p = part1(instructions)
    print(p)

    test2(test_instructions)

    p = part2(instructions)
    print(p)


if __name__ == "__main__":
    main()
