
import re

from help import get_input


TEST1 = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''


regex = re.compile('Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)')


def parse(s):
    for line in s.split('\n'):
        m = regex.match(line)
        assert m is not None
        s = int(m[1]), int(m[2])
        b = int(m[3]), int(m[4])
        yield s, b


def draw(data, extra):
    items = {}
    xs = set()
    ys = set()
    for x in extra:
        items[x] = '#'
        xs.add(x[0])
        ys.add(x[1])
    for s, b in data:
        items[s] = 'S'
        items[b] = 'B'
        xs.add(s[0])
        xs.add(b[0])
        ys.add(s[1])
        ys.add(b[1])
    x_min = min(xs)
    x_max = max(xs)
    y_min = min(ys)
    y_max = max(ys)
    rows = []
    for y in range(y_min, y_max + 1):
        row = []
        for x in range(x_min, x_max + 1):
            v = items.get((x, y), '.')
            row.append(v)
        rows.append(''.join(row))
    map_ = '\n'.join(rows)
    print(map_)


def manhattan(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) + abs(y2 - y1)


def part1(data, y):
    locations = set()
    for s, b in data:
        sx, sy = s
        # bx, by = b
        d = manhattan(s, b)
        if sy - d <= y <= sy + d:
            dx = d - abs(sy - y)
            for x in range(-dx, dx + 1):
                l = sx + x, y
                locations.add(l)
    for s, b in data:
        if s in locations:
            locations.remove(s)
        if b in locations:
            locations.remove(b)
    return len(locations)


def main():
    s = get_input('15')
    # s = TEST1.strip()
    data = list(parse(s))

    # p1 = part1(data, 10)
    p1 = part1(data, 2000000)

    print('Part 1:', p1)


if __name__ == '__main__':
    main()
