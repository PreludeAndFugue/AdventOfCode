
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


def part1():
    a, b = source.split('\n\n')
    ranges = []
    for line in a.split('\n'):
        x, y = line.strip().split('-')
        ranges.append(range(int(x), int(y)+1))
    fresh = []
    for line in b.split('\n'):
        n = int(line.strip())
        fresh.append(n)

    # print(ranges)
    # print(fresh)

    t = 0
    for f in fresh:
        for r in ranges:
            if f in r:
                t += 1
                break
    return t



if __name__ == '__main__':
    p1 = part1()
    print(p1)
