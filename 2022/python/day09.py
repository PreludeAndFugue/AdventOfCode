
from help import get_input


TEST1 = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''


TEST2 = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''


DIR = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}


def draw_rope(rope):
    xs = [k[0] for k in rope]
    ys = [k[1] for k in rope]
    d = {k: str(9 - n) for n, k in enumerate(reversed(rope))}
    x_min = min(xs) - 1
    x_max = max(xs) + 1
    y_min = min(ys) - 1
    y_max = max(ys) + 1
    rows = []
    for y in range(y_min, y_max + 1):
        row = []
        for x in range(x_min, x_max + 1):
            location = x, y
            item = d.get(location, '.')
            row.append(item)
        rows.append(''.join(row))
    print('\n'.join(rows))
    print()


def parse(s):
    for line in s.split('\n'):
        d, n = line.split(' ')
        n = int(n)
        yield d, n


def move_tail(H, T):
    Tx, Ty = T
    Hx, Hy = H
    dx = Hx - Tx
    dy = Hy - Ty
    d = abs(dx) + abs(dy)
    if d == 0 or d == 1:
        return T
    elif d == 2:
        if dx == 0 or dy == 0:
            return Tx + dx//2, Ty + dy//2
        else:
            return T
    elif d == 3:
        if abs(dx) == 2:
            return Tx + dx//2, Ty + dy
        else:
            return Tx + dx, Ty + dy//2
    elif d == 4:
        # Extra rule for part 2
        return Tx + dx//2, Ty + dy//2
    else:
        raise ValueError


def part2(data):
    rope = [(0, 0)]*10
    # draw_rope(rope)
    locations1 = set()
    locations9 = set()
    for d, n in data:
        # print(d, n)
        for _ in range(n):
            dx, dy = DIR[d]
            H = rope[0]
            H = H[0] + dx, H[1] + dy
            rope[0] = H
            for i, (h, t) in enumerate(zip(rope, rope[1:])):
                t = move_tail(h, t)
                rope[i + 1] = t
            # draw_rope(rope)
            locations1.add(rope[1])
            locations9.add(rope[-1])
    return len(locations1), len(locations9)


def main():
    s = get_input('09')
    # s = TEST2
    data = list(parse(s))

    p1, p2 = part2(data)

    print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()
