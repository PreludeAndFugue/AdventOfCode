
from help import get_input

'''
Part 1
------
418: too low

'''

TEST1 = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''


DIRS = [(0, 1), (-1, 1), (1, 1)]
START = (500, 0)

ROCK = '█'
SAND = 'o'
VOID = '.'


def parse(s):
    m = {START: '+'}
    for line in s.split('\n'):
        coords = [tuple(map(int, coord.split(','))) for coord in line.split(' -> ')]
        for p1, p2 in zip(coords, coords[1:]):
            x1, y1 = p1
            x2, y2 = p2
            dx = x2 - x1
            dy = y2 - y1
            if dx != 0:
                assert dy == 0
                x_sgn = -1 if dx < 0 else 1
                for i in range(abs(dx) + 1):
                    m[(x1 + i*x_sgn, y1)] = ROCK
            elif dy != 0:
                assert dx == 0
                y_sgn = -1 if dy < 0 else 1
                for i in range(dy + 1):
                    m[(x1, y1 + i*y_sgn)] = ROCK
            else:
                raise ValueError
    return m


def draw(m):
    xs = [x for (x, _) in m.keys()]
    ys = [y for (_, y) in m.keys()]
    x_min = min(xs)
    x_max = max(xs)
    y_min = min(ys)
    y_max = max(ys)
    rows = []
    for y in range(y_min, y_max + 1):
        row = []
        for x in range(x_min, x_max + 1):
            value = m.get((x, y), VOID)
            row.append(value)
        rows.append(''.join(row))
    result = '\n'.join(rows)
    print(result)


def get_next(location, m):
    lx, ly = location
    for x, y in DIRS:
        nx = lx + x
        ny = ly + y
        n = (nx, ny)
        value = m.get(n, VOID)
        if value == VOID:
            return n
    return None


def is_below_bottom(l, m):
    max_y = max(y for (_, y) in m.keys())
    _, y = l
    return y > max_y


def drop(m):
    l = START
    while True:
        ln = get_next(l, m)
        if ln is None:
            m[l] = SAND
            return True
        elif is_below_bottom(ln, m):
            return False
        else:
            l = ln


def main():
    s = get_input('14')
    # s = TEST1.strip()
    m = parse(s)
    draw(m)

    while True:
        result = drop(m)
        if not result:
            break
        draw(m)
        print()
        # input()

    c = sum(1 for v in m.values() if v == SAND)
    print(c)


if __name__ == '__main__':
    main()
