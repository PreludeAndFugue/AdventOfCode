
import re

from help import get_input

'''
Part 1
------
172062: too high

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
        return new_location, map_[new_location]
    else:
        # print('new location not in map', direction)
        if direction == U:
            ny = max(c[1] for c in map_ if c[0] == x)
        elif direction == D:
            ny = min(c[1] for c in map_ if c[0] == x)
        elif direction == L:
            nx = max(c[0] for c in map_ if c[1] == y)
        elif direction == R:
            nx = min(c[0] for c in map_ if c[1] == y)
            # print('jump --', nx)
        else:
            raise ValueError(location, direction)

        new_location = nx, ny
        if new_location in map_:
            return new_location, map_[new_location]
    raise ValueError(location, direction)


def get_neighbour_2(location, direction, map_):
    return location, direction


def get_initial_location(map_):
    ymin = min(y for _, y in map_)
    locations = [c for c in map_ if c[1] == ymin]
    return sorted(locations)[0]


def part(location, direction, instructions, neighbour_function, map_):
    d = direction
    for i in instructions:
        if isinstance(i, int):
            for _ in range(i):
                # print('move', d)
                new_location, value = neighbour_function(location, d, map_)
                if value == '#':
                    # print('blocked')
                    continue
                else:
                    location = new_location

                # print(location, d)
        else:
            # print('new direction', d)
            # d = get_new_direction(d, i)
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

    print('Part 1:', p1)


if __name__ == '__main__':
    main()