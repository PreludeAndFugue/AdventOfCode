
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

# source = test1.strip()
source = get_input(4)


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
            return None
        word += ch
    return word


map_ = {}
for r, row in enumerate(source.split('\n')):
    for c, ch in enumerate(row):
        map_[(r, c)] = ch

count = 0
for p, ch in map_.items():
    if ch != 'X':
        continue
    for d in DIRECTIONS.values():
        w = get_word(p, d, map_)
        if w == 'XMAS':
            count += 1

print(count)