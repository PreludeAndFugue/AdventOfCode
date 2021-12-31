#!python3

from computer import IntcodeComputer, read_program
from helpers import BASE

NORTH = '1'
SOUTH = '2'
WEST = '3'
EAST = '4'
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

def turn_left(direction):
    i = (DIRECTIONS.index(direction) - 1) % len(DIRECTIONS)
    return DIRECTIONS[i]


def turn_right(direction):
    i = (DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)
    return DIRECTIONS[i]


WALL = '0'
MOVED = '1'
MOVED_OXYGEN = '2'

MOVE = {
    NORTH: (0, 1),
    SOUTH: (0, -1),
    WEST: (-1, 0),
    EAST: (1, 0),
}

OFFSETS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

START = 0, 0


class RepairDroid(object):
    def __init__(self):
        self.locations = set([START])
        self.walls = set()
        self.location = START
        self.direction = NORTH
        self.oxygen = None
        self.start_count = 0
        self.done = False


    def readline(self):
        if self.done:
            return None
        return self.direction


    def write(self, s):
        if s == WALL:
            self.direction = turn_left(self.direction)
        elif s == MOVED:
            self._move()
        elif s == MOVED_OXYGEN:
            self._move()
            self.oxygen = self.location

        if self.location == START:
            self.start_count += 1
            if self.start_count > 4:
                self.done = True


    def _move(self):
        x, y = self.location
        dx, dy = MOVE[self.direction]
        self.location = x + dx, y + dy
        self.locations.add(self.location)
        self.direction = turn_right(self.direction)


def print_map(map_, on):
    xs = [l[0] for l in map_]
    x_min = min(xs)
    x_max = max(xs)
    ys = [l[1] for l in map_]
    y_min = min(ys)
    y_max = max(ys)
    rows = []
    for y in range(y_min, y_max + 1):
        row = []
        for x in range(x_min, x_max + 1):
            if (x, y) == START:
                row.append('X')
            elif (x, y) in on:
                row.append('O')
            elif (x, y) in map_:
                row.append('.')
            else:
                row.append(' ')
        rows.append(''.join(row))
    m = '\n'.join(rows)
    print(m)


def get_neighbours(location, map_):
    x, y = location
    for dx, dy in OFFSETS:
        new_location = x + dx, y + dy
        if new_location in map_:
            yield new_location


def bfs(map_, start, goal):
    oxygen_d = 0
    max_d = 0
    seen = set()
    to_check = [(start, 0)]
    while to_check:
        location, d = to_check.pop(0)
        if location == goal:
            oxygen_d = d
        if location not in seen:
            seen.add(location)
            max_d = max(max_d, d)
            for neighbour in get_neighbours(location, map_):
                to_check.append((neighbour, d + 1))
    return oxygen_d, max_d


def test():
    assert turn_right(NORTH) == EAST
    assert turn_right(SOUTH) == WEST
    assert turn_right(EAST) == SOUTH
    assert turn_right(WEST) == NORTH

    assert turn_left(NORTH) == WEST
    assert turn_left(SOUTH) == EAST
    assert turn_left(EAST) == NORTH
    assert turn_left(WEST) == SOUTH


def main():
    test()

    program = read_program(BASE + 'day15.txt')
    repair = RepairDroid()
    computer = IntcodeComputer(program, repair)
    try:
        computer.run()
    except AttributeError:
        map_ = repair.locations
        oxygen = repair.oxygen

    p1, _ = bfs(map_, START, oxygen)
    print(f'Part 1: {p1}')

    _, p2 = bfs(map_, oxygen, None)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
