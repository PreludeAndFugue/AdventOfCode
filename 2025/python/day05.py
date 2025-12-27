
from help import get_input

TEST01 = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

source = TEST01.strip()
source = get_input(5)


def make(source):
    a, b = source.split('\n\n')
    ranges = []
    for line in a.split('\n'):
        x, y = line.strip().split('-')
        ranges.append(range(int(x), int(y)+1))
    fresh = []
    for line in b.split('\n'):
        n = int(line.strip())
        fresh.append(n)
    return ranges, fresh


def part1():
    ranges, fresh = make(source)
    t = 0
    for f in fresh:
        for r in ranges:
            if f in r:
                t += 1
                break
    return t


def merge_ranges(r1: range, r2: range) -> list[range]:
    if r2.start <= r1.stop:
        r = range(r1.start, max(r1.stop, r2.stop))
        return [r]
    else:
        return [r1, r2]


def part2():
    ranges, _ = make(source)
    ranges.sort(key=lambda r: r.start)
    i = 0
    while True:
        try:
            r1 = ranges[i]
            r2 = ranges[i + 1]
        except IndexError:
            break
        result = merge_ranges(r1, r2)
        if len(result) == 1:
            ranges[i:i + 2] = result
        else:
            i += 1
    return sum(len(r) for r in ranges)


if __name__ == '__main__':
    p1 = part1()
    print(p1)
    p2 = part2()
    print(p2)
