
import re
from help import get_input

d = '05'

PATTERN = re.compile('move (\d+) from (\d+) to (\d+)')

STACKS = [
    'SZPDLBFC',
    'NVGPHWB',
    'FWBJG',
    'GJNFLWCS',
    'WJLTPMSH',
    'BCWGFS',
    'HTPMQBW',
    'FSWT',
    'NCR',
]

TEST_STACKS = [
    'ZN',
    'MCD',
    'P'
]

TEST = '''    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''


def setup_stacks(stacks):
    stacks = [[t for t in s] for s in stacks]
    stacks.insert(0, [])
    return stacks


def get_instructions(s):
    for line in s.strip().split('\n'):
        m = re.match(PATTERN, line)
        if m is None:
            continue
        yield list(map(int, m.groups()))


def get_stack_tops(stacks):
    return ''.join(stack[-1] for stack in stacks[1:])


def part1(stacks, instructions):
    for i, stack1, stack2 in instructions:
        for _ in range(i):
            n = stacks[stack1].pop()
            stacks[stack2].append(n)
    return get_stack_tops(stacks)


def main():
    s = get_input(d)
    stacks = setup_stacks(STACKS)
    instructions = list(get_instructions(s))
    p1 = part1(stacks, instructions)

    print('Part 1:', p1)


def test():
    stacks = setup_stacks(TEST_STACKS)
    instructions =  get_instructions(TEST)
    a = part1(stacks, instructions)
    print(a)


if __name__ == '__main__':
    # test()
    main()
