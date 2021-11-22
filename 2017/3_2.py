#!python3

'''Day 3, part 2.'''

import pprint

def items_in_ring(n):
    '''The count of numbers in ring.
    >>> items_in_ring(1)
    1
    >>> items_in_ring(2)
    8
    >>> items_in_ring(3)
    16
    '''
    if n == 1:
        return 1
    return 8*(n - 1)


def coord_below_start_of_ring(n):
    '''Coord of start position of ring n.
    >>> coord_below_start_of_ring(1)
    (0, -1)
    >>> coord_below_start_of_ring(2)
    (1, -1)
    >>> coord_below_start_of_ring(3)
    (2, -2)
    '''
    if n == 1:
        return 0, -1
    return (n - 1), -1*(n - 1)


def coord_generator():
    '''Generate sequence of coords for spiral.'''
    yield (0, 0)
    ring = 2
    current_coord = (1, -1)
    while True:
        ring_side = int(items_in_ring(ring)/4)
        for diff in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            for _ in range(ring_side):
                current_coord = current_coord[0] + diff[0], current_coord[1] + diff[1]
                yield current_coord

        ring += 1
        current_coord = coord_below_start_of_ring(ring)


def neighbour_sum(grid, coord):
    '''Calculate the sum of neighbours for a coord.'''
    neighbours = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
    total = 0
    for neighbour in neighbours:
        row, col = coord[0] + neighbour[0], coord[1] + neighbour[1]
        total += grid[row][col]
    return total


def main():
    test = 277678
    grid_size = 21
    centre = 10, 10
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    grid[centre[0]][centre[1]] = 1
    c_gen = coord_generator()
    next(c_gen)
    for _ in range(60):
        coord = next(c_gen)
        coord_and_offset = coord[0] + centre[0], coord[1] + centre[1]
        s = neighbour_sum(grid, coord_and_offset)
        if s > test:
            print(s)
            break
        # print(coord, centre, coord_and_offset, s)
        grid[coord_and_offset[0]][coord_and_offset[1]] = s

    pprint.pprint(grid)


if __name__ == '__main__':
    main()
