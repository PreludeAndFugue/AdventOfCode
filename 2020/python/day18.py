#!python3

from day18helpers import Lexer, Interpreter


INPUT = 'day18.txt'

TEST_INPUT = '''1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
'''
TEST_OUTPUT = [71, 51, 26, 437, 12240, 13632]

TEST_INPUT_1 = '''6 * ((4 * 3) * 6 * (5 * 5 * 6 + 6) + (3 * 2) * 5 * 3)
'''
TEST_OUTPUT_1 = [1011420]
# 1010970

TEST_OUTPUT_PART_2 = [231, 51, 46, 1445, 669060, 23340]


def get_input(input):
    for line in input.strip().split('\n'):
        yield line


def test1():
    for answer, line in zip(TEST_OUTPUT, get_input(TEST_INPUT)):
        lexer = Lexer(line)
        i = Interpreter(lexer)
        assert i.expr() == answer


def test2():
    for answer, line in zip(TEST_OUTPUT_1, get_input(TEST_INPUT_1)):
        lexer = Lexer(line)
        i = Interpreter(lexer)
        assert i.expr() == answer


def part1():
    total = 0
    for line in get_input(open(INPUT, 'r').read()):
        lexer = Lexer(line)
        i = Interpreter(lexer)
        total += i.expr()
    return total


def test3():
    for answer, line in zip(TEST_OUTPUT_PART_2, get_input(TEST_INPUT)):
        lexer = Lexer(line)
        i = Interpreter(lexer)
        assert i.expr() == answer


def main():
    # test1()
    # test2()

    test3()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
