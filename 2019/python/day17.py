#!python3

from os import getpriority, rename
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


def z_algorithm(s):
    '''Competitive programmer's handbook'''
    x = 0
    y = 0
    n = len(s)
    z = [0] * n
    for i in range(n):
        z[i] = max(0, min(z[i - x], y - i + 1))
        while (i+z[i] < n and s[z[i]] == s[i + z[i]]):
            x = i
            y = i + z[i]
            z[i] = z[i] + 1
    z[0] = 0
    return z


def get_prefix(path, replacement):
    z_array = z_algorithm(path)
    z_max = max(z_array)
    z_array[0] = z_max
    a = path[0:z_max]
    z_indices = [i for i, n in enumerate(z_array) if n == z_max]
    for z_index in reversed(z_indices):
        path[z_index:z_index + z_max] = replacement
    path.pop(0)
    path = [f'{r}{i}' if r == replacement else r for i, r in enumerate(path)]
    return a, path


def make_path_parts(path, a, b, c):
    path_parts = []
    while path:
        if path[:2] == a[:2]:
            path_parts.append('A')
            path = path[len(a):]
        elif path[:2] == b[:2]:
            path_parts.append('B')
            path = path[len(b):]
        elif path[:2] == c[:2]:
            path_parts.append('C')
            path = path[len(c):]
        else:
            ValueError
    return path_parts


def make_ascii_input(path_parts, a, b, c):
    result = []
    for part in (path_parts, a, b, c):
        x = ','.join(str(x) for x in part)
        for p in x:
            result.append(ord(p))
        result.append(ord('\n'))

    result.append(ord('n'))
    result.append(ord('\n'))

    result = [str(x) for x in result]
    return result


def part1(program):
    console = Console([])
    computer = IntcodeComputer(program, console)
    computer.run()
    map_ = make_map(console.buffer)
    intersections = []
    for location in map_.keys():
        if all(n == '#' for n in get_neighbours(location, map_)):
            intersections.append(location)
    return sum(l[0] * l[1] for l in intersections), map_


def part2(map_, program):
    original_path = make_path(map_)
    path = original_path.copy()
    a, path = get_prefix(path, 'A')
    b, path = get_prefix(path, 'B')
    path.pop(0)
    c, path = get_prefix(path, 'C')
    path_parts = make_path_parts(original_path, a, b, c)
    ascii = make_ascii_input(path_parts, a, b, c)

    program[0] = 2
    console = Console(ascii)
    computer = IntcodeComputer(program, console)
    computer.run()
    return console.buffer[-1]



def main():
    program = read_program(BASE + 'day17.txt')

    p1, map_ = part1(program)
    print(f'Part 1: {p1}')

    p2 = part2(map_, program)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
