#!python3

'''
Here are some tests

>>> answer([ [5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]])
9
'''

import data_2


def row_answer(row):
    '''Find the answer for a row.'''
    row = sorted(row, reverse=True)
    for i, n in enumerate(row[:-1]):
        for m in row[i + 1:]:
            if n % m == 0:
                return int(n/m)


def answer(data):
    '''Calculate answer for input.'''
    return sum(row_answer(row) for row in data)


def main():
    '''main entry point.'''
    data = data_2.data
    print(answer(data))


if __name__ == '__main__':
    main()
