
from help import get_input

TEST1 = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''

NOOP = 'noop'
ADDX = 'addx'

def parse(s):
    for line in s.split('\n'):
        parts = line.split(' ')
        instruction = parts[0]
        if instruction == 'noop':
            yield instruction, None
        elif instruction == 'addx':
            x = int(parts[1])
            yield instruction, x
        else:
            raise ValueError


def check_signal_strength(cycle, x):
    cases = set((20, 60, 100, 140, 180, 220))
    if cycle in cases:
        return cycle * x
    else:
        return 0


def run(instructions):
    pointer = 0
    cycle = 1
    x = 1
    for instruction, value in instructions:
        if instruction == NOOP:
            yield check_signal_strength(cycle, x)
            pointer += 1
            cycle += 1

        elif instruction == ADDX:
            yield check_signal_strength(cycle, x)
            pointer += 1
            cycle += 1

            yield check_signal_strength(cycle, x)
            x += value
            pointer += 1
            cycle += 1
        else:
            raise ValueError


def main():
    s = get_input('10')
    instructions = parse(s)
    # instructions = parse(TEST1)
    p1 = sum(x for x in run(instructions))

    print('Part 1:', p1)


if __name__ == '__main__':
    main()
