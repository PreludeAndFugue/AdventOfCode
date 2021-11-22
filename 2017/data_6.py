#!python3

'''Data for day 6.'''

INPUT = '''2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14'''

data = [int(x.strip()) for x in INPUT.split()]

def redistribute(banks):
    '''Redistribute items in largest memory bank.

    >>> redistribute((0, 2, 7, 0))
    (2, 4, 1, 2)
    >>> redistribute((2, 4, 1, 2))
    (3, 1, 2, 3)
    >>> redistribute((3, 1, 2, 3))
    (0, 2, 3, 4)
    >>> redistribute((0, 2 , 3, 4))
    (1, 3, 4, 1)
    >>> redistribute((1, 3, 4, 1))
    (2, 4, 1, 2)
    '''
    banks = list(banks)
    max_value, position = max_and_position(banks)
    bank_count = len(banks)
    banks[position] = 0
    for i in range(max_value):
        p = (position + i + 1) % bank_count
        banks[p] = banks[p] + 1
    return tuple(banks)


def max_and_position(banks):
    '''Find position and value in maximum bank.

    >>> max_and_position([0, 2, 7, 0])
    (7, 2)
    >>> max_and_position([2, 4, 1, 2])
    (4, 1)
    >>> max_and_position([3, 1, 2, 3])
    (3, 0)
    >>> max_and_position([0, 2, 3, 4])
    (4, 3)
    >>> max_and_position([1, 3, 4, 1])
    (4, 2)
    '''
    max_value = 0
    max_position = 0
    for position, value in enumerate(banks):
        if value > max_value:
            max_value = value
            max_position = position
    return max_value, max_position
