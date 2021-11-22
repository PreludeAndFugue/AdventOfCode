#!python3

'''Day 17, part 1.'''

from collections import deque

STEP = 354


def spinlock(step, count):
    '''Run a spinlock.'''
    # buffer = [0]
    buffer = deque([0])
    position = 0
    for i in range(1, count + 1):
        position = (position + step) % len(buffer)
        buffer.insert(position + 1, i)
        position += 1
    return buffer


def spinlock2(step, count):
    '''Run a spinlock and calculate what appears at index 1.

    Don't need a list or deque in this case because know that 0 will always be
    at index zero in list.
    '''
    in_position_1 = 1
    position = 0
    for i in range(1, count + 1):
        position = (position + step) % i
        if position == 0:
            in_position_1 = i
        position += 1
    return in_position_1


if __name__ == '__main__':
    buffer = spinlock(STEP, 2017)
    position2017 = buffer.index(2017)
    print(buffer[position2017 + 1])
    position0 = buffer.index(0)
    print(position0, buffer[position0 + 1])

    position1 = spinlock2(STEP, 50_000_000)
    print(position1)