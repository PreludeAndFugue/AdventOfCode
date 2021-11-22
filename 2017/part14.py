#!python3

'''Day 14, part 1.'''

from part10 import knot_hash


TEST = 'flqrgnkx'
CODE = 'ugkiagan'


def hex_to_bin(hex_string):
    '''Convert hex string to binary string.

    >>> hex_to_bin('1')
    '0001'
    >>> hex_to_bin('8')
    '1000'
    >>> hex_to_bin('f')
    '1111'
    >>> hex_to_bin('a0c2017')
    '1010000011000010000000010111'
    >>> hex_to_bin('70c2017')
    '0111000011000010000000010111'
    '''
    parts = []
    for x in hex_string:
        int_x = int(x, 16)
        parts.append(format(int_x, '04b'))
    return ''.join(parts)


def sum_bin_digits(bin_string):
    '''Sum the digits of binary number.

    >>> sum_bin_digits('111')
    3
    >>> sum_bin_digits('1000101011')
    5
    '''
    return bin_string.count('1')


def squares_used(code):
    '''Calculate squares used.

    >>> squares_used('flqrgnkx')
    8108
    '''
    total = 0
    for i in range(128):
        full_code = f'{code}-{i}'
        h = knot_hash(full_code)
        b = hex_to_bin(h)
        # print(full_code)
        # print(b)
        count = sum_bin_digits(b)
        total += count
    return total


def main():
    '''Main entry point.'''
    total = squares_used(CODE)
    print(total)


if __name__ == '__main__':
    main()
