
from help import get_input


TEST1 = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''


DIR = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}


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
    else:
        raise ValueError


def part1(data):
    H = 0, 0
    T = 0, 0
    locations = set()
    for d, n in data:
        for _ in range(n):
            dx, dy = DIR[d]
            H = H[0] + dx, H[1] + dy
            T = move_tail(H, T)
            locations.add(T)
    return len(locations)


def main():
    s = get_input('09')
    # s = TEST1
    data = list(parse(s))
    print(data)

    p1 = part1(data)
    print('Part 1:', p1)


if __name__ == '__main__':
    main()
