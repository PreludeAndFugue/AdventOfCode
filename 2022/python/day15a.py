
from help import get_input
from day15 import TEST1, parse, manhattan

'''
Find all the points that are just outside the boundary of the sensor-beacon
manhattan distance diamonds. This is where the missing beacon is. Then remove
all points that are inside the manhattan distance diamond of another
sensor-beacon pair.
'''


def draw(coords, s):
    xs = [x for x, _ in coords]
    ys = [y for _, y in coords]
    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    rows = []
    for y in range(ymin, ymax + 1):
        row = ''
        for x in range(xmin, xmax + 1):
            if (x, y) in coords:
                row += '#'
            elif (x, y) == s:
                row += 'B'
            else:
                row += '.'
        rows.append(row)
    return '\n'.join(rows)


def make_boundary(s, b):
    d = manhattan(s, b) + 1
    sx, sy = s
    for y in range(-d, d + 1):
        x = d - abs(y)
        if x == 0:
            yield sx, sy + y
        else:
            yield sx - x, sy + y
            yield sx + x, sy + y


def filter_boundary(sensor, boundary, all_sensors, mmax):
    test_boundary = boundary.copy()
    for s, b in all_sensors:
        if s == sensor:
            continue
        d = manhattan(s, b)
        test_boundary = [x for x in test_boundary if manhattan(x, s) > d]
    test_boundary = [b for b in test_boundary if 0 <= b[0] <= mmax and 0 <= b[1] <= mmax]
    return test_boundary


def tuning_freq(c):
    x, y = c
    return 4000000*x + y


def part2():
    x = get_input('15')
    # x = TEST1.strip()

    sbs = list(parse(x))
    boundaries = dict()
    for s, b in sbs:
        boundary = list(make_boundary(s, b))
        boundaries[s] = boundary

    remaining_boundary = set()
    for s, boundary in boundaries.items():
        result = filter_boundary(s, boundary, sbs, 4000000)
        for r in result:
            remaining_boundary.add(r)

    c = remaining_boundary.pop()
    return tuning_freq(c)


def main():
    p2 = part2()
    print('Part 2:', p2)


if __name__ == '__main__':
    main()
