#!python3

from math import prod, sqrt
import re

TEST_IMAGE = '''.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###'''


from day20helper import (
    INPUT, TEST_INPUT, Edge, get_tiles, transpose
)


def have_matching_edge(tile1, tile2):
    for e1 in tile1.get_all_edges():
        e2 = tile2.get_opposite_edge(e1.edge)
        if e1.matches(e2):
            return True
    return False


def get_neighbours(tile, tiles):
    neighbours = []
    for t in tiles:
        if t.n == tile.n:
            continue
        for o in t.all_orientations():
            if have_matching_edge(tile, o):
                neighbours.append(o)
                # break
    return neighbours


def get_all_neighbours(tiles):
    neighbours = {}
    to_check = {tiles[0].n: tiles[0]}
    seen = set()
    while to_check:
        _, tile = to_check.popitem()
        seen.add(tile.n)
        tile_neighbours = get_neighbours(tile, tiles)
        neighbours[tile.n] = tile_neighbours
        for n in tile_neighbours:
            if n.n not in seen:
                to_check[n.n] = n
    return neighbours


def build_map(tiles, all_neighbours):
    '''Build a dict
    key: tile number
    value: coordinate
    '''
    t0 = tiles[0]
    tiles = {tile.n: tile for tile in tiles}
    tiles_correct_orientation = []
    tile_map = {t0.n: (0, 0)}
    to_check = [t0]
    seen = set()
    while to_check:
        tile = to_check.pop()
        seen.add(tile.n)
        tiles_correct_orientation.append(tile)
        for neighbour in all_neighbours[tile.n]:
            e1, e2 = tile.get_matching_edges(neighbour)
            dx, dy = Edge.direction(e1.edge, e2.edge)
            x, y = tile_map[tile.n]
            tile_map[neighbour.n] = x + dx, y + dy
            if neighbour.n not in seen:
                to_check.append(neighbour)
    return tile_map, tiles_correct_orientation


def fix_map_origin(tile_map):
    values = list(tile_map.values())
    min_x = min(v[0] for v in values)
    min_y = min(v[1] for v in values)
    dx = -min_x
    dy = -min_y
    new_map = {}
    for k, (x, y) in tile_map.items():
        new_map[k] = x + dx, y + dy
    return new_map


def make_whole_map(tile_map, tiles, test=False):
    tiles = {tile.n: tile for tile in tiles}
    values = list(tile_map.values())
    xs = list(v[0] for v in values)
    ys = list(v[1] for v in values)
    x_min = min(xs)
    y_min = min(ys)
    x_max = max(xs)
    y_max = max(ys)
    assert x_min == 0
    assert y_min == 0
    rows = y_max + 1
    cols = x_max + 1
    whole_map = [[None for _ in range(cols)] for _ in range(rows)]
    dummy_map = [[None for _ in range(cols)] for _ in range(rows)]
    for tile_n, coord in tile_map.items():
        tile = tiles[tile_n]
        col, row = coord
        whole_map[row][col] = tile.text if test else tile.trimmed_text
        dummy_map[row][col] = tile.n
    # for row in dummy_map:
    #     print(row)
    return whole_map


def make_image(whole_map, test=False):
    spacer = ' ' if test else ''
    new_line = '\n\n' if test else '\n'
    image = []
    for row in whole_map:
        x = '\n'.join(spacer.join(x) for x in zip(*row))
        image.append(x)
    return new_line.join(image)


def flip_image(image):
    '''Flip top row to bottom row.'''
    lines = image.strip().split('\n')
    return '\n'.join(lines[::-1])


def rotate_image(image):
    '''Rotate clockwise.'''
    flipped = flip_image(image)
    lines = flipped.strip().split('\n')
    lines = transpose(lines)
    return '\n'.join(lines)


ALL_TRANSFORMATIONS = [
    (),
    (rotate_image,),
    (rotate_image, rotate_image),
    (rotate_image, rotate_image, rotate_image),
    (flip_image,),
    (flip_image, rotate_image),
    (flip_image, rotate_image, rotate_image),
    (flip_image, rotate_image, rotate_image, rotate_image)
]


def test_all_transformations():
    image = 'AB\nDC'
    for transforms in ALL_TRANSFORMATIONS:
        i = image
        for t in transforms:
            i = t(i)
        print(i)
        print()


def find_monsters(flat_image):
    '''
        "                  # "
        "#    ##    ##    ###"
        " #  #  #  #  #  #   "
    '''
    p1 = r"..................#."
    p2 = r"#....##....##....###"
    p3 = r".#..#..#..#..#..#..."
    image_width = int(sqrt(len(flat_image)))
    spacer_width = image_width - len(p1)
    print(spacer_width)
    spacer = r"." * spacer_width
    pattern = p1 + spacer + p2 + spacer + p3
    print(pattern)
    regex = re.compile(pattern)
    count = 0
    position = 0
    while True:
        m = regex.search(flat_image, pos=position)
        if m:
            count += 1
            m.start()
            position = m.start() + 1
        else:
            break
    return count


def find_all_monsters(image):
    all_counts = []
    for i, transformations in enumerate(ALL_TRANSFORMATIONS):
        for t in transformations:
            image = t(image)
        write_image(image, i)
        flat_image = ''.join(image.strip().split('\n'))
        c = find_monsters(flat_image)
        all_counts.append(c)
    return max(all_counts)


def _part1(neighbours):
    corners = [k for k, v in neighbours.items() if len(v) == 2]
    return prod(corners)


def test1(neighbours):
    assert _part1(neighbours) == 20899048083289


def part1(neighbours):
    return _part1(neighbours)


def write_image(image, i):
    with open(f'day20_{i}_out.txt', 'w') as f:
        # text = ''.join(line.strip() for line in image)
        # f.write(text)

        f.writelines(image)


def _part2(tiles, all_neighbours):
    tile_map, tiles_correct_orientation = build_map(tiles, all_neighbours)
    tile_map = fix_map_origin(tile_map)
    whole_map = make_whole_map(tile_map, tiles_correct_orientation, test=True)
    image = make_image(whole_map, test=True)
    # write_image(image, 999)
    c = find_all_monsters(image)
    return c


def test2(tiles, all_neighbours):
    c = _part2(tiles, all_neighbours)
    # assert c == 2


def part2(tiles, all_neighbours):
    return _part2(tiles, all_neighbours)


def main():
    test_tiles = list(get_tiles(TEST_INPUT))
    test_neighbours = get_all_neighbours(test_tiles)

    # tiles = list(get_tiles(open(INPUT, 'r').read()))
    # neighbours = get_all_neighbours(tiles)

    test1(test_neighbours)

    # p = part1(neighbours)
    # print(p)

    # test_all_transformations()

    test2(test_tiles, test_neighbours)

    # p = part2(tiles, neighbours)
    # print(p)


if __name__ == "__main__":
    main()
