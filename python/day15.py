#!python3


from collections import defaultdict

INPUT = '1,2,16,19,18,0'

TEST_INPUT_1 = '0,3,6'


def get_input(input):
    for x in input.strip().split(','):
        yield int(x)


def do_turn(i, numbers, seen):
    last_n = numbers[i - 1]
    if len(seen[last_n]) == 1:
        numbers[i] = 0
        seen[0].append(i)
        return 0
    else:
        i1, i2 = seen[last_n][-2:]
        n = i2 - i1
        numbers[i] = n
        seen[n].append(i)
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
    numbers = _part1(starting_numbers, 2020)
    assert numbers[2020] == 1

    starting_numbers = [2, 1, 3]
    numbers = _part1(starting_numbers, 2020)
    assert numbers[2020] == 10

    starting_numbers = [1, 2, 3]
    numbers = _part1(starting_numbers, 2020)
    assert numbers[2020] == 27

    starting_numbers = [2, 3, 1]
    numbers = _part1(starting_numbers, 2020)
    assert numbers[2020] == 78

    starting_numbers = [3, 2, 1]
    numbers = _part1(starting_numbers, 2020)
    assert numbers[2020] == 438

    starting_numbers = [3, 1, 2]
    numbers = _part1(starting_numbers, 2020)
    assert numbers[2020] == 1836


def part1():
    starting_numbers = list(get_input(INPUT))
    numbers = _part1(starting_numbers, 2020)
    return numbers[2020]


def main():
    test1()
    test2()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
