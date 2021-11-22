#!python3

'''Day 6, part 1.'''

import data_6


def cycle_count(banks):
    '''Count the number of cycles to repeat a configuration.

    >>> cycle_count([0, 2, 7, 0])
    5
    '''
    configurations = set()
    banks = tuple(banks)
    while banks not in configurations:
        configurations.add(banks)
        banks = data_6.redistribute(banks)
    return len(configurations)


def main():
    '''Main entry point.'''
    banks = data_6.data
    count = cycle_count(banks)
    print(count)


if __name__ == '__main__':
    main()
