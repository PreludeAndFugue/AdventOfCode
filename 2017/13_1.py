#!python3

'''Day 13, parts 1 & 2.'''

from data_13 import data, period, test_data


def total_cost(layers, start=0):
    '''Find the total cost of layers.

    >>> total_cost([(0, 3), (1, 2), (4, 4), (6, 4)])
    24
    '''
    total = 0
    for layer, range_ in layers:
        p = period(range_)
        if (layer + start) % p == 0:
            total += layer * range_
    return total


def is_caught(layers, start=0):
    '''Find if caught.'''
    for layer, range_ in layers:
        p = period(range_)
        if (layer + start) % p == 0:
            return True
    return False


def part1():
    '''The answer to part 1.'''
    total = total_cost(data)
    print(total)


def part2():
    '''Main entry point.'''
    for start in range(10000000):
        caught = is_caught(data, start)
        if not caught:
            print(start)
            break


if __name__ == '__main__':
    part1()

    part2()
