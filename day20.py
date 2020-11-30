#!python3


INPUT = 'day20.txt'


def make_ranges(input):
    lines = open(input, 'r').read().strip().split('\n')
    ranges = []
    for line in lines:
        x, y = line.split('-', 1)
        x, y = int(x), int(y)
        assert x < y
        r = range(x, y + 1)
        ranges.append(r)
    return ranges


def not_in_ranges(n, ranges):
    for r in ranges:
        if n in r:
            return False, r.stop
    return True, None


def part1():
    ranges = make_ranges(INPUT)
    i = 0
    while True:
        result, n = not_in_ranges(i, ranges)
        if result:
            return i
        else:
            i = n


def main():
    p = part1()
    print(p)



if __name__ == '__main__':
    main()
