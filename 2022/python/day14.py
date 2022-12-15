
from help import get_input

'''
Part 1
------
418: too low

'''

TEST1 = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''


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
                if dx < 0:
                    r = range(dx, 1)
                else:
                    r = range(dx + 1)
                for i in r:
                    m[(x1 + i, y1)] = ROCK
            elif dy != 0:
                assert dx == 0
                if dy < 0:
                    r = range(dy, 1)
                else:
                    r = range(dy + 1)
                for i in r:
                    m[(x1, y1 + i)] = ROCK
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
    ns = []
    for x in (0, -1, 1):
        nx = lx + x
        ny = ly + 1
        n = (nx, ny)
        value = m.get(n, VOID)
        if value == VOID:
            ns.append(n)
    return ns


def drop(m, y_max):
    l = START
    while True:
        lns = get_next(l, m)
        if not lns:
            m[l] = SAND
            return True
        ln = lns[0]
        if ln[1] > y_max:
            return False
        else:
            l = ln


def add_floor(m):
    y_max = max(y for _, y in m.keys())
    for x in range(0, 1000):
        m[(x, y_max + 2)] = ROCK


def fill(m):
    '''A flood fill for a faster part 2.'''
    q = [START]
    while q:
        l = q.pop()
        m[l] = SAND
        for n in get_next(l, m):
            q.append(n)
    return m


def part1(s):
    m = parse(s)
    y_max = max(y for (_, y) in m.keys())
    while True:
        result = drop(m, y_max)
        if not result:
            break
    return sum(1 for v in m.values() if v == SAND)


def part2(s):
    m = parse(s)
    add_floor(m)
    fill(m)
    return sum(1 for v in m.values() if v == SAND)


def main():
    s = get_input('14')
    # s = TEST1.strip()
    p1 = part1(s)
    p2 = part2(s)

    print('Part 1:', p1)
    print('Part 2:', p2)



if __name__ == '__main__':
    main()
