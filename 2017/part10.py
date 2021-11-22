#!python3

'''Day 10, part 1 & 2.'''

from functools import reduce

data = '129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108'

INPUT_LENGTHS_1 = list(map(int, data.split(',')))
EXTRA_LENGTHS = [17, 31, 73, 47, 23]

def rearrange(items, input_lengths, current_position=0, skip_size_start=0):
    '''Main method for rearranging items for part 1.

    >>> rearrange([0, 1, 2, 3, 4], [3, 4, 1, 5])
    ([3, 4, 2, 1, 0], 4, 4)
    '''
    len_items = len(items)
    output_skip_size = 0
    for skip_size, input_length in enumerate(input_lengths, start=skip_size_start):
        elements = get_elements(items, current_position, input_length)
        elements = reversed(elements)
        items = replace_elements(items, current_position, elements)
        # print(items, elements, skip_size, input_length)
        current_position = (current_position + input_length + skip_size) % len_items
        output_skip_size = skip_size

    return items, current_position, output_skip_size + 1


def get_elements(items, start, count):
    '''Get elements from items - loop round if count goes beyond end of list.

    >>> get_elements([1, 2, 3, 4], 0, 2)
    [1, 2]
    >>> get_elements([1, 2, 3, 4], 1, 3)
    [2, 3, 4]
    >>> get_elements([1, 2, 3, 4], 0, 4)
    [1, 2, 3, 4]
    >>> get_elements([1, 2, 3, 4], 2, 3)
    [3, 4, 1]
    >>> get_elements([1, 2, 3, 4], 3, 4)
    [4, 1, 2, 3]
    >>> get_elements([1, 2, 3, 4], 2, 5)
    Traceback (most recent call last):
    ...
    Exception: Count is longer than items
    '''
    item_count = len(items)
    if count > item_count:
        raise Exception('Count is longer than items')
    if start + count <= item_count:
        return items[start:start + count]
    return items[start:] + items[:count - (item_count - start)]


def replace_elements(items, start, elements):
    '''Replace elements in items.

    >>> replace_elements([0, 0, 0, 0], 0, [1, 1])
    [1, 1, 0, 0]
    >>> replace_elements([0, 0, 0, 0], 2, [1])
    [0, 0, 1, 0]
    >>> replace_elements([0, 0, 0, 0], 3, [1, 1])
    [1, 0, 0, 1]
    >>> replace_elements([0, 0, 0, 0], 1, [1, 1, 1, 1])
    [1, 1, 1, 1]
    >>> replace_elements([0, 0, 0, 0], 2, [1, 1, 1])
    [1, 0, 1, 1]
    '''
    len_items = len(items)
    for i, element in enumerate(elements, start=start):
        items[i % len_items] = element
    return items


def dense_hash(items):
    '''Calculate the dense hash.

    >>> dense_hash(range(256))
    '00000000000000000000000000000000'
    '''
    values = []
    for i in range(16):
        start = 16*i
        items_for_hash = items[start:start + 16]
        x = reduce(lambda m, n: m ^ n, items_for_hash)
        values.append(x)
    return ''.join(format(value, '02x') for value in values)


def get_lengths(input_string):
    '''Get lengths from input string for part 2.

    >>> get_lengths('1,2,3')
    [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]
    '''
    return [ord(x) for x in input_string] + EXTRA_LENGTHS


def rearrange64(items, input_lengths):
    '''Main method for rearranging items for part 2.

    >>> rearrange64(list(range(256)), '')
    'a2582a3a0e66e6e86e3812dcb672a272'

    >>> rearrange64(list(range(256)), 'AoC 2017')
    '33efeb34ea91902bb2f59c9920caa6cd'

    >>> rearrange64(list(range(256)), '1,2,3')
    '3efbe78a8d82f29979031a4aa0b16a9d'

    >>> rearrange64(list(range(256)), '1,2,4')
    '63960835bcdc130f0b66d7ff4f6a5a8e'
    '''
    input_lengths = get_lengths(input_lengths)
    current_position = 0
    skip_size = 0
    for _ in range(64):
        items, current_position, skip_size = rearrange(items, input_lengths, current_position, skip_size)
    return dense_hash(items)


def knot_hash(string):
    '''Calculate knot hash of string.'''
    return rearrange64(list(range(256)), string)


def part1():
    '''Calculate answer for part 1.'''
    items = list(range(256))
    items, _, _ = rearrange(items, INPUT_LENGTHS_1)
    total = items[0] * items[1]
    print('part 1:', total)


def part2():
    '''Calculate answer for part 2.'''
    items = list(range(256))
    result = rearrange64(items, data)
    print('part 2', result)


if __name__ == '__main__':
    part1()
    part2()
