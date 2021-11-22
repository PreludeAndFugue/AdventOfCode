#!python3

'''Day 9, part 2.'''

from data_9 import data, State


def process(stream):
    '''Process stream of characters.

    >>> process('<>')
    0
    >>> process('<random characters>')
    17
    >>> process('<<<<>')
    3
    >>> process('<{!>}>')
    2
    >>> process('<!!>')
    0
    >>> process('<!!!>>')
    0
    >>> process('<{o"i!a,<{i<a>')
    10
    '''
    state = State.NORMAL
    total = 0

    for ch in stream:
        new_state, _ = state.process(ch)
        if state == State.GARGABE and new_state == State.GARGABE:
            total += 1
        state = new_state

    return total


if __name__ == '__main__':
    result = process(data)

    print(result)
