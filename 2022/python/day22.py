
import re

from help import get_input

'''
Part 1
------
172062: too high

Part 2
------
101330: too low
'''

TEST = '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5'''


regex = re.compile('\d+|R|L')

U = 0, -1
D = 0, 1
L = -1, 0
R = 1, 0

CHANGE_DIRECTION = {
    'L': {U: L, L: D, D: R, R: U},
    'R': {U: R, R: D, D: L, L: U}
}

FACING = {R: 0, D: 1, L: 2, U: 3}


def parse(s):
    s1, s2 = s.split('\n\n')
    map_ = {}
    for y, line in enumerate(s1.split('\n'), start=1):
        for x, ch in enumerate(line, start=1):
            if ch == ' ':
                continue
            elif ch == '.' or ch =='#':
                map_[(x, y)] = ch
            else:
                raise ValueError(repr(ch))
    instructions = []
    for f in regex.findall(s2.strip()):
        if f == 'R' or f == 'L':
            instructions.append(f)
        else:
            instructions.append(int(f))
    return map_, instructions


def get_neighbour(location, direction, map_):
    x, y = location
    dx, dy = direction
    nx, ny = x + dx, y + dy
    new_location = nx, ny
    if new_location in map_:
        return new_location, direction, map_[new_location]
    else:
        if direction == U:
            ny = max(c[1] for c in map_ if c[0] == x)
        elif direction == D:
            ny = min(c[1] for c in map_ if c[0] == x)
        elif direction == L:
            nx = max(c[0] for c in map_ if c[1] == y)
        elif direction == R:
            nx = min(c[0] for c in map_ if c[1] == y)
        else:
            raise ValueError(location, direction)

        new_location = nx, ny
        if new_location in map_:
            return new_location, direction, map_[new_location]
    raise ValueError(location, direction)


def get_neighbour_2(location, direction, map_):
    '''
    Use Rubik's cube colours

                    W       W
                    ^       ^
                -----------------
            O < |   B   |   R   | > G
                -----------------
                |   Y   |
        -----------------
    B < |   O   |   G   | > R
        -----------------
    B < |   W   |
        ---------
            v
            R

    Blue
    ----
    B -> W
    direction: U ->

    Red
    ---
    R -> W
    directions: U ->

    R -> Y
    direction: D -> L
    coords:

    R -> G
    direction: R ->

    Yellow
    ------
    Y -> O
    direction: L -> D

    Y -> R
    direction: R -> U
    '''
    x, y = location
    dx, dy = direction
    nx, ny = x + dx, y + dy
    new_location = nx, ny
    if new_location in map_:
        return new_location, direction, map_[new_location]
    else:
        if direction == U:
            if 1 <= x <= 50:
                # O -> Y
                new_direction = R
                nx = 51
                ny = x + 50
            elif 51 <= x <= 100:
                # B -> W
                new_direction = R
                nx = 1
                ny = x + 100
            elif 101 <= x <= 150:
                # R -> W
                new_direction = direction
                nx = x - 100
                ny = 200
            else:
                raise ValueError(location, direction)
        elif direction == D:
            if 1 <= x <= 50:
                # W -> R
                new_direction = direction
                nx = x + 100
                ny = 1
            elif 51 <= x <= 100:
                # G -> W
                new_direction = L
                nx = 50
                ny = x + 100
            elif 101 <= x <= 150:
                # R -> Y
                new_direction = L
                nx = 100
                ny = x - 50
            else:
                raise ValueError(location, direction)
        elif direction == L:
            if 1 <= y <= 50:
                # B -> O
                new_direction = R
                nx = 1
                ny = 151 - y
            elif 51 <= y <= 100:
                # Y -> 0
                new_direction = D
                nx = y - 50
                ny = 101
            elif 101 <= y <= 150:
                # O -> B
                new_direction = R
                nx = 51
                ny = 151 - y
            elif 151 <= y <= 200:
                # W -> B
                new_direction = D
                nx = y - 100
                ny = 1
            else:
                raise ValueError(location, direction)
        elif direction == R:
            if 1 <= y <= 50:
                # R -> G
                new_direction = L
                nx = 100
                ny = 151 - y
            elif 51 <= y <= 100:
                # Y -> R
                new_direction = U
                nx = y + 50
                ny = 50
            elif 101 <= y <= 150:
                # G -> R
                new_direction = L
                nx = 150
                ny = 151 - y
            elif 151 <= y <= 200:
                # W -> G
                new_direction = U
                nx = y - 100
                ny = 150
            else:
                raise ValueError(location, direction)

        new_location = nx, ny
        if new_location in map_:
            return new_location, new_direction, map_[new_location]

        raise ValueError(location, direction)


def get_initial_location(map_):
    ymin = min(y for _, y in map_)
    locations = [c for c in map_ if c[1] == ymin]
    return sorted(locations)[0]


def part(location, direction, instructions, neighbour_function, map_):
    d = direction
    for i in instructions:
        if isinstance(i, int):
            for _ in range(i):
                new_location, new_direction, value = neighbour_function(location, d, map_)
                if value == '#':
                    continue
                else:
                    location = new_location
                    d = new_direction
        else:
            d = CHANGE_DIRECTION[i][d]

    f = FACING[d]
    x, y = location
    password = 1000*y + 4*x + f
    return password


def main():
    s = open('../day22.txt', 'r').read()
    # s = TEST
    map_, instructions = parse(s)

    d = R
    location = get_initial_location(map_)

    p1 = part(location, d, instructions, get_neighbour, map_)
    p2 = part(location, d, instructions, get_neighbour_2, map_)

    print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()