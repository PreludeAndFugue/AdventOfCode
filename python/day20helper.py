#!python3

from collections import Counter, defaultdict
from enum import Enum
from math import prod
from queue import Queue

INPUT = 'day20.txt'

TEST_INPUT = '''
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
'''

class Edge(Enum):
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

    @staticmethod
    def all():
        return [Edge.TOP, Edge.RIGHT, Edge.BOTTOM, Edge.LEFT]


    @staticmethod
    def are_pair(edge1, edge2):
        if edge1 == Edge.TOP and edge2 == Edge.BOTTOM:
            return True
        if edge1 == Edge.BOTTOM and edge2 == Edge.TOP:
            return True
        if edge1 == Edge.LEFT and edge2 == Edge.RIGHT:
            return True
        if edge1 == Edge.RIGHT and edge2 == Edge.LEFT:
            return True
        return False


    @staticmethod
    def direction(from_edge, to_edge):
        if from_edge == Edge.TOP and to_edge == Edge.BOTTOM:
            return (0, -1)
        if from_edge == Edge.BOTTOM and to_edge == Edge.TOP:
            return (0, 1)
        if from_edge == Edge.LEFT and to_edge == Edge.RIGHT:
            return (-1, 0)
        if from_edge == Edge.RIGHT and to_edge == Edge.LEFT:
            return (1, 0)
        raise Exception('Invalid direction')


class Rotation(Enum):
    R0 = 0
    R90 = 1
    R180 = 2
    R270 = 3


class Flip(object):
    NONE = 0
    HORIZONTAL = 1
    VERTICAL = 2


def transpose(matrix):
    return [''.join(list(x)) for x in zip(*matrix)]


def flip_horizontal(matrix):
    '''↕︎'''
    return matrix[::-1]


def flip_vertical(matrix):
    '''↔︎'''
    return [row[::-1] for row in matrix]


class TileEdge(object):
    def __init__(self, edge, text):
        self.edge = edge
        self.text = text


    def matches(self, other):
        if self.text != other.text:
            return False
        return Edge.are_pair(self.edge, other.edge)


    def __repr__(self):
        e = Edge(self.edge).name
        return f'TileEdge({e}, {self.text})'



class Tile(object):
    def __init__(self, n, text, rotation=Rotation.R0, flip=Flip.NONE):
        self.n = n
        self.text = text
        self.rotation = rotation
        self.flip = flip


    @property
    def trimmed_text(self):
        '''The text content without the border.'''
        return [t[1:-1] for t in self.text[1:-1]]


    def get_edge(self, n):
        if n == Edge.TOP:
            return TileEdge(n, self.text[0])
        elif n == Edge.BOTTOM:
            return TileEdge(n, self.text[-1])
        elif n == Edge.LEFT:
            text = ''.join(t[0] for t in self.text)
            return TileEdge(n, text)
        elif n == Edge.RIGHT:
            text = ''.join(t[-1] for t in self.text)
            return TileEdge(n, text)
        else:
            raise Exception(f'Invalid edge number: {n}')


    def get_opposite_edge(self, n):
        if n == Edge.TOP:
            return self.get_edge(Edge.BOTTOM)
        if n == Edge.BOTTOM:
            return self.get_edge(Edge.TOP)
        if n == Edge.LEFT:
            return self.get_edge(Edge.RIGHT)
        if n == Edge.RIGHT:
            return self.get_edge(Edge.LEFT)


    def get_matching_edges(self, other):
        '''Get's the edge of this Tile and the edge of the other
        tile that have matching patterns.'''
        for edge in self.get_all_edges():
            other_edge = other.get_opposite_edge(edge.edge)
            if edge.matches(other_edge):
                # print(self.n, other.n)
                # print(edge, other_edge)
                return edge, other_edge
        raise Exception("Shouldn't be here")


    def get_all_edges(self):
        for edge in Edge.all():
            yield self.get_edge(edge)


    def rotated(self, rotation):
        if rotation == Rotation.R90:
            text = flip_vertical(transpose(self.text))
            return Tile(self.n, text, rotation=rotation)
        elif rotation == Rotation.R180:
            text = flip_vertical(flip_horizontal(self.text))
            return Tile(self.n, text, rotation=rotation)
        elif rotation == Rotation.R270:
            text = flip_horizontal(transpose(self.text))
            return Tile(self.n, text, rotation=rotation)
        else:
            raise Exception(f'Invalid rotation: {rotation}')


    def flipped(self, flip):
        if flip == Flip.VERTICAL:
            text = flip_vertical(self.text)
            return Tile(self.n, text, flip=flip)
        elif flip == Flip.HORIZONTAL:
            text = flip_horizontal(self.text)
            return Tile(self.n, text, flip=flip)
        else:
            raise Exception(f'Invalid flip: {flip}')


    def all_orientations(self):
        vertical = self.flipped(Flip.VERTICAL)
        horizontal = self.flipped(Flip.HORIZONTAL)
        return [
            self,
            self.rotated(Rotation.R90),
            self.rotated(Rotation.R180),
            self.rotated(Rotation.R270),
            vertical,
            vertical.rotated(Rotation.R90),
            horizontal,
            horizontal.rotated(Rotation.R90)
        ]


    def __hash__(self):
        return self.n


    def __repr__(self):
        text = '\n'.join(self.text)
        return f'\n{self.n}\n----\n{text}'


def get_tile(text):
    name, text = text.split('\n', maxsplit=1)
    n = int(name[:-1].split(' ')[1])
    text = text.strip().split('\n')
    return Tile(n, text)


def get_tiles(input):
    for t in input.strip().split('\n\n'):
        yield get_tile(t)



def test0():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_fv = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    matrix_r90 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    matrix_r180 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    matrix_r270 = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    assert flip_horizontal(flip_vertical(matrix)) == flip_vertical(flip_horizontal(matrix))
    assert transpose(transpose(matrix)) == matrix
    assert flip_vertical(matrix) == matrix_fv
    assert flip_vertical(transpose(matrix)) == matrix_r90
    assert flip_vertical(flip_horizontal(matrix)) == matrix_r180
    assert flip_horizontal(transpose(matrix)) == matrix_r270


def test1():
    tiles1 = list(get_tiles(TEST_INPUT))

    tiles = []
    for t in tiles1:
        if t.n == 3079:
            tiles.append(t.flipped(Flip.VERTICAL).rotated(Rotation.R90))
        elif t.n == 1171:
            tiles.append(t.rotated(Rotation.R90))
        else:
            tiles.append(t)
    print(tiles)

    edge_map = defaultdict(list)
    for t in tiles:
        for edge in t.get_all_edges():
            edge_map[edge].append(t.n)
    print(edge_map)

    edge_map_1 = {}
    for k, v in edge_map.items():
        if len(v) == 2:
            edge_map_1[k] = v
        elif len(v) > 2:
            raise Exception('too many matches')
    print(edge_map_1)

    all_ids = set([t.n for t in tiles])
    used_ids = set()
    for v in edge_map_1.values():
        used_ids.update(v)
    print(used_ids)
    unused_ids = all_ids - used_ids
    print(unused_ids)

    edge_repetitions = []
    for v in edge_map_1.values():
        edge_repetitions.extend(v)
    edge_count = Counter(edge_repetitions)
    print(edge_count)
    corners = [k for k, v in edge_count.items() if v == 2]
    print(corners)
    print(prod(corners))


def test2():
    tiles = list(get_tiles(TEST_INPUT))
    t = tiles[0]
    print(t)
    t1 = t.rotated(Rotation.R90)
    print(t1)
    print(t.rotated(Rotation.R180))


def part1():
    tiles1 = list(get_tiles(open(INPUT, 'r').read()))

    tiles = []
    for t in tiles1:
        if t.n in [1597, 3499, 3821, 3677]:
            tiles.append(t.flipped(Flip.VERTICAL))
        elif t.n in [1249, 1607, 2339, 3019, 3593, 1879, 2089]:
            tiles.append(t.flipped(Flip.HORIZONTAL))
        elif t.n in [1031, 1129, 1163, 1579, 1619, 1877, 2039, 2131, 2161, 2311, 2437, 2927, 3571, 3733, 3907]:
            tiles.append(t.rotated(Rotation.R180))
        elif t.n in [1451, 1453, 1999, 2593, 2657, 3389, 3391, 3709]:
            tiles.append(t.rotated(Rotation.R90))
        elif t.n in []:
            tiles.append(t.flipped(Flip.VERTICAL).rotated(Rotation.R90))
        elif t.n in []:
            tiles.append(t.rotated(Rotation.R270))
        elif t.n in [1123]:
            tiles.append(t.flipped(Flip.HORIZONTAL).rotated(Rotation.R90))
        else:
            tiles.append(t)
    # print(tiles)

    edge_map = defaultdict(list)
    for t in tiles:
        for edge in t.get_all_edges():
            edge_map[edge].append(t.n)
    # print(edge_map)

    edge_map_1 = {}
    for k, v in edge_map.items():
        if len(v) == 2:
            edge_map_1[k] = v
        elif len(v) > 2:
            raise Exception('too many matches')
    # print(edge_map_1)

    all_ids = set([t.n for t in tiles])
    used_ids = set()
    for v in edge_map_1.values():
        used_ids.update(v)
    # print(used_ids)
    unused_ids = all_ids - used_ids
    print('unused')
    print(sorted(unused_ids))
    print(len(unused_ids))
    print()

    edge_repetitions = []
    for v in edge_map_1.values():
        edge_repetitions.extend(v)
    edge_count = Counter(edge_repetitions)
    # print(edge_count)
    c1 = [k for k, v in edge_count.items() if v == 1]
    print('c1')
    print(sorted(c1))
    print(len(c1))
    print()

    c2 = [k for k, v in edge_count.items() if v == 2]
    print('c2')
    print(sorted(c2))
    print(len(c2))
    print()

    c3 = [k for k, v in edge_count.items() if v == 3]
    print('c3')
    # print(sorted(c3))
    print(len(c3))
    print()

    c4 = [k for k, v in edge_count.items() if v == 4]
    print('c4')
    # print(sorted(c4))
    print(len(c4))
    print()

    # print(prod(corners))

    # good tiles
    centre_tiles = set([k for k, v in edge_count.items() if v == 4])
    print(sorted(centre_tiles))
    connected_to_centre_tiles = set()
    for v in edge_map_1.values():
        if centre_tiles.intersection(v):
            connected_to_centre_tiles.update(v)
    print(sorted(connected_to_centre_tiles))

    print(sorted(set(c2) - connected_to_centre_tiles))


def main():
    # test0()
    # test1()
    # test2()

    part1()


if __name__ == "__main__":
    main()
