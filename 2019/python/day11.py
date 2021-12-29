#!python3

from computer import IntcodeComputer
from helpers import BASE


class RobotInterface(object):
    def __init__(self, start):
        self.instruction = 0
        self.position = 0, 0
        self.direction = 0, 1
        self.map = {self.position: start}


    def readline(self):
        return self.map.get(self.position, '0')


    def write(self, s):
        if self.instruction % 2 == 0:
            self.map[self.position] = s
        else:
            if s == '0':
                # turn left
                if self.direction == (0, 1):
                    self.direction = -1, 0
                elif self.direction == (-1, 0):
                    self.direction = 0, -1
                elif self.direction == (0, -1):
                    self.direction = 1, 0
                elif self.direction == (1, 0):
                    self.direction = 0, 1
                else:
                    raise ValueError
            else:
                # turn right
                if self.direction == (0, 1):
                    self.direction = 1, 0
                elif self.direction == (1, 0):
                    self.direction = 0, -1
                elif self.direction == (0, -1):
                    self.direction = -1, 0
                elif self.direction == (-1, 0):
                    self.direction = 0, 1
                else:
                    raise ValueError
            x, y = self.position
            dx, dy = self.direction
            self.position = x + dx, y + dy
        self.instruction += 1


    def draw_map(self):
        keys = self.map.keys()
        x_min = min(k[0] for k in keys)
        x_max = max(k[0] for k in keys) + 1
        y_min = min(k[1] for k in keys)
        y_max = max(k[1] for k in keys) + 1
        rows = []
        for y in range(y_min, y_max):
            row = []
            for x in range(x_min, x_max):
                position = x, y
                paint = '#' if self.map.get(position, '0') == '1' else ' '
                row.append(paint)
            rows.append(''.join(row))
        rows = reversed(rows)
        return '\n'.join(rows)


def part1(program):
    interface = RobotInterface('0')
    computer = IntcodeComputer(program, interface)
    computer.run()
    return len(interface.map)


def part2(program):
    interface = RobotInterface('1')
    computer = IntcodeComputer(program, interface)
    computer.run()
    print(interface.draw_map())


def main():
    program = list(map(int, open(BASE + 'day11.txt', 'r').read().strip().split(',')))

    p1 = part1(program)
    print(f'Part 1: {p1}')

    part2(program)


if __name__ == '__main__':
    main()
