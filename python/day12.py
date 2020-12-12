#!python 3


INPUT = 'day12.txt'
TEST_INPUT = '''F10
N3
F7
R90
F11
'''

DIRECTIONS = 'NESW'
DIRECTION_NUMBERS = {
    'N': complex(0, 1),
    'E': complex(1, 0),
    'S': complex(0, -1),
    'W': complex(-1, 0)
}


def get_input(input):
    for line in input.strip().split('\n'):
        action, distance = line[0], line[1:]
        distance = int(distance)
        yield action, distance


def rotate(facing, number, direction):
    assert number in (90, 180, 270)
    if number == 180:
        direction = -1
    power = number // 90
    power_j = 1j ** power
    x = -direction * power_j * facing
    return x


def test_rotate():
    assert rotate(DIRECTION_NUMBERS['N'], 90, 1) == DIRECTION_NUMBERS['E']
    assert rotate(DIRECTION_NUMBERS['E'], 90, 1) == DIRECTION_NUMBERS['S']
    assert rotate(DIRECTION_NUMBERS['S'], 90, 1) == DIRECTION_NUMBERS['W']
    assert rotate(DIRECTION_NUMBERS['W'], 90, 1) == DIRECTION_NUMBERS['N']

    assert rotate(DIRECTION_NUMBERS['N'], 180, 1) == DIRECTION_NUMBERS['S']
    assert rotate(DIRECTION_NUMBERS['E'], 180, 1) == DIRECTION_NUMBERS['W']
    assert rotate(DIRECTION_NUMBERS['S'], 180, 1) == DIRECTION_NUMBERS['N']
    assert rotate(DIRECTION_NUMBERS['W'], 180, 1) == DIRECTION_NUMBERS['E']

    assert rotate(DIRECTION_NUMBERS['N'], 270, 1) == DIRECTION_NUMBERS['W']
    assert rotate(DIRECTION_NUMBERS['E'], 270, 1) == DIRECTION_NUMBERS['N']
    assert rotate(DIRECTION_NUMBERS['S'], 270, 1) == DIRECTION_NUMBERS['E']
    assert rotate(DIRECTION_NUMBERS['W'], 270, 1) == DIRECTION_NUMBERS['S']

    assert rotate(DIRECTION_NUMBERS['N'], 90, -1) == DIRECTION_NUMBERS['W']
    assert rotate(DIRECTION_NUMBERS['E'], 90, -1) == DIRECTION_NUMBERS['N']
    assert rotate(DIRECTION_NUMBERS['S'], 90, -1) == DIRECTION_NUMBERS['E']
    assert rotate(DIRECTION_NUMBERS['W'], 90, -1) == DIRECTION_NUMBERS['S']

    assert rotate(DIRECTION_NUMBERS['N'], 180, -1) == DIRECTION_NUMBERS['S']
    assert rotate(DIRECTION_NUMBERS['E'], 180, -1) == DIRECTION_NUMBERS['W']
    assert rotate(DIRECTION_NUMBERS['S'], 180, -1) == DIRECTION_NUMBERS['N']
    assert rotate(DIRECTION_NUMBERS['W'], 180, -1) == DIRECTION_NUMBERS['E']

    assert rotate(DIRECTION_NUMBERS['N'], 270, -1) == DIRECTION_NUMBERS['E']
    assert rotate(DIRECTION_NUMBERS['E'], 270, -1) == DIRECTION_NUMBERS['S']
    assert rotate(DIRECTION_NUMBERS['S'], 270, -1) == DIRECTION_NUMBERS['W']
    assert rotate(DIRECTION_NUMBERS['W'], 270, -1) == DIRECTION_NUMBERS['N']


def _part1(instructions):
    position = complex(0, 0)
    facing = complex(1, 0)
    for action, number in instructions:
        if action == 'F':
            position += number * facing
        elif action == 'R':
            facing = rotate(facing, number, 1)
        elif action == 'L':
            facing = rotate(facing, number, -1)
        elif action in DIRECTIONS:
            d = DIRECTION_NUMBERS[action]
            position += number * d
        else:
            raise IOError
    return abs(position.real) + abs(position.imag)


def test1(instructions):
    return _part1(instructions)


def part1(instructions):
    return _part1(instructions)


def _part2(instructions):
    position = complex(0, 0)
    waypoint = complex(10, 1)
    for action, number in instructions:
        if action in DIRECTIONS:
            d = DIRECTION_NUMBERS[action]
            waypoint += number * d
        elif action == 'F':
            position += number * waypoint
        elif action == 'R':
            waypoint = rotate(waypoint, number, 1)
        elif action == 'L':
            waypoint = rotate(waypoint, number, -1)
        else:
            raise IOError
    return abs(position.real) + abs(position.imag)


def test2(instructions):
    return _part2(instructions)


def part2(instructions):
    return _part2(instructions)


def main():
    instructions = list(get_input(open(INPUT, 'r').read()))
    test_instructions = list(get_input(TEST_INPUT))

    test_rotate()
    assert test1(test_instructions) == 25

    p = part1(instructions)
    print(p)

    assert test2(test_instructions) == 286

    p = part2(instructions)
    print(p)


if __name__ == "__main__":
    main()
