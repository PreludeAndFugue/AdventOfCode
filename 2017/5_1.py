#!python3

'''Day 5, part 1.'''

import data_5

def count_jumps(instructions):
    '''Count number of jumps to exit instructions.

    >>> count_jumps([0, 3, 0, 1, -3])
    5
    '''
    counter = 0
    position = 0
    instruction_count = len(instructions)
    while True:
        action = instructions[position]
        instructions[position] = instructions[position] + 1
        counter += 1
        position += action
        if position < 0 or position >= instruction_count:
            break

    return counter



def main():
    '''Main entry point.'''
    data = data_5.data
    count = count_jumps(data)
    print(count)


if __name__ == '__main__':
    main()
