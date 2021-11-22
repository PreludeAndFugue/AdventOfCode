#!python3

'''Day 7.

For part 2 change value for b to the answer to part 1.
    956 ->b

'''

import operator

INPUT = 'day07.txt'
TEST_INPUT = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
'''


def parse_input(input):
    '''Parse input to dict.'''
    rows = (row.strip().split(' -> ') for row in input.strip().split('\n'))
    return {row[1]: Instruction.create(row[0]) for row in rows}


def noop(n):
    '''The no-op operator.'''
    return n


def my_eval(operand, instructions):
    return instructions


def my_not(n):
    '''16-bit not.'''
    return ~n & 0xffff


OPERATORS = {
    'NOOP': noop,
    'EVAL': my_eval,
    'OR': operator.or_,
    'AND': operator.and_,
    'NOT': my_not,
    'RSHIFT': operator.rshift,
    'LSHIFT': operator.lshift
}

NOOP = 'NOOP'
EVAL = 'EVAL'
OR = 'OR'
AND = 'AND'
NOT = 'NOT'
RSHIFT = 'RSHIFT'
LSHIFT = 'LSHIFT'


class Instruction(object):
    '''An Instruction.'''

    def __init__(self, operator_, operand1, operand2):
        self.operator = operator_
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = None


    def run(self, instructions):
        '''Run the instruction with the full instruction set.'''
        if self.result is not None:
            return self.result

        if self.operator == NOOP:
            self.result = self.operand1
        if self.operator == EVAL:
            self.result = self._evaluate_operand(self.operand1, instructions)
        if self.operator == OR:
            o1 = self._evaluate_operand(self.operand1, instructions)
            o2 = self._evaluate_operand(self.operand2, instructions)
            self.result = o1 | o2
        if self.operator == AND:
            o1 = self._evaluate_operand(self.operand1, instructions)
            o2 = self._evaluate_operand(self.operand2, instructions)
            self.result = o1 & o2
        if self.operator == NOT:
            o1 = self._evaluate_operand(self.operand1, instructions)
            self.result = my_not(o1)
        if self.operator == RSHIFT:
            o1 = self._evaluate_operand(self.operand1, instructions)
            self.result = o1 >> self.operand2
        if self.operator == LSHIFT:
            o1 = self._evaluate_operand(self.operand1, instructions)
            self.result = o1 << self.operand2

        return self.result


    def _evaluate_operand(self, operand, instructions):
        if operand.isdigit():
            return int(operand)
        return instructions[operand].run(instructions)


    @staticmethod
    def create(instruction):
        '''Create an instruction from raw input.'''
        if instruction.isdigit():
            return Instruction(NOOP, int(instruction), None)
        if AND in instruction:
            op1, _, op2 = instruction.split(' ')
            return Instruction(AND, op1, op2)
        if OR in instruction:
            op1, _, op2 = instruction.split(' ')
            return Instruction(OR, op1, op2)
        if NOT in instruction:
            _, op1 = instruction.split(' ')
            return Instruction(NOT, op1, None)
        if RSHIFT in instruction:
            op1, _, op2 = instruction.split(' ')
            return Instruction(RSHIFT, op1, int(op2))
        if LSHIFT in instruction:
            op1, _, op2 = instruction.split(' ')
            return Instruction(LSHIFT, op1, int(op2))
        return Instruction(EVAL, instruction, None)


    def __str__(self):
        '''String representation.'''
        return f'Instruction({self.operator}, {self.operand1}, {self.operand2})'


    def __repr__(self):
        return str(self)


def run(item, instructions):
    '''Run instruction.'''
    instructions[item]


def part1(data):
    return data['a'].run(data)


def part2(result, data):
    instruction_b = Instruction(NOOP, result, None)
    data['b'] = instruction_b
    return data['a'].run(data)


def main():
    data1 = parse_input(open(INPUT, 'r').read())
    p1 = part1(data1)
    print(p1)

    data2 = parse_input(open(INPUT, 'r').read())
    p2 = part2(p1, data2)
    print(p2)


if __name__ == '__main__':
    main()
