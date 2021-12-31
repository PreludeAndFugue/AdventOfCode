#!python3

from computer import read_program, IntcodeComputer, Console
from helpers import BASE


def make_map(buffer):
    map_ = {}
    for r, line in enumerate(''.join(chr(int(c)) for c in buffer).strip().split('\n')):
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


def part1(program):
    console = Console([])
    computer = IntcodeComputer(program, console)
    computer.run()
    map_ = make_map(console.buffer)
    intersections = []
    for location in map_.keys():
        if all(n == '#' for n in get_neighbours(location, map_)):
            intersections.append(location)
    return sum(l[0] * l[1] for l in intersections)


def main():
    program = read_program(BASE + 'day17.txt')

    p1 = part1(program)
    print(f'Part 1: {p1}')



if __name__ == '__main__':
    main()
