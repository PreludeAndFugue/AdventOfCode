
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


def compress_coordinates(data):
    values = set()
    for s, b in data:
        values.add(s[0])
        values.add(s[1])
        values.add(b[0])
        values.add(b[1])
    values = sorted(values)
    decompress = {i: v for i, v in enumerate(values)}
    compress = {v: i for i, v in decompress.items()}
    return compress, decompress


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


def make_extra(c, d):
    '''Make all points within manhattan distance d of c.'''
    x, y = c
    results = []
    for xi in range(x - d, x + d + 1):
        for yi in range(y - d, y + d + 1):
            ci = xi, yi
            if manhattan(c, ci) <= d:
                results.append(ci)
    return results


def make_rotated_extra(c, d):
    x, y = c
    results = []
    for xi in range(x - d, x + d + 1):
        for yi in range(y - d, y + d + 1):
            results.append((xi, yi))
    return results


def part2(data):
    hash_locations = set()
    for s, b in data:
        d = rotated_manhattan(s, b)
        for x in range(s[0] - d, s[0] + d + 1):
            for y in range(s[1] - d, s[1] + d + 1):
                hash_locations.add((x, y))
    draw(data, [])
    draw(data, hash_locations)

    # unrotate
    unrotated_hash_locations = [unrotate_coordinate(l) for l in hash_locations]
    unrotated_hash_locations = [l for l in unrotated_hash_locations if l is not None]
    # unrotated_data = [(unrotate_coordinate(s), unrotate_coordinate(b)) for s, b in data]

    print(data)
    # print(unrotated_data)
    # draw(unrotated_data, unrotated_hash_locations)



def main():
    # s = get_input('15')
    s = TEST1.strip()
    data = list(parse(s))
    extra = make_extra((8, 7), 9)

    # draw(data, extra)
    # print()

    # draw(data, [])
    # compress, decompress = compress_coordinates(data)

    rotated_data = [(rotate_coordinate(s), rotate_coordinate(b)) for s, b in data]
    rotate_compress, _ = compress_coordinates(rotated_data)

    # compressed_data = [((compress[s[0]], compress[s[1]]), (compress[b[0]], compress[b[1]])) for s, b in data]
    compressed_rotated_data = [((rotate_compress[s[0]], rotate_compress[s[1]]), (rotate_compress[b[0]], rotate_compress[b[1]])) for s, b in rotated_data]
    # rotated_extra = [rotate_coordinate(x) for x in extra]
    # rotated_coord = rotate_coordinate((8, 7))
    # rotated_extra = make_rotated_extra(rotated_coord, 9)
    # draw(rotated_data, rotated_extra)

    # print(data)
    # print(rotated_data)
    for a, b in zip(rotated_data, compressed_rotated_data):
        print(a)
        print(b)
        print()

    # p1 = part1(data, 10)
    # p1 = part1(data, 2000000)
    p2 = part2(compressed_rotated_data)

    # print('Part1:', p1)
    # print('Part 2', p2)


if __name__ == '__main__':
    main()
