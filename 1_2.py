#!python3

'''Day 1, part 2.'''

import data_1

def main():
    '''Main entry point.'''
    floor = 0
    for i, ch in enumerate(data_1.data):
        if ch == '(':
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            print(i + 1)
            break


if __name__ == '__main__':
    main()
