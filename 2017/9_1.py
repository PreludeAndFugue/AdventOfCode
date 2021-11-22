#!python3

'''Day 9, part 1.'''

from enum import Enum

from data_9 import data, State


def process(stream):
    '''Process a stream of characters.

    >>> process('{}')
    1
    >>> process('{{{}}}')
    6
    >>> process('{{},{}}')
    5
    >>> process('{{{},{},{{}}}}')
    16
    >>> process('{<a>,<a>,<a>,<a>}')
    1
    >>> process('{{<ab>},{<ab>},{<ab>},{<ab>}}')
    9
    >>> process('{{<!!>},{<!!>},{<!!>},{<!!>}}')
    9
    >>> process('{{<a!>},{<a!>},{<a!>},{<ab>}}')
    3
    '''
    state = State.NORMAL
    level = 0
    total = 0

    for ch in stream:
        state, output = state.process(ch)
        if output == '{':
            level += 1
        elif output == '}':
            total += level
            level -= 1
    return total


if __name__ == '__main__':
    result = process(data)
    print(result)
