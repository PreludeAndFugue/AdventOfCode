#!python3

from collections import defaultdict

from numbertheory.nt import divisors

INPUT = 36_000_000
INPUT_1 = INPUT / 10


def part1():
    for i in range(1, 1_000_000):
        n = sum(i for i in divisors(i))
        if n >= INPUT_1:
            print(i)
            return


def part2():
    results = defaultdict(int)
    for i in range(1, 3_300_000):
        for j in range(i, 51 * i, i):
        # l = list(r)
        # print(l)
        # assert len(l) == 50
        # for j in r:
            results[j] += 11 * i

    for i in range(1, 3_300_000):
        if i in results:
            r = results[i]
            if r >= INPUT:
                print(i, r)
                return


def main():
    # part1()
    part2()



if __name__ == '__main__':
    main()
