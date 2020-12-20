#!python3

from math import prod

from day20helper import INPUT, TEST_INPUT, get_tiles


def matching_edge(tile1, tile2):
    edges1 = set(tile1.get_all_edges())
    edges2 = set(tile2.get_all_edges())
    intersection = edges1.intersection(edges2)
    assert len(intersection) < 2
    return len(intersection) > 0


def get_neighbours(tile, tiles):
    neighbours = []
    for t in tiles:
        if t.n == tile.n:
            continue
        for o in t.all_orientations():
            if matching_edge(tile, o):
                neighbours.append(o)
                break
    return neighbours


def get_all_neighbours(tiles):
    neighbours = {}
    for tile in tiles:
        n = get_neighbours(tile, tiles)
        neighbours[tile.n] = n
    return neighbours


def _part1(tiles):
    neighbours = get_all_neighbours(tiles)
    corners = [k for k, v in neighbours.items() if len(v) == 2]
    return prod(corners)


def test1():
    tiles = sorted(list(get_tiles(TEST_INPUT)), key=lambda t: t.n)
    assert _part1(tiles) == 20899048083289


def part1():
    tiles = list(get_tiles(open(INPUT, 'r').read()))
    return _part1(tiles)


def test2():
    pass


def main():
    test1()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
