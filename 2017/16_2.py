#!python3

'''Day 16, part 2.'''

from itertools import chain

from data_16 import commands, dance, data
import data_16

REPEAT = 1_000_000_000
# REPEAT = 1


def dance_position_changes(commands, data, items):
    '''A list of 2-tuples where each tuple is (start_pos, end_pos) of item in items.'''
    end_items = dance(commands, data, items)
    return list((i, end_items.find(item)) for i, item in enumerate(items))


def create_cycles(position_changes):
    '''Create cycles from position changes.'''
    position_changes_dict = {pos_from: pos_to for pos_from, pos_to in position_changes}
    cycles = []
    current_cycle = []
    position = None
    while position_changes_dict:
        if position is None:
            item, position = position_changes_dict.popitem()
            current_cycle.append(item)
        else:
            position = position_changes_dict.pop(position)
        if position in current_cycle:
            cycles.append(current_cycle)
            current_cycle = []
            position = None
        else:
            current_cycle.append(position)
    return cycles


def rotate_cycle(cycle, n):
    '''Rotate cycle n times.

    >>> rotate_cycle([0, 1, 2, 3], 1)
    [3, 0, 1, 2]
    >>> rotate_cycle([0, 1, 2, 3], 2)
    [2, 3, 0, 1]
    >>> rotate_cycle([0, 1, 2, 3], 3)
    [1, 2, 3, 0]
    >>> rotate_cycle([0, 1, 2, 3], 4)
    [0, 1, 2, 3]
    >>> rotate_cycle([0, 1, 2, 3], 5)
    [3, 0, 1, 2]
    '''
    len_cycle = len(cycle)
    m = n % len_cycle
    # return cycle[len_cycle - m:] + cycle[:len_cycle - m]
    return cycle[m:] + cycle[:m]


def rotate_cycles(cycles, n):
    '''Rotate cycles n times.

    >>> rotate_cycles([[0, 1, 2, 3], [4]], 1)
    [[3, 0, 1, 2], [4]]
    >>> rotate_cycles([[0, 1, 2, 3], [4]], 2)
    [[2, 3, 0, 1], [4]]
    '''
    return [rotate_cycle(cycle, n) for cycle in cycles]


def position_changes_from_cycles(cycle1, cycle2):
    '''Create a list of position changes.'''
    return list((a, b) for a, b in zip(chain(*cycle1), chain(*cycle2)))


def permute_items(items, position_changes):
    '''Permute items base on position changes.'''
    final_positions = [None] * len(items)
    for m, n in position_changes:
        final_positions[n] = items[m]
    return ''.join(final_positions)


def main3():
    '''Main entry point.

    The main dance repeats every 42 dances
    '''
    items = data_16.items
    print(0, items)
    repeat = REPEAT % 42
    for i in range(1, 100):
        items = dance(commands, data, items)
        print(i, items)


if __name__ == '__main__':
    main3()

    x = 0
    values = []
    while x < 1_000_000_000:
        values.append(x)
        x += 42

    print(values[:5])
    print(values[-5:])

    items = data_16.items
    print(999999966, items)
    for i in range(999999967, 1_000_000_000 + 1):
        items = dance(commands, data, items)
        print(i, items)
