#!python3

'''
Part 2
------
Base input number has 650 digits. Repeated 10,000 times: 6,500,000 digit input number
for part 2.

Offset position: 5,972,877

The digits before the offset position of the number (first seven digits of number) do
not contribute to the fft update of the number at the offset position. The pattern
digits are all zero before the offset position.

5,972,876 zeros, 5,972,876 ones

So the digit at the offset position is the units digit of the sum of the remaining digits.
'''

from itertools import chain, cycle, repeat

from helpers import BASE

TEST01 = '''12345678'''

TEST02 = '''80871224585914546619083218645595'''

TEST03 = '''19617804207202209144916044189917'''

TEST04 = '''69317163492948606335995924319873'''

TEST05 = '''03036732577212944063491565474664'''

TEST06 = '''02935109699940807407585447034323'''

TEST07 = '''03081770884921959731165446850517'''


def parse(string):
    return list(int(x) for x in string.strip())


def pattern(i):
    base = (0, 1, 0, -1)
    repeats = [repeat(n, i) for n in base]
    c = chain(*repeats)
    y = cycle(c)
    next(y)
    while True:
        yield next(y)


def fft(digits):
    new_digits = []
    for i, _ in enumerate(digits, start=1):
        p = pattern(i)
        m = abs(sum(next(p) * n for n in digits)) % 10
        new_digits.append(m)
    return new_digits


def fft2(digits):
    s = sum(digits)
    new_digits = [s % 10]
    for i in digits[:-1]:
        s -= i
        m = s % 10
        new_digits.append(m)
    return new_digits


def make_offset(digits):
    offset = digits[:7]
    n = 0
    for d in offset:
        n *= 10
        n += d
    return n


def expand(digits, offset):
    result = []
    for _ in range(10_000):
        result += digits
    return result[offset:]


def part1(digits):
    for _ in range(100):
        digits = fft(digits)
    return ''.join(str(n) for n in digits[:8])


def part2(digits):
    offset = make_offset(digits)
    digits = expand(digits, offset)
    for _ in range(100):
        digits = fft2(digits)
    return ''.join(str(d) for d in digits[:8])


def test1():
    t2 = parse(TEST02)
    assert part1(t2) == '24176176'

    t3 = parse(TEST03)
    assert part1(t3) == '73745418'

    t4 = parse(TEST04)
    assert part1(t4) == '52432133'


def test2():
    t5 = parse(TEST05)
    assert part2(t5) == '84462026'

    t6 = parse(TEST06)
    assert part2(t6) == '78725270'

    t7 = parse(TEST07)
    assert part2(t7) == '53553731'


def main():
    test1()

    digits = parse(open(BASE + 'day16.txt', 'r').read())
    p1 = part1(digits)
    print(f'Part 1: {p1}')

    test2()

    p2 = part2(digits)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
