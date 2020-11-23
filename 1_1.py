#!python3

'''Day 1, part 1.'''

import data_1

def main():
    '''Main entry point.'''
    data = data_1.data
    up = data.count('(')
    down = data.count(')')
    print(up - down)


if __name__ == '__main__':
    main()
