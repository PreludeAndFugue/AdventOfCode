#!python3

from os import rename
from computer import read_program, IntcodeComputer, Console
from helpers import BASE


def make_map(buffer):
    map_ = {}
    for r, line in enumerate(''.join(chr(int(x)) for x in buffer).strip().split('\n')):
        for c, ch in enumerate(line):
            map_[r, c] = ch
    return map_


def get_neighbours(location, map_):
    r, c = location
    return [
        map_.get((r + 1, c), '.'),
        map_.get((r - 1, c), '.'),
        map_.get((r, c + 1), '.'),
        map_.get((r, c - 1), '.'),
    ]


def get_neighbours2(location, direction, map_):
    r, c = location
    dR, dC = direction
    # forward
    r_new, c_new = r + dR, c + dC
    if map_.get((r_new, c_new), '.') == '#':
        return (r_new, c_new), direction, 'S'
    # right
    dr, dc = -dC, dR
    r_new, c_new = r + dr, c + dc
    if map_.get((r_new, c_new), '.') == '#':
        return (r_new, c_new), (dr, dc), 'L'
    # left
    dr, dc = dC, -dR
    r_new, c_new = r + dr, c + dc
    if map_.get((r_new, c_new), '.') == '#':
        return (r_new, c_new), (dr, dc), 'R'

    return None, None, None


def make_path(map_):
    start = [k for k, v in map_.items() if v == '^'][0]
    location = start
    direction = -1, 0
    path = []
    while True:
        new_location, new_direction, D = get_neighbours2(location, direction, map_)
        if new_location is None:
            break
        if new_direction != direction:
            path.append(D)
            path.append(1)
        else:
            d = path.pop()
            path.append(d + 1)
        location = new_location
        direction = new_direction
    return path


def part1(program):
    console = Console([])
    computer = IntcodeComputer(program, console)
    computer.run()
    map_ = make_map(console.buffer)
    intersections = []
    for location in map_.keys():
        if all(n == '#' for n in get_neighbours(location, map_)):
            intersections.append(location)
    return sum(l[0] * l[1] for l in intersections), console.buffer, map_


def part2(buffer, map_):
    m = ''.join(chr(int(c)) for c in buffer)
    print(m)
    path = make_path(map_)
    print(path)


def main():
    program = read_program(BASE + 'day17.txt')

    p1, buffer, map_ = part1(program)
    print(f'Part 1: {p1}')

    p2 = part2(buffer, map_)


if __name__ == '__main__':
    main()
