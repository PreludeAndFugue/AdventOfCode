#!python3

INPUT = 'day21.txt'

PASSWORD = 'abcdefgh'
TEST_PASSWORD = 'abcde'

TEST_INSTRUCTIONS = '''swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
'''

TEST_OUTPUT = [
    'ebcda', 'edcba', 'abcde', 'bcdea', 'bdeac', 'abdec', 'ecabd', 'decab'
]


def swap_position(m, n):
    def f(password):
        c_m = password[m]
        c_n = password[n]
        t = str.maketrans(c_m + c_n, c_n + c_m)
        return password.translate(t)
    return f


def swap_letter(a, b):
    def f(password):
        t = str.maketrans(a + b, b + a)
        return password.translate(t)
    return f


def rotate_left(n):
    def f(password):
        i = n % len(password)
        return password[i:] + password[:i]
    return f


def rotate_right(n):
    def f(password):
        i = n % len(password)
        return password[-i:] + password[:-i]
    return f


ROTATE_BASED_ON_MAP = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 6,
    5: 7,
    6: 8,
    7: 9
}
def rotate_based_on(a):
    def f(password):
        i = password.index(a)
        total = ROTATE_BASED_ON_MAP[i]
        rr = rotate_right(total)
        return rr(password)
    return f


ROTATE_BASED_ON_REVERSE_MAP = {
    1: 1,
    3: 2,
    5: 3,
    7: 4,
    2: 6,
    4: 7,
    6: 8,
    0: 9
}
def rotate_based_on_reversed(a):
    def f(password):
        i = password.index(a)
        total = ROTATE_BASED_ON_REVERSE_MAP[i]
        ll = rotate_left(total)
        return ll(password)
    return f


def reverse_positions(m, n):
    def f(password):
        return password[:m] + password[m:n + 1][::-1] + password[n + 1:]
    return f


def move_position(m, n):
    def f(password):
        a = password[m]
        password = password[:m] + password[m + 1:]
        password = password[:n] + a + password[n:]
        return password
    return f


def make_instructions(input, reverse=False):
    for line in input.strip().split('\n'):
        if line.startswith('swap position'):
            _, _, m, _, _, n = line.strip().split(' ')
            m = int(m)
            n = int(n)
            yield swap_position(m, n)
        elif line.startswith('swap letter'):
            _, _, a, _, _, b = line.strip().split(' ')
            yield swap_letter(a, b)
        elif line.startswith('rotate left'):
            _, _, n, _ = line.strip().split(' ')
            n = int(n)
            if reverse:
                yield rotate_right(n)
            else:
                yield rotate_left(n)
        elif line.startswith('rotate right'):
            _, _, n, _ = line.strip().split(' ')
            n = int(n)
            if reverse:
                yield rotate_left(n)
            else:
                yield rotate_right(n)
        elif line.startswith('rotate based on'):
            _, _, _, _, _, _, a = line.strip().split(' ')
            if reverse:
                yield rotate_based_on_reversed(a)
            else:
                yield rotate_based_on(a)
        elif line.startswith('reverse positions'):
            _, _, m, _, n = line.strip().split(' ')
            m = int(m)
            n = int(n)
            yield reverse_positions(m, n)
        elif line.startswith('move position'):
            _, _, m, _, _, n = line.strip().split(' ')
            m = int(m)
            n = int(n)
            if reverse:
                yield move_position(n, m)
            else:
                yield move_position(m, n)
        else:
            raise IOError


def test1():
    password = TEST_PASSWORD
    instructions = make_instructions(TEST_INSTRUCTIONS)
    for i, r in zip(instructions, TEST_OUTPUT):
        password = i(password)
        assert password == r


def part1():
    password = PASSWORD
    instructions = make_instructions(open(INPUT, 'r').read())
    for i in instructions:
        password = i(password)
    print(1, password)


def test2():
    password = 'hcdefbag'
    instructions = list(make_instructions(open(INPUT, 'r').read(), reverse=True))[::-1]
    for i in instructions:
        password = i(password)
    print(password, 'abcdefgh')


def test2a():
    password = 'decab'
    instructions = list(make_instructions(TEST_INSTRUCTIONS, reverse=True))[::-1]
    for i in instructions:
        password = i(password)
    assert password == 'abcde'


def part2():
    password = 'fbgdceah'
    instructions = list(make_instructions(open(INPUT, 'r').read(), reverse=True))[::-1]
    for i in instructions:
        password = i(password)
    print(2, password)


def test_inverses():
    print('test inverses')
    password = 'abcdefgh'

    i = swap_position(5, 7)
    password1 = i(i(password))
    assert password == password1

    i = swap_position(3, 3)
    password1 = i(i(password))
    assert password == password1

    i = swap_letter('b', 'd')
    password1 = i(i(password))
    assert password == password1

    i = swap_letter('c', 'c')
    password1 = i(i(password))
    assert password == password1

    i = rotate_left(4)
    j = rotate_right(4)
    password1 = i(j(password))
    password2 = j(i(password))
    assert password == password1
    assert password == password2

    i = rotate_left(0)
    j = rotate_right(0)
    password1 = i(j(password))
    password2 = j(i(password))
    assert password == password1
    assert password == password2

    i = reverse_positions(3, 6)
    password1 = i(i(password))
    assert password == password1

    i = reverse_positions(4, 4)
    password1 = i(i(password))
    assert password == password1

    i = move_position(5, 1)
    j = move_position(1, 5)
    password1 = j(i(password))
    assert password == password1

    i = move_position(3, 3)
    j = move_position(3, 3)
    password1 = i(j(password))
    assert password == password1

    i = rotate_based_on('a')
    j = rotate_based_on_reversed('a')
    password1 = j(i(password))
    assert password == password1, f'{password}, {password1}'


def main():
    test1()
    part1()
    test_inverses()
    test2a()
    test2()
    part2()


if __name__ == '__main__':
    main()
