#!python3

from helpers import BASE
from day24helpers import ALU


def make_input_numbers(n):
    s = str(n)
    ns = (int(x) for x in s)
    return ns


def run(input_numbers):
    '''
    The early x tests all set x equal to one. Want the later x tests to set x to zero so
    that we can keep dividing z by 26 to get it to zero. This provides the following
    constraints on the fourteen input numbers.

    w_6 = w_5 - 2
    w_4 = w_7 - 7
    w_8 = w_9 - 4
    w_11 = w_10 - 6
    w_3 = w_12 - 5
    w_13 = w_2 - 7
    w_1 = w_14

    # Largest

    w_1 = 9
    w_2 = 9
    w_3 = 4
    w_4 = 2
    w_5 = 9
    w_6 = 7
    w_7 = 9
    w_8 = 5
    w_9 = 9
    w_10 = 9
    w_11 = 3
    w_12 = 9
    w_13 = 2
    w_14 = 9

    z = 99429795993929

    # Smallest

    w_1 = 1
    w_2 = 8
    w_3 = 1
    w_4 = 1
    w_5 = 3
    w_6 = 1
    w_7 = 8
    w_8 = 1
    w_9 = 5
    w_10 = 7
    w_11 = 1
    w_12 = 6
    w_13 = 1
    w_14 = 1

    z = 18113181571611

    '''
    x, y, z = 0, 0, 0
    x = 1

    w_6 = 7
    w_8 = 5

    # print(input_numbers)
    w_1, w_2, w_3, w_4, w_5, w_7, w_9, w_10, w_11, w_12, w_13, w_14 = input_numbers
    ws = (w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8, w_9, w_10, w_11, w_12, w_13, w_14)
    # print(w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8, w_9, w_10, w_11, w_12, w_13, w_14)

    z = 26 * (26 * (26 * (w_1 + 2) + w_2 + 4) + w_3 + 8) + w_4 + 7
    # x = 1 if (w_5 - 2) != w_6 else 0

    if (w_5 - 2) != w_6:
        return 10_000, 1

    if (w_4 + 7) != w_7:
        return 10_000, 1

    if (w_8 + 4) != w_9:
        return 10_000, 1

    if (w_10 - 6) != w_11:
        return 10_000, 1

    if (w_3 + 5) != w_12:
        return 10_000, 1

    if (w_2 - 7) != w_13:
        return 10_000, 1

    if w_1 != w_14:
        return 10_000, 1


    # if (w_5 - 2) != w_6:

        # raise ValueError

        # if (w_6 + 7) != w_7:
        #     z = 26 * z + w_7 + 10

        # if (w_8 + 4) != w_9:
        #     z = 26 * z + w_9 + 2

        # if (w_10 - 6) != w_11:
        #     z = 26 * z + w_11 + 8

        # x = z % 26 - 3
        # z = z // 26
        # if x != w_12:
        #     z = 26 * z + w_12 + 11

        # x = z % 26 - 11
        # z = z // 26
        # if x != w_13:
        #     z = 26 * z + w_13 + 5

        # x = z % 26 - 2
        # z = z // 26
        # if x != w_14:
        #     z = 26 * z + w_14 + 11
    # else:
    z = 26 * (26 * (w_1 + 2) + w_2 + 4) + w_3 + 8
    # if (w_4 + 7) != w_7:
    #     z = 26 * z + w_7 + 10

    # if (w_8 + 4) != w_9:
    #     z = 26 * z + w_9 + 2

    # x = 1 if (w_10 - 6) != w_11 else 0
    # if x == 1:
    #     z = 26 * z + w_11 + 8

    # x = z % 26 - 3
    # x = w_3 + 5
    # z = z // 26
    z = 26 * (w_1 + 2) + w_2 + 4
    # if (w_3 + 5) != w_12:
    #     z = 26 * z + w_12 + 11

    # x = z % 26 - 11
    # x = (w_2 + 4) - 11
    # z = z // 26
    z = (w_1 + 2)
    # if (w_2 - 7) != w_13:
    #     z = 26 * z + w_13 + 5

    # x = z % 26 - 2
    # x = (w_1 + 2) - 2
    # x = w_1
    z = z // 26
    # if w_1 != w_14:
    #     z = 26 * z + w_14 + 11

    return z, ws


def main():
    program = open(BASE + 'day24.txt', 'r').read().strip()

    numbers = [
        # largest
        99429795993929,
        # smallest
        18113181571611,
    ]
    for n in numbers:
        input_numbers = make_input_numbers(n)
        c = ALU(program, input_numbers)
        c.run()
        assert c.memory['z'] == 0

    print('Part 1: 99429795993929')
    print('Part 2: 18113181571611')


if __name__ == '__main__':
    main()
