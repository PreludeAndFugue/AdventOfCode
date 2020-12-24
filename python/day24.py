#!python3

from collections import Counter, defaultdict

INPUT = 'day24.txt'

TEST_INPUT = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
'''

DIRECTIONS = {
    'w': (-2, 0),
    'nw': (-1, -1),
    'ne': (1, -1),
    'e': (2, 0),
    'se': (1, 1),
    'sw': (-1, 1)
}


def parse_line(line):
    part = ''
    for x in line:
        if x in ('s', 'n'):
            part = x
            continue
        if part:
            yield part + x
            part = ''
        else:
            yield x


def get_input(input):
    for line in input.strip().split('\n'):
        yield list(parse_line(line))


def follow_path(path):
    '''Find the final coordinates from (0, 0) by following the path.'''
    x, y = 0, 0
    for step in path:
        dx, dy = DIRECTIONS[step]
        x += dx
        y += dy
    return x, y


def _part1(paths):
    tiles = defaultdict(bool)
    for path in paths:
        c = follow_path(path)
        tiles[c] = not tiles[c]
    count = Counter(tiles.values())
    return count[True]


def test1():
    c = _part1(get_input(TEST_INPUT))
    assert c == 10


def part1():
    paths = get_input(open(INPUT, 'r').read())
    return _part1(paths)


def main():
    test1()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
