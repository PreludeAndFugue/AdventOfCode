#!python3

from itertools import chain

from helpers import BASE

TEST01 = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''


class Board(object):
    def __init__(self, numbers):
        self.numbers = numbers
        self.called = []


    def call(self, n):
        self.called.append(n)


    def has_won(self):
        for row in self.numbers:
            if all(n in self.called for n in row):
                return True
        for column in zip(*self.numbers):
            if all(n in self.called for n in column):
                return True
        return False


    def score(self):
        s = sum(n for n in chain(*self.numbers) if n not in self.called)
        last_called = self.called[-1]
        return s * last_called


def parse(text):
    text = text.strip()
    lines = text.split('\n')
    lines = iter(lines)
    numbers = next(lines)
    numbers = [int(n) for n in numbers.split(',')]
    boards = []
    board = []
    while True:
        line = next(lines, None)

        if line == '':
            if board:
                boards.append(Board(board))
            board = []

        elif line is None:
            boards.append(Board(board))
            break

        else:
            line_numbers = [int(x) for x in line.strip().split()]
            board.append(line_numbers)

    return numbers, boards


def part1(numbers, boards):
    for n in numbers:
        for board in boards:
            board.call(n)
            if board.has_won():
                return board.score()


def part2(numbers, boards):
    board_count = len(boards)
    boards_won = set()
    for n in numbers:
        for i, board in enumerate(boards):
            board.call(n)
            if board.has_won():
                boards_won.add(i)
                if len(boards_won) == board_count:
                    return board.score()


def main():
    test_n, test_boards = parse(TEST01)
    n, boards = parse(open(BASE + 'day04.txt', 'r').read())

    t1 = part1(test_n, test_boards)
    assert t1 == 4512

    p1 = part1(n, boards)
    print(f'Part 1: {p1}')

    t2 = part2(test_n, test_boards)
    assert t2 == 1924

    p2 = part2(n, boards)
    print(f'Part 2: {p2}')

if __name__ == '__main__':
    main()
