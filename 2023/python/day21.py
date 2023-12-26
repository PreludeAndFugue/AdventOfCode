
from pathlib import Path

from PIL import Image

from help import get_input

TEST = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''


def make_map(d):
    map_ = set()
    start = None
    for r, line in enumerate(d.split('\n')):
        c_max = len(line)
        for c, ch in enumerate(line):
            if ch == '.':
                map_.add(complex(r, c))
            elif ch == 'S':
                start = complex(r, c)
                map_.add(start)
    return map_, start


def expand_map(d, n):
    result = ''
    for i in range(n):
        for line in d.split('\n'):
            for j in range(n):
                if i == n//2 and j == n//2:
                    result += line
                else:
                    if 'S' in line:
                        l = line.replace('S', '.')
                        result += l
                    else:
                        result += line
            result += '\n'
    return make_map(result)


def printer(map_, positions, i):
    p = [(int(c.real), int(c.imag)) for c in map_]
    p_min = min(p)
    p_max = max(p)
    bytes = bytearray()
    for r in range(p_min[0], p_max[0] + 1):
        for c in range(p_min[1], p_max[1] + 1):
            z = complex(r, c)
            if z in positions:
                bytes.append(255)
            elif z in map_:
                bytes.append(0)
            else:
                bytes.append(70)

    size = p_max[0] + 1, p_max[1] + 1
    p = Path(f'./day21/day21_{i:0>4d}.png')
    im = Image.frombytes('L', size, bytes)
    im.save(p)


def move(positions, map_):
    new_positions = set()
    for p in positions:
        for d in DIR:
            pp = p + d
            if pp in map_:
                new_positions.add(pp)
    return new_positions


DIR = (complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1))


def part1(d):
    map_, start = make_map(d)
    positions = set([start])
    for _ in range(64):
        positions = move(map_, positions)
    return len(positions)


def part2(d):
    # The following commented out code was used to calculate the number of positons
    # after the following number of steps: 65, 65 + 131, 65 + 2*131, etc.
    # Then enter values into Numbers spreadsheet and fit to 2nd degree polynomial.

    # map_, start = expand_map(d, 11)
    # positions = frozenset([start])

    # x = 65
    # for i in range(x):
    #     positions = move(positions, map_)
    # print(len(positions))
    # printer(map_, positions, 0)

    # for j in range(5):
    #     for i in range(dx):
    #         positions = move(positions, map_)
    #     print(len(positions))
    #     printer(map_, positions, j + 1)

    def f(x):
        '''Exact quadratic equation to calculate the number of positions after the
        following number of steps:

        x = 0 -> 65 steps
        x = 1 -> 65 + 131 steps
        x = 2 -> 65 + 2*131 steps
        ...
        '''
        return 14669*x*x + 14738*x + 3701

    # T = 202300*131 + 65
    T = 26501365
    Y = 202300

    return f(Y)


def main():
    d = get_input('21').strip()
    # d = TEST.strip()

    p1 = part1(d)
    print(p1)

    p2 = part2(d)
    print(p2)


if __name__ == '__main__':
    main()
