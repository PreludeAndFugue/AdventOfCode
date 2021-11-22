#!python3

'''
Hexagonal grids
https://www.redblobgames.com/grids/hexagons/

Neighbours
https://www.redblobgames.com/grids/hexagons/#neighbors-doubled

'''

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

OFFSETS = list(DIRECTIONS.values())


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


def get_neighbours(c):
    x, y = c
    for dx, dy in OFFSETS:
        yield x + dx, y + dy


def is_black_update(tile, tiles):
    black = sum(tiles.get(n, False) for n in get_neighbours(tile))
    if tiles.get(tile, False):
        return black == 1 or black == 2
    else:
        return black == 2


def change_day(tiles):
    new_tiles = {}
    for c in tiles.keys():
        new_tiles[c] = is_black_update(c, tiles)
        for n in get_neighbours(c):
            new_tiles[n] = is_black_update(n, tiles)
    return {k: v for k, v in new_tiles.items() if v}


def make_tiles(paths):
    tiles = defaultdict(bool)
    for path in paths:
        c = follow_path(path)
        tiles[c] = not tiles.get(c, False)
    return tiles


def count_black(tiles):
    return Counter(tiles.values())[True]


def _part1(paths):
    tiles = make_tiles(paths)
    return count_black(tiles)


def test1():
    c = _part1(get_input(TEST_INPUT))
    assert c == 10


def part1():
    paths = get_input(open(INPUT, 'r').read())
    return _part1(paths)


def _part2(paths):
    tiles = make_tiles(paths)
    for _ in range(100):
        tiles = change_day(tiles)
    return count_black(tiles)


def test2():
    paths = get_input(TEST_INPUT)
    c = _part2(paths)
    assert c == 2208


def part2():
    paths = get_input(open(INPUT, 'r').read())
    return _part2(paths)


def main():
    test1()

    p = part1()
    print(p)

    test2()

    p = part2()
    print(p)


if __name__ == "__main__":
    main()
