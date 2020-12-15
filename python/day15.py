#!python3


from collections import defaultdict

INPUT = '1,2,16,19,18,0'

TEST_INPUT_1 = '0,3,6'

TURNS_1 = 2020
TURNS_2 = 30_000_000

def get_input(input):
    for x in input.strip().split(','):
        yield int(x)


def update_seen(seen, n, i):
    if len(seen[n]) <= 1:
        seen[n].append(i)
    else:
        seen[n] = [seen[n][-1], i]


def update_seen1(seen, n, i):
    seen[n].append(i)


def do_turn(i, numbers, seen):
    last_n = numbers[i - 1]
    if len(seen[last_n]) == 1:
        numbers[i] = 0
        update_seen(seen, 0, i)
        return 0
    else:
        i1, i2 = seen[last_n]
        # i1, i2 = seen[last_n][-2:]
        n = i2 - i1
        numbers[i] = n
        update_seen(seen, n, i)
        return n


def _part1(starting_numbers, last_turn):
    numbers = {}
    seen = defaultdict(list)
    for i, n in enumerate(starting_numbers, start=1):
        numbers[i] = n
        seen[n].append(i)
    turn = len(numbers) + 1
    while turn <= last_turn:
        n = do_turn(turn, numbers, seen)
        turn += 1
    return numbers


def test1():
    starting_numbers = list(get_input(TEST_INPUT_1))
    numbers = _part1(starting_numbers, 10)
    keys = sorted(numbers.keys())
    values = [numbers[i] for i in keys]
    assert values == [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]


def test2():
    starting_numbers = [1, 3, 2]
    numbers = _part1(starting_numbers, TURNS_1)
    assert numbers[TURNS_1] == 1

    starting_numbers = [2, 1, 3]
    numbers = _part1(starting_numbers, TURNS_1)
    assert numbers[TURNS_1] == 10

    starting_numbers = [1, 2, 3]
    numbers = _part1(starting_numbers, TURNS_1)
    assert numbers[TURNS_1] == 27

    starting_numbers = [2, 3, 1]
    numbers = _part1(starting_numbers, TURNS_1)
    assert numbers[TURNS_1] == 78

    starting_numbers = [3, 2, 1]
    numbers = _part1(starting_numbers, TURNS_1)
    assert numbers[TURNS_1] == 438

    starting_numbers = [3, 1, 2]
    numbers = _part1(starting_numbers, TURNS_1)
    assert numbers[TURNS_1] == 1836


def part1():
    starting_numbers = list(get_input(INPUT))
    numbers = _part1(starting_numbers, TURNS_1)
    return numbers[TURNS_1]


def test3():
    starting_numbers = [1, 2, 3]
    numbers = _part1(starting_numbers, TURNS_2)
    assert numbers[TURNS_2] == 261_214

    starting_numbers = [3, 2, 1]
    numbers = _part1(starting_numbers, TURNS_2)
    assert numbers[TURNS_2] == 18

    starting_numbers = [2, 3, 1]
    numbers = _part1(starting_numbers, TURNS_2)
    assert numbers[TURNS_2] == 6_895_259


def part2():
    starting_numbers = list(get_input(INPUT))
    numbers = _part1(starting_numbers, TURNS_2)
    return numbers[TURNS_2]


def main():
    test1()
    test2()

    p = part1()
    print(p)

    # test3()

    p = part2()
    print(p)


if __name__ == "__main__":
    main()
