
from help import get_input

test1 = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

DIRECTIONS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
    'UR': (-1, 1),
    'UL': (-1, -1),
    'DR': (1, 1),
    'DL': (1, -1)
}


def parse(source):
    map_ = {}
    for r, row in enumerate(source.split('\n')):
        for c, ch in enumerate(row):
            map_[(r, c)] = ch
    return map_


def get_word(p, direction, map_):
    word = 'X'
    r, c = p
    dr, dc = direction
    for _ in range(3):
        r += dr
        c += dc
        pp = r, c
        ch = map_.get(pp, None)
        if ch is None:
            return False
        word += ch
    return word == 'XMAS'


def get_word_2(p, map_):
    check = set(['M', 'S'])
    r, c = p
    x1 = map_.get((r - 1, c - 1), None)
    x2 = map_.get((r + 1, c + 1), None)

    y1 = map_.get((r - 1, c + 1), None)
    y2 = map_.get((r + 1, c - 1), None)

    if not any([x1, x2, y1, y2]):
        return False

    x = set([x1, x2])
    y = set([y1, y2])
    return x == check and y == check


def part1():
    # source = test1.strip()
    source = get_input(4)
    map_ = parse(source)

    count = 0
    for p, ch in map_.items():
        if ch != 'X':
            continue
        for d in DIRECTIONS.values():
            count +=  get_word(p, d, map_)

    print(count)


def part2():
    # source = test1.strip()
    source = get_input(4)
    map_ = parse(source)

    count = 0
    for p, ch in map_.items():
        if ch != 'A':
            continue
        count += get_word_2(p, map_)

    print(count)



part1()
part2()