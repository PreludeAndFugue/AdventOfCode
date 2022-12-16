
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


class Rectangle:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max


    @property
    def width(self):
        return self.x_max - self.x_min


    @property
    def height(self):
        return self.y_max - self.y_min


    @staticmethod
    def make_from_sensor_and_beacon(s, b):
        d = rotated_manhattan(s, b)
        xmin = s[0] - d
        xmax = s[0] + d
        ymin = s[1] - d
        ymax = s[1] + d
        return Rectangle(xmin, ymin, xmax, ymax)


    def subtract(self, other):
        '''Subtract another rectangle from this rectangle.

        Returns a list of rectangles.
        '''
        intersection = self._intersection(other)
        if intersection is None:
            return [self]

        return []


    def coords(self):
        for x in range(self.x_min, self.x_max + 1):
            for y in range(self.y_min, self.y_max + 1):
                yield x, y


    def _intersection(self, other):
        '''The intersection of this an another rectangle

        Returns a rectangle or None.
        '''
        if self.x_max < other.x_min:
            return None
        if self.x_min > other.x_max:
            return None
        if self.y_max < other.y_min:
            return None
        if self.y_min > other.y_max:
            return None

        return None


    def __repr__(self) -> str:
        return f'R({self.x_min}, {self.y_min}, {self.x_max}, {self.y_max})'


def parse(s):
    for line in s.split('\n'):
        m = regex.match(line)
        assert m is not None
        s = int(m[1]), int(m[2])
        b = int(m[3]), int(m[4])
        yield s, b


def rotate_coordinate(c):
    x, y = c
    return x + y, y - x


def unrotate_coordinate(c):
    x, y = c
    # assert (x - y) % 2 == 0, c
    # assert (x + y) % 2 == 0, c
    if (x - y) % 2 != 0:
        return None
    if (x + y) % 2 != 0:
        return None
    return (x - y)//2, (x + y)//2


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


def rotated_manhattan(a, b):
    x1, y1 = a
    x2, y2 = b
    return max(abs(x2 - x1), abs(y2 - y1))


def tuning_freq(b):
    x, y = b
    return 4000000 * x + y


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


def part2(data):
    xs = []
    ys = []
    for s, b in data:
        xs.append(s[0])
        xs.append(b[0])
        ys.append(s[1])
        ys.append(b[1])
    xmin = min(xs)
    ymin = min(ys)
    xmax = max(xs)
    ymax = max(ys)
    everything = [Rectangle(xmin, ymin, xmax, ymax)]
    print(everything)
    to_remove = [Rectangle.make_from_sensor_and_beacon(s, b) for s, b in data]
    for r in to_remove:
        print(r, r.width, r.height)
        # print(list(r.coords()))


def main():
    # s = get_input('15')
    s = TEST1.strip()
    data = list(parse(s))
    rotated_data = [(rotate_coordinate(s), rotate_coordinate(b)) for s, b in data]

    # p1 = part1(data, 10)
    p1 = part1(data, 2000000)
    p2 = part2(rotated_data)

    print('Part1:', p1)
    # print('Part 2', p2)

    for s, b in rotated_data:
        print(s, b, rotated_manhattan(s, b))


if __name__ == '__main__':
    main()
