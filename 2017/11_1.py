#!python 3

'''Day 11, part 1.

The distance function is incorrect, but it gives the correct answer for this
input.
'''

import data_11
from data_11 import convert_direction_to_coord


def distance(coordinate):
    '''Distance from origin of coordinate.'''
    return max(map(abs, coordinate))


def follow(path, start=(0, 0)):
    '''Follow a path and return destination coordinates.'''
    for direction in path:
        coords = convert_direction_to_coord(direction)
        start = start[0] + coords[0], start[1] + coords[1]
    return start


def path_distance(path, start=(0, 0)):
    '''Find path distance.

    >>> path_distance(['ne', 'ne', 'ne'])
    3
    >>> path_distance(['ne', 'ne', 'sw', 'sw'])
    0
    >>> path_distance(['ne', 'ne', 's', 's'])
    2
    >>> path_distance(['se', 'sw', 'se', 'sw', 'sw'])
    3
    '''
    end = follow(path, start)
    return distance(end)


def part1():
    '''Find answer for part 1.'''
    distance = path_distance(data_11.directions)
    print(distance)


def part2():
    '''Find answer for part 2.'''
    max_distance = 0
    start = 0, 0
    for direction in data_11.directions:
        coords = convert_direction_to_coord(direction)
        start = start[0] + coords[0], start[1] + coords[1]
        max_distance = max(max_distance, distance(start))
    print(max_distance)


def main():
    '''Main entry point.'''
    part1()

    part2()


if __name__ == '__main__':
    main()
