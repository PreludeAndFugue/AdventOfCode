
from itertools import islice
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
        if instruction == NOOP:
            yield instruction, None
        elif instruction == ADDX:
            x = int(parts[1])
            yield instruction, x
        else:
            raise ValueError


def check_signal_strength(cycle, x):
    return cycle * x if cycle in set((20, 60, 100, 140, 180, 220)) else 0


def draw(cycle, x):
    return '█' if x - 1 <= (cycle - 1) % 40 <= x + 1 else ' '


def run(instructions):
    def work(x, picture):
        nonlocal cycle
        nonlocal signal_strength
        signal_strength += check_signal_strength(cycle, x)
        picture.append(draw(cycle, x))
        if cycle % 40 == 0:
            picture.append('\n')
        cycle += 1

    cycle = 1
    x = 1
    picture = []
    signal_strength = 0
    for instruction, value in instructions:
        if instruction == NOOP:
            work(x, picture)

        elif instruction == ADDX:
            for _ in range(2):
                work(x, picture)
            x += value

        else:
            raise ValueError

    return signal_strength, ''.join(picture)


def main():
    s = get_input('10')
    instructions = parse(s)
    # instructions = parse(TEST1)
    p1, p2 = run(instructions)

    print('Part 1:', p1)
    print(p2)


if __name__ == '__main__':
    main()
