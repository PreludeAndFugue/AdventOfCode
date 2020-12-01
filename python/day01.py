#!python3


from itertools import combinations


INPUT = 'python/day01.txt'


def part1():
    numbers = (int(line.strip()) for line in open(INPUT, 'r').readlines())
    for n1, n2 in combinations(numbers, 2):
        if n1 + n2 == 2020:
            return n1 * n2


def main():
    p = part1()
    print(p)


if __name__ == "__main__":
    main()
