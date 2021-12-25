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
    x = 1

    w_1 = next(input_numbers)
    w_2 = next(input_numbers)
    w_3 = next(input_numbers)
    w_4 = next(input_numbers)
    w_5 = next(input_numbers)
    w_6 = next(input_numbers)
    w_7 = next(input_numbers)
    w_8 = next(input_numbers)
    w_9 = next(input_numbers)
    w_10 = next(input_numbers)
    w_11 = next(input_numbers)
    w_12 = next(input_numbers)
    w_13 = next(input_numbers)
    w_14 = next(input_numbers)

    z = 26 * (26 * (26 * (w_1 + 2) + w_2 + 4) + w_3 + 8) + w_4 + 7
    x = 1 if (w_5 - 2) != w_6 else 0
    if x == 1:
        # z = 26 * z + w_6 + 7

        x = w_6 + 7
        # z = z // 26
        x = 1 if (w_6 + 7) != w_7 else 0
        if x == 1:
            z = 26 * z + w_7 + 10

        x = 1 if (w_8 + 4) != w_9 else 0
        if x == 1:
            z = 26 * z + w_9 + 2

        x = 1 if (w_10 - 6) != w_11 else 0
        if x == 1:
            z = 26 * z + w_11 + 8

        x = z % 26 - 3
        z = z // 26
        x = 1 if x != w_12 else 0
        if x == 1:
            z = 26 * z + w_12 + 11

        x = z % 26 - 11
        z = z // 26
        x = 1 if x != w_13 else 0
        if x == 1:
            z = 26 * z + w_13 + 5

        x = z % 26 - 2
        z = z // 26
        x = 1 if x != w_14 else 0
        if x == 1:
            z = 26 * z + w_14 + 11
    else:
        x = w_4 + 7
        z = 26 * (26 * (w_1 + 2) + w_2 + 4) + w_3 + 8
        x = 1 if x != w_7 else 0
        if x == 1:
            z = 26 * z + w_7 + 10

        x = 1 if (w_8 + 4) != w_9 else 0
        if x == 1:
            z = 26 * z + w_9 + 2

        x = 1 if (w_10 - 6) != w_11 else 0
        if x == 1:
            z = 26 * z + w_11 + 8

        x = z % 26 - 3
        z = z // 26
        x = 1 if x != w_12 else 0
        if x == 1:
            z = 26 * z + w_12 + 11

        x = z % 26 - 11
        z = z // 26
        x = 1 if x != w_13 else 0
        if x == 1:
            z = 26 * z + w_13 + 5

        x = z % 26 - 2
        z = z // 26
        x = 1 if x != w_14 else 0
        if x == 1:
            z = 26 * z + w_14 + 11







    # x = z % 26
    # z = z // 26
    # x = 1 if x != w_7 else 0
    # if x == 1:
    #     z = 26 * z + w_7 + 10

    # x = 1 if (w_8 + 4) != w_9 else 0
    # if x == 1:
    #     z = 26 * z + w_9 + 2

    # x = 1 if (w_10 - 6) != w_11 else 0
    # if x == 1:
    #     z = 26 * z + w_11 + 8

    # x = z % 26 - 3
    # z = z // 26
    # x = 1 if x != w_12 else 0
    # if x == 1:
    #     z = 26 * z + w_12 + 11

    # x = z % 26 - 11
    # z = z // 26
    # x = 1 if x != w_13 else 0
    # if x == 1:
    #     z = 26 * z + w_13 + 5

    # x = z % 26 - 2
    # z = z // 26
    # x = 1 if x != w_14 else 0
    # if x == 1:
    #     z = 26 * z + w_14 + 11

    return z


def part1():
    current_min = 1_000_000_000_000_000_000
    for numbers in product([9, 8, 7, 6, 5, 4, 3, 2, 1], repeat=14):
        # print(numbers)
        z = run(iter(numbers))
        if z < current_min:
            current_min = z
            print(numbers)
            print(z)
        # print(z)


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

    part1()


if __name__ == '__main__':
    main()
