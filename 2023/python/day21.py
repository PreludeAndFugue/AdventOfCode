
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
        for c, ch in enumerate(line):
            # print(r, c, ch)
            if ch == '.':
                map_.add(complex(r, c))
            elif ch == 'S':
                start = complex(r, c)
                map_.add(start)
            else:
                pass
    return map_, start


def expand_map(d, n):
    result = ''
    for i in range(3):
        for line in d.split('\n'):
            for j in range(3):
                # print(i, j)
                if i == 1 and j == 1:
                    result += line
                else:
                    if 'S' in line:
                        # print('removing S', i, j)
                        l = line.replace('S', '.')
                        result += l
                    else:
                        result += line
            result += '\n'
    # print(result)
    return make_map(result)


def printer(map_, positions):
    p = [(int(c.real), int(c.imag)) for c in map_]
    p_min = min(p)
    p_max = max(p)
    # print(p_min, p_max)
    # print(positions)
    rows = []
    for r in range(p_min[0], p_max[0] + 1):
        row = []
        for c in range(p_min[1], p_max[1] + 1):
            z = complex(r, c)
            # print(z)
            if z in positions:
                # print('z in positions', z)
                # input()
                row.append('o')
            elif z in map_:
                row.append(' ')
            else:
                row.append('#')
        rows.append(''.join(row))
    print('\n'.join(rows))


def move(map_, positions):
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
    map_, start = expand_map(d, 3)
    print('start', start)
    # print(map_)
    positions = set([start])

    for _ in range(30):
        positions = move(map_, positions)

        printer(map_, positions)
        input()


def main():
    # d = get_input('21').strip()
    d = TEST.strip()

    # p1 = part1(d)
    # print(p1)

    part2(d)

    # z1 = complex(3, 4)
    # z2 = complex(2, 5)
    # s = set([complex(3, 4)])
    # print(s)
    # print(z1 in s)
    # print(z2 in s)

if __name__ == '__main__':
    main()
