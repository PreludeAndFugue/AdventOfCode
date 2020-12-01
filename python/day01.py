#!python3

from itertools import combinations
from math import prod


INPUT = 'python/day01.txt'


def check(numbers, n):
    for m in combinations(numbers, n):
        if sum(m) == 2020:
            return prod(m)


def part1(numbers):
    return check(numbers, 2)


def part2(numbers):
    return check(numbers, 3)


def main():
    numbers = list(map(int, open(INPUT, 'r').readlines()))
    p = part1(numbers)
    print(p)

    p = part2(numbers)
    print(p)


if __name__ == "__main__":
    main()
