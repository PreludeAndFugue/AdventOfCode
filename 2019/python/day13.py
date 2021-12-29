#!python3

from computer import IntcodeComputer
from helpers import BASE


class GameInterface(object):
    def __init__(self, buffer):
        self.instruction = 0
        self.pointer = 0
        self.buffer = buffer
        self.block_count = 0
        self.x = 0
        self.y = 0
        self.ball_position = 0, 0
        self.paddle_position = 0, 0
        self.score = 0

    def readline(self):
        ball_x = self.ball_position[0]
        paddle_x = self.paddle_position[0]
        if ball_x < paddle_x:
            return '-1'
        elif ball_x == paddle_x:
            return '0'
        else:
            return '1'

    def write(self, s):
        s = int(s)
        i = self.instruction % 3
        self.instruction += 1
        if i == 0:
            self.x = s
        elif i == 1:
            self.y = s
        else:
            if s == 2:
                self.block_count += 1
            if self.x == -1 and self.y == 0:
                self.score = s
            else:
                if s == 4:
                    self.ball_position = (self.x, self.y)
                elif s == 3:
                    self.paddle_position = (self.x, self.y)


def part1(program):
    game = GameInterface([])
    computer = IntcodeComputer(program, game)
    computer.run()
    return game.block_count


def part2(program):
    program[0] = 2
    game = GameInterface([])
    computer = IntcodeComputer(program, game)
    computer.run()
    return game.score


def main():
    program = list(map(int, open(BASE + 'day13.txt', 'r').read().strip().split(',')))

    p1 = part1(program)
    print(f'Part 1: {p1}')

    p2 = part2(program)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
