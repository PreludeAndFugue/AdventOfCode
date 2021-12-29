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


def part1(program):
    interface = RobotInterface('0')
    computer = IntcodeComputer(program, interface)
    computer.run()
    return len(interface.map)


def main():
    program = list(map(int, open(BASE + 'day11.txt', 'r').read().strip().split(',')))

    p1 = part1(program)
    print(f'Part 1: {p1}')


if __name__ == '__main__':
    main()
