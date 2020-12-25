#!python3

INPUT = 'day25.txt'
TEST_INPUT = '''5764801
17807724
'''


N = 20_201_227
SUBJECT_NUMBER = 7


def get_input(input):
    return tuple(map(int, input.strip().split('\n')))


def transform(subject_number, loop):
    value = 1
    for _ in range(loop):
        value = value * subject_number
        value = value % N
    return value


def find_loop_size(n):
    value = 1
    loop_size = 0
    while True:
        value = value * SUBJECT_NUMBER
        value = value % N
        loop_size += 1
        if value == n:
            return loop_size


def test1():
    p1, p2 = get_input(TEST_INPUT)
    l1 = find_loop_size(p1)
    l2 = find_loop_size(p2)
    z1 = transform(p1, l2)
    z2 = transform(p2, l1)
    assert z1 == 14897079
    assert z2 == 14897079


def part1():
    p1, p2 = get_input(open(INPUT, 'r').read())
    l1 = find_loop_size(p1)
    l2 = find_loop_size(p2)
    z1 = transform(p1, l2)
    z2 = transform(p2, l1)
    assert z1 == z2
    return z1


def main():
    test1()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
