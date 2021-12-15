#!python3

from helpers import BASE


def fuel_required(mass):
    return mass // 3 - 2


def fuel_required_2(mass):
    f = fuel_required(mass)
    total_f = 0
    while f > 0:
        total_f += f
        f = fuel_required(f)
    return total_f


def main():
    assert fuel_required(12) == 2
    assert fuel_required(14) == 2
    assert fuel_required(1969) == 654
    assert fuel_required(100756) == 33583

    masses = list(map(int, open(BASE + 'day01.txt').read().strip().split('\n')))

    p1 = sum(fuel_required(m) for m in masses)
    print(f'Part 1: {p1}')

    assert fuel_required_2(12) == 2
    assert fuel_required_2(14) == 2
    assert fuel_required_2(1969) == 966
    assert fuel_required_2(100756) == 50346

    p2 = sum(fuel_required_2(m) for m in masses)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
