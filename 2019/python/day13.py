#!python3

from computer import IntcodeComputer
from helpers import BASE


class GameInterface(object):
    def __init__(self, buffer):
        self.instruction = 0
        self.pointer = 0
        self.buffer = buffer
        self.block_count = 0

    def readline(self):
        s = self.buffer[self.pointer]
        self.pointer += 1
        return s

    def write(self, s):
        if self.instruction % 3 == 2:
            if s == '2':
                self.block_count += 1
        self.buffer.append(str(s))
        self.instruction += 1


def part1(program):
    game = GameInterface([])
    computer = IntcodeComputer(program, game)
    computer.run()
    return game.block_count


def main():
    program = list(map(int, open(BASE + 'day13.txt', 'r').read().strip().split(',')))

    p1 = part1(program)
    print(f'Part 1: {p1}')


if __name__ == '__main__':
    main()
