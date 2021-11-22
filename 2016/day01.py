#!python3

TEST01 = 'R2, L3'
TEST02 = 'R2, R2, R2'
TEST03 = 'R5, L5, R5, R3'
TEST04 = 'R8, R4, R4, R8'

SOURCE = 'day01.txt'

WEST = -1, 0
EAST = 1, 0
NORTH = 0, 1
SOUTH = 0, -1

TURN_L = 'L'
TURN_R = 'R'

def make_instructions(string):
    for item in string.strip().split(', '):
        direction = item[0]
        distance = int(item[1:])
        yield direction, distance


def update_direction(direction, turn):
    if direction == WEST:
        return SOUTH if turn == 'L' else NORTH
    elif direction == NORTH:
        return WEST if turn == TURN_L else EAST
    elif direction == EAST:
        return NORTH if turn == TURN_L else SOUTH
    else:
        return EAST if turn == TURN_L else WEST


def update_location(location, direction, turn, distance):
    x, y = location
    direction = update_direction(direction, turn)
    w, z = direction
    x += distance * w
    y += distance * z
    return (x, y), direction


def run1(instructions):
    location = 0, 0
    direction = NORTH
    for turn, distance in instructions:
        location, direction = update_location(location, direction, turn, distance)
    x, y = location
    return abs(x) + abs(y)


def run2(instructions):
    location = 0, 0
    locations = set([location])
    direction = NORTH
    for turn, distance in instructions:
        direction = update_direction(direction, turn)
        for _ in range(1, distance + 1):
            location = location[0] + direction[0], location[1] + direction[1]
            if location in locations:
                x, y = location
                return abs(x) + abs(y)
            else:
                locations.add(location)
    return 0



def main1():
    instructions = make_instructions(open(SOURCE, 'r').read())
    distance = run1(instructions)
    print(distance)


def main2():
    instructions = make_instructions(open(SOURCE, 'r').read())
    distance = run2(instructions)
    print(distance)


def test1():
    i1 = make_instructions(TEST01)
    d1 = run1(i1)
    assert d1 == 5

    i2 = make_instructions(TEST02)
    d2 = run1(i2)
    assert d2 == 2

    i3 = make_instructions(TEST03)
    d3 = run1(i3)
    assert d3 == 12


def test2():
    i1 = make_instructions(TEST04)
    d1 = run2(i1)
    assert d1 == 4


if __name__ == '__main__':
    test1()
    test2()
    main1()
    main2()
