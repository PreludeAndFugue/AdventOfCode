#!python3

'''
Here are some tests

>>> answer([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]])
18
'''

import data_2


def diff(row):
    '''Find the difference between largest and smallest values.'''
    row.sort()
    return row[-1] - row[0]


def answer(data):
    '''Calculate answer for input.'''
    return sum(diff(row) for row in data)


def main():
    '''main entry point.'''
    data = data_2.data
    print(answer(data))


if __name__ == '__main__':
    main()
