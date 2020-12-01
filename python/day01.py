#!python3

from functools import reduce
from itertools import combinations


INPUT = 'python/day01.txt'


def check(numbers, n):
    for m in combinations(numbers, n):
        if sum(m) == 2020:
            return reduce(lambda x, y: x * y, m)


def part1(numbers):
    return check(numbers, 2)


def part2(numbers):
    return check(numbers, 3)


def main():
    numbers = [int(line.strip()) for line in open(INPUT, 'r').readlines()]
    p = part1(numbers)
    print(p)

    p = part2(numbers)
    print(p)


if __name__ == "__main__":
    main()
