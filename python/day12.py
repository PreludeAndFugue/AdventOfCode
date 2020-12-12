#!python 3


INPUT = 'day12.txt'
TEST_INPUT = '''F10
N3
F7
R90
F11
'''

DIRECTIONS = 'NESW'


def get_input(input):
    for line in input.strip().split('\n'):
        action, distance = line[0], line[1:]
        distance = int(distance)
        yield action, distance


def move(position, facing, distance):
    if facing == 'E':
        return position[0] + distance, position[1]
    elif facing == 'S':
        return position[0], position[1] - distance
    elif facing == 'W':
        return position[0] - distance, position[1]
    elif facing == 'N':
        return position[0], position[1] + distance
    else:
        raise IOError


def rotate_right(facing, number):
    assert number in (90, 180, 270)
    steps = number // 90
    i = DIRECTIONS.index(facing)
    new_i = (i + steps) % len(DIRECTIONS)
    return DIRECTIONS[new_i]


def rotate_left(facing, number):
    assert number in (90, 180, 270)
    steps = number // 90
    i = DIRECTIONS.index(facing)
    new_i = (i - steps) % len(DIRECTIONS)
    return DIRECTIONS[new_i]


def test_rotate():
    assert rotate_right('N', 90) == 'E'
    assert rotate_right('E', 90) == 'S'
    assert rotate_right('S', 90) == 'W'
    assert rotate_right('W', 90) == 'N'

    assert rotate_right('N', 180) == 'S'
    assert rotate_right('E', 180) == 'W'
    assert rotate_right('S', 180) == 'N'
    assert rotate_right('W', 180) == 'E'

    assert rotate_right('N', 270) == 'W'
    assert rotate_right('E', 270) == 'N'
    assert rotate_right('S', 270) == 'E'
    assert rotate_right('W', 270) == 'S'

    assert rotate_left('N', 90) == 'W'
    assert rotate_left('E', 90) == 'N'
    assert rotate_left('W', 90) == 'S'
    assert rotate_left('S', 90) == 'E'

    assert rotate_left('N', 180) == 'S'
    assert rotate_left('E', 180) == 'W'
    assert rotate_left('W', 180) == 'E'
    assert rotate_left('S', 180) == 'N'

    assert rotate_left('N', 270) == 'E'
    assert rotate_left('E', 270) == 'S'
    assert rotate_left('W', 270) == 'N'
    assert rotate_left('S', 270) == 'W'


def _part1(instructions):
    position = 0, 0
    facing = 'E'
    for action, number in instructions:
        if action == 'F':
            position = move(position, facing, number)
        elif action == 'R':
            facing = rotate_right(facing, number)
        elif action == 'L':
            facing = rotate_left(facing, number)
        elif action in DIRECTIONS:
            position = move(position, action, number)
        else:
            raise IOError
    return sum(map(abs, position))


def test1():
    instructions = get_input(TEST_INPUT)
    return _part1(instructions)


def part1():
    instructions = get_input(open(INPUT, 'r').read())
    return _part1(instructions)


def main():
    test_rotate()
    assert test1() == 25

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
