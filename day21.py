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


def rotate_based_on(a):
    def f(password):
        i = password.index(a)
        total = 1 + i + (1 if i >= 4 else 0)
        rr = rotate_right(total)
        return rr(password)
    return f


def reverse_positions(m, n):
    def f(password):
        # print(m, n)
        # x = password[:m]
        # y = password[m:n + 1:][::-1]
        # z = password[n + 1:]
        # print(repr(x), repr(y), repr(z))
        return password[:m] + password[m:n + 1][::-1] + password[n + 1:]
    return f


def move_position(m, n):
    def f(password):
        a = password[m]
        password = password[:m] + password[m + 1:]
        password = password[:n] + a + password[n:]
        return password
    return f


def make_instructions(input):
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
            yield rotate_left(n)
        elif line.startswith('rotate right'):
            _, _, n, _ = line.strip().split(' ')
            n = int(n)
            yield rotate_right(n)
        elif line.startswith('rotate based on'):
            _, _, _, _, _, _, a = line.strip().split(' ')
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
    print(password)


def main():
    test1()
    part1()


if __name__ == '__main__':
    main()
