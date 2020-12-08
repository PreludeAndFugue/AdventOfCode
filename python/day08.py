#!python3

from collections import namedtuple


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
            instruction = self.instructions[self.pointer]
            if self.pointer in self.pointer_history:
                return self.accumulator
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


def test1():
    instructions = get_instructions(TEST_INPUT)
    computer = Computer(instructions)
    n = computer.run()
    assert n == 5


def part1():
    instructions = get_instructions(open(INPUT, 'r').read())
    computer = Computer(instructions)
    n = computer.run()
    return n


def main():
    test1()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
