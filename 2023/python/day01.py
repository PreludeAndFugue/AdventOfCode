
from help import get_input

NUMBERS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def part1(s):
    ns = []
    for l in s:
        cs = [c for c in l if c.isdigit()]
        n = cs[0] + cs[-1]
        n = int(n)
        ns.append(n)
    return sum(ns)


def part2(s):
    pass


def main():
    s = get_input('01').strip().split()
    p1 = part1(s)
    print(p1)
    p2 = part2(s)
    print(p2)


if __name__ == '__main__':
    main()
