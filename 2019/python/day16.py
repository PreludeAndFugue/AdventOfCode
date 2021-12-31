#!python3

from itertools import chain, cycle, repeat

from helpers import BASE

TEST01 = '''12345678'''

TEST02 = '''80871224585914546619083218645595'''

TEST03 = '''19617804207202209144916044189917'''

TEST04 = '''69317163492948606335995924319873'''


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


def part1(digits):
    for _ in range(100):
        digits = fft(digits)
    return ''.join(str(n) for n in digits[:8])



def test1():
    t2 = parse(TEST02)
    assert part1(t2) == '24176176'

    t3 = parse(TEST03)
    assert part1(t3) == '73745418'

    t4 = parse(TEST04)
    assert part1(t4) == '52432133'


def main():
    test1()

    digits = parse(open(BASE + 'day16.txt', 'r').read())
    p1 = part1(digits)
    print(f'Part 1: {p1}')


if __name__ == '__main__':
    main()
