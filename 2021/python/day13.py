#!python3

from helpers import BASE

TEST01 = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''


def parse(string):
    dots, instructions = string.strip().split('\n\n')
    dots = [tuple(map(int, dot.split(','))) for dot in dots.split('\n')]
    instructions = [i.split('=') for i in instructions.split('\n')]
    instructions = [(i[0][-1], int(i[1])) for i in instructions]
    return instructions, dots


def fold_dot(instruction, dot):
    axis, n = instruction
    x, y = dot
    if axis == 'x':
        if x > n:
            return x - 2*(x - n), y
        else:
            return dot
    else:
        if y > n:
            return x, y - 2*(y - n)
        else:
            return dot


def fold_dots(instruction, dots):
    return list(set(fold_dot(instruction, dot) for dot in dots)) 


def part1(instructions, dots):
    i = instructions[0]
    dots = fold_dots(i, dots)
    return len(dots)


def part2(instructions, dots):
    for i in instructions:
        dots = fold_dots(i, dots)
    max_x = max(dot[0] for dot in dots)
    max_y = max(dot[1] for dot in dots)
    unique_dots = set(dots)
    pattern = []
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            dot = x, y
            if dot in unique_dots:
                row.append('#')
            else:
                row.append('.')
        pattern.append(''.join(row))
    print('\n'.join(pattern))


def main():
    test_input = parse(TEST01)
    instructions, dots = parse(open(BASE + 'day13.txt', 'r').read())

    t1 = part1(*test_input)
    assert t1 == 17

    p1 = part1(instructions, dots)
    print(f'Part 1: {p1}')

    part2(*test_input)
    part2(instructions, dots)


if __name__ == '__main__':
    main()
