
from help import get_input

TEST1 = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

TEST2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''


NUMBERS = {
    'one': ('1', 2),
    'two': ('2', 2),
    'three': ('3', 4),
    'four': ('4', 4),
    'five': ('5', 3),
    'six': ('6', 3),
    'seven': ('7', 5),
    'eight': ('8', 4),
    'nine': ('9', 3),
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
    ns = []
    for l in s:
        cs = []
        while l:
            if l[0].isdigit():
                cs.append(l[0])
                l = l[1:]
                continue
            for a, (b, c) in NUMBERS.items():
                if l.startswith(a):
                    cs.append(b)
                    l = l[c:]
                    break
            else:
                l = l[1:]
        n = cs[0] + cs[-1]
        n = int(n)
        ns.append(n)
    return sum(ns)


def test2():
    p2 = part2(TEST2.strip().split())
    assert p2 == 281


def main():
    s = get_input('01').strip().split()
    p1 = part1(s)
    print(p1)
    test2()
    p2 = part2(s)
    print(p2)


if __name__ == '__main__':
    main()
