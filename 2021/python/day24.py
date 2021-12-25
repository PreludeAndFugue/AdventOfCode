#!python3

from itertools import product

from helpers import BASE
from day24helpers import ALU


def test():
    y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    for x in product(y, repeat=14):
        yield x


def make_input_numbers(n):
    s = str(n)
    ns = (int(x) for x in s)
    return ns


def run(input_numbers):
    x, y, z = 0, 0, 0

    w_1 = next(input_numbers)
    # print('w', w)

    x = 1
    # z = w_1 + 2

    # print('x', x, ', y', y, ', z', z)

    w_2 = next(input_numbers)
    # print('w', w)

    # x = z % 26 + 10
    # x = 1 if x != w else 0
    # y = 25 * x + 1
    # y = 26
    # z = 26 * (w_1 + 2)
    # y = (w + 4) * x
    # y = w + 4
    # z = z + y
    # z = 26 * (w_1 + 2) + w_2 + 4

    # print('x', x, ', y', y, ', z', z)

    w_3 = next(input_numbers)

    # x = z % 26 + 14
    # x = 1 if x != w_3 else 0
    # y = 26
    # z = 26 * (26 * (w_1 + 2) + w_2 + 4)
    # y = w_3 + 8
    # z = 26 * (26 * (w_1 + 2) + w_2 + 4) + w_3 + 8

    w_4 = next(input_numbers)

    # x = z % 26 + 11
    # x = 1 if x != w_4 else 0
    # y = 25 * x + 1
    # z = 26 * (26 * (26 * (w_1 + 2) + w_2 + 4) + w_3 + 8)
    # y = w_4 + 7
    # z = 26 * (26 * (26 * (w_1 + 2) + w_2 + 4) + w_3 + 8) + w_4 + 7

    w_5 = next(input_numbers)

    # x = z % 26 + 14
    # x = 1 if x != w_5 else 0
    # y = 25 * x + 1
    # z = 26 * (26 * (26 * (26 * (w_1 + 2) + w_2 + 4) + w_3 + 8) + w_4 + 7)
    # y = w_5 + 12
    # z = 26 * (26 * (26 * (26 * (w_1 + 2) + w_2 + 4) + w_3 + 8) + w_4 + 7) + w_5 + 12

    w_6 = next(input_numbers)

    # x = z % 26 - 14
    # x = w_5 - 2
    # z = z // 26
    z = 26 * (26 * (26 * (w_1 + 2) + w_2 + 4) + w_3 + 8) + w_4 + 7
    x = 1 if (w_5 - 2) != w_6 else 0
    if x == 1:
        # y = 25 * x + 1
        # z = 26 * z
        # y = w_6 + 7
        z = 26 * z + w_6 + 7

    w_7 = next(input_numbers)

    x = z % 26
    z = z // 26
    x = 1 if x != w_7 else 0
    if x == 1:
        # y = 25 * x + 1
        # z = 26 * z
        # y = w_7 + 10
        z = 26 * z + w_7 + 10

    w_8 = next(input_numbers)

    # x = z % 26 + 10
    # x = 1 if x != w_8 else 0
    # y = 25 * x + 1
    # x = 1
    # z = 26 * z
    # y = (w_8 + 14) * x
    # z = 26 * z + w_8 + 14

    w_9 = next(input_numbers)

    # x = z % 26 - 10
    # x = w_8 + 4
    # z = z // 26
    x = 1 if (w_8 + 4) != w_9 else 0
    if x == 1:
        # y = 25 * x + 1
        # z = 26 * z
        # y = w_9 + 2
        z = 26 * z + w_9 + 2

    w_10 = next(input_numbers)

    # x = z % 26 + 13
    # x = 1 if x != w else 0
    # x = 1
    # y = 25 * x + 1
    # z = 26 * z
    # y = (w_10 + 6) * x
    # z = 26 * z + w_10 + 6

    w_11 = next(input_numbers)

    # x = z % 26 - 12
    # x = w_10 - 6
    # x = w_10 - 6
    # z = z // 26
    x = 1 if (w_10 - 6) != w_11 else 0
    if x == 1:
        # y = 25 * x + 1
        # z = 26 * z
        # y = w_11 + 8
        z = 26 * z + w_11 + 8

    w_12 = next(input_numbers)

    x = z % 26 - 3
    z = z // 26
    x = 1 if x != w_12 else 0
    if x == 1:
        # y = 25 * x + 1
        # z = 26 * z
        # y = (w_12 + 11) * x
        z = 26 * z + w_12 + 11

    w_13 = next(input_numbers)

    x = z % 26 - 11
    z = z // 26
    x = 1 if x != w_13 else 0
    if x == 1:
        # y = 25 * x + 1
        # z = 26 * z
        # y = w_13 + 5
        z = 26 * z + w_13 + 5

    w_14 = next(input_numbers)

    x = z % 26 - 2
    z = z // 26
    x = 1 if x != w_14 else 0
    if x == 1:
        # y = 26
        # z = 26 * z
        # y = w_14 + 11
        z = 26 * z + w_14 + 11
    # y = 25 * x + 1
    # z = y * z
    # y = (w_14 + 11) * x
    # z = z + y

    return z


def main():
    program = open(BASE + 'day24.txt', 'r').read().strip()

    numbers = [
        13579246899999, 11111111111111, 22222222222222,
        99999999999999,

        12345678912345,
    ]
    for n in numbers:
        input_numbers = make_input_numbers(n)
        z = run(input_numbers)
        print(z)

        input_numbers = make_input_numbers(n)
        c = ALU(program, input_numbers)
        c.run()
        print(c.memory)

        assert z == c.memory['z']


if __name__ == '__main__':
    main()
