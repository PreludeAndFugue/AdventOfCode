#!python3

'''Day 14, part 2.'''

from collections import defaultdict

from part10 import knot_hash
from part14 import hex_to_bin

TEST = 'flqrgnkx'
CODE = 'ugkiagan'

def make_bin_grid(code):
    '''Make binary grid from code.'''
    rows = []
    for i in range(128):
        full_code = f'{code}-{i}'
        h = knot_hash(full_code)
        b = hex_to_bin(h)
        rows.append(b)
    return rows


def bin_grid_to_coords(bin_grid):
    '''Convert bin grid to a list of coords.'''
    coords = []
    for i, row in enumerate(bin_grid):
        for col, digit in enumerate(row):
            if digit == '1':
                coords.append((i, col))
    return set(coords)


def get_neighbours(coord, upper_bound=127):
    '''Calculate neighbours of coord.

    >>> get_neighbours((0, 0))
    [(1, 0), (0, 1)]
    >>> get_neighbours((1, 1))
    [(0, 1), (2, 1), (1, 0), (1, 2)]
    '''
    row, col = coord
    neighbours = []
    for i in (-1, 1):
        new_row = row + i
        if 0 <= new_row <= upper_bound:
            neighbours.append((new_row, col))
    for j in (-1, 1):
        new_col = col + j
        if 0 <= new_col <= upper_bound:
            neighbours.append((row, new_col))
    return neighbours


def make_regions(coords):
    '''Calculate regions from coords.'''
    regions = defaultdict(list)
    current_region_number = 1
    while coords:
        region = find_region(coords)
        regions[current_region_number] = region
        current_region_number += 1
        coords = coords - region
    return regions


def find_region(coords):
    '''Find a region in the coords.'''
    coords_copy = set(coords)
    region = set()
    seen_nodes = set()
    next_nodes = set([coords_copy.pop()])
    while next_nodes:
        next_node = next_nodes.pop()
        if next_node in seen_nodes:
            continue
        seen_nodes.add(next_node)
        region.add(next_node)
        neighbours = get_neighbours(next_node)
        for neighbour in neighbours:
            if neighbour in coords_copy and neighbour not in seen_nodes:
                next_nodes.add(neighbour)
    return region


def main():
    '''Main entry point.'''
    grid = make_bin_grid(CODE)
    coords = bin_grid_to_coords(grid)

    regions = make_regions(coords)
    print(len(regions))


if __name__ == '__main__':
    main()
