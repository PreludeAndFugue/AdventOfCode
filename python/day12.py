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


def rotate(facing, number, direction):
    assert number in (90, 180, 270)
    steps = number // 90
    i = DIRECTIONS.index(facing)
    new_i = (i + direction * steps) % len(DIRECTIONS)
    return DIRECTIONS[new_i]


def test_rotate():
    assert rotate('N', 90, 1) == 'E'
    assert rotate('E', 90, 1) == 'S'
    assert rotate('S', 90, 1) == 'W'
    assert rotate('W', 90, 1) == 'N'

    assert rotate('N', 180, 1) == 'S'
    assert rotate('E', 180, 1) == 'W'
    assert rotate('S', 180, 1) == 'N'
    assert rotate('W', 180, 1) == 'E'

    assert rotate('N', 270, 1) == 'W'
    assert rotate('E', 270, 1) == 'N'
    assert rotate('S', 270, 1) == 'E'
    assert rotate('W', 270, 1) == 'S'

    assert rotate('N', 90, -1) == 'W'
    assert rotate('E', 90, -1) == 'N'
    assert rotate('W', 90, -1) == 'S'
    assert rotate('S', 90, -1) == 'E'

    assert rotate('N', 180, -1) == 'S'
    assert rotate('E', 180, -1) == 'W'
    assert rotate('W', 180, -1) == 'E'
    assert rotate('S', 180, -1) == 'N'

    assert rotate('N', 270, -1) == 'E'
    assert rotate('E', 270, -1) == 'S'
    assert rotate('W', 270, -1) == 'N'
    assert rotate('S', 270, -1) == 'W'


def _part1(instructions):
    position = 0, 0
    facing = 'E'
    for action, number in instructions:
        if action == 'F':
            position = move(position, facing, number)
        elif action == 'R':
            facing = rotate(facing, number, 1)
        elif action == 'L':
            facing = rotate(facing, number, -1)
        elif action in DIRECTIONS:
            position = move(position, action, number)
        else:
            raise IOError
    return sum(map(abs, position))


def test1(instructions):
    return _part1(instructions)


def part1(instructions):
    return _part1(instructions)


def rotate_waypoint(waypoint, number, direction):
    x, y = waypoint
    if number == 90:
        return direction * y, -direction * x
    elif number == 180:
        return -x, -y
    elif number == 270:
        return -direction * y, direction * x
    else:
        raise IOError


def _part2(instructions):
    position = 0, 0
    waypoint = 10, 1
    for action, number in instructions:
        if action in DIRECTIONS:
            waypoint = move(waypoint, action, number)
        elif action == 'F':
            x, y = position
            a, b = waypoint
            position = x + number * a, y + number * b
        elif action == 'R':
            waypoint = rotate_waypoint(waypoint, number, 1)
        elif action == 'L':
            waypoint = rotate_waypoint(waypoint, number, -1)
        else:
            raise IOError
    return sum(map(abs, position))


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
