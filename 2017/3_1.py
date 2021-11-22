#!python3

'''
Day 3, part 1
'''

import math

def ring(n):
    '''Calculate the ring a number belongs to.

    >>> ring(1)
    1
    >>> ring(2)
    2
    >>> ring(9)
    2
    >>> ring(10)
    3
    >>> ring(25)
    3
    >>> ring(26)
    4
    '''
    m = math.ceil(math.sqrt(n))
    if m % 2 == 0:
        return int((m + 2)/2)
    return int((m + 1)/2)


def ring_start(n):
    '''The first value in ring n.
    >>> ring_start(1)
    1
    >>> ring_start(2)
    2
    >>> ring_start(3)
    10
    >>> ring_start(4)
    26
    >>> ring_start(5)
    50
    >>> ring_start(6)
    82
    '''
    if n == 1:
        return 1
    return (2*n - 3)**2 + 1


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


def final_coord(n):
    '''Calculate final position for a number.'''
    if n == 1:
        return 0, 0
    ring_number = ring(n)
    start = ring_start(ring_number)
    current_number = start - 1
    items = items_in_ring(ring_number)
    position = coord_below_start_of_ring(ring_number)
    # print(ring_number, start, current_number, position)
    for diffs in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        for _ in range(int(items/4)):
            position = (position[0] + diffs[0], position[1] + diffs[1])
            current_number += 1
            # print(current_number, position)
            if current_number == n:
                return position


def distance(n):
    '''What distance to move n back to position of 1.
    >>> distance(1)
    0
    >>> distance(2)
    1
    >>> distance(3)
    2
    >>> distance(11)
    2
    >>> distance(17)
    4
    >>> distance(22)
    3
    >>> distance(26)
    5
    >>> distance(1024)
    31
    '''
    coord = final_coord(n)
    return abs(coord[0]) + abs(coord[1])


def main():
    '''Main entry point.'''
    n = 277678
    d = distance(n)
    print(d)


if __name__ == '__main__':
    main()
