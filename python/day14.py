#!python3

from collections import defaultdict, namedtuple
import re

INPUT = 'day14.txt'
TEST_INPUT = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
'''

class Mask(object):
    def __init__(self, mask):
        self.mask = mask


    def apply(self, value):
        value = value | self._one_mask
        value = value & self._zero_mask
        return value


    @property
    def _one_mask(self):
        return int(''.join('1' if x == '1' else '0' for x in self.mask), base=2)


    @property
    def _zero_mask(self):
        return int(''.join('0' if x == '0' else '1' for x in self.mask), base=2)


Memory = namedtuple('Memory', ['address', 'value'])

MEM = re.compile(r'^mem\[(\d+)\] = (\d+)')

def get_input(input):
    for line in input.strip().split('\n'):
        if line.startswith('mask'):
            m = line.split(' = ')[1]
            yield Mask(m)
        elif line.startswith('mem'):
            match = re.match(MEM, line)
            address, value = list(map(int, match.groups()))
            yield Memory(address, value)
        else:
            raise IOError(line)


def _part1(instructions):
    memory = defaultdict(int)
    mask = None
    for instruction in instructions:
        if isinstance(instruction, Mask):
            mask = instruction
        elif isinstance(instruction, Memory):
            value = mask.apply(instruction.value)
            memory[instruction.address] = value
        else:
            raise IOError
    return sum(v for v in memory.values())


def test1():
    instructions = get_input(TEST_INPUT)
    assert _part1(instructions) == 165


def part1():
    instructions = get_input(open(INPUT, 'r').read())
    return _part1(instructions)


def main():
    test1()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
