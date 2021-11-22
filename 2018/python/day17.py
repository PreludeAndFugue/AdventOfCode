#!python3

import re

INPUT = 'day17.txt'

TEST_INPUT = '''x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
'''


pattern = r'(\w)=(\d+), \w=(\d+)..(\d+)'
regex = re.compile(pattern)


def read_scan(scan):
    for line in scan.strip().split('\n'):
        m = regex.match(line)
        first_coord = m.group(1)
        first_value = int(m.group(2))
        range_start = int(m.group(3))
        range_end = int(m.group(4))
        r = range(range_start, range_end + 1)
        if first_coord == 'x':
            yield first_value, r
        else:
            yield r, first_value


def draw_scan(scan):
    scan = list(scan)
    xs = []
    ys = []
    for x, y in scan:
        if isinstance(x, int):
            xs.append(x)
            ys.append(y.start)
            ys.append(y.stop)
        else:
            xs.append(x.start)
            xs.append(x.stop)
            ys.append(y)
    print(xs)
    print(ys)


def test1():
    scan = read_scan(TEST_INPUT)
    draw_scan(scan)


def main():
    test1()


if __name__ == "__main__":
    main()
