#!python3

'''
To continue, please consult the code grid in the manual. Enter the code at
row 3010, column 3019.
'''


def first_col_number(n):
    return sum(range(n + 1))


def array_number(row, col):
    c = first_col_number(col)
    r = sum(range(col, col + row - 1))
    return c + r


def next_code(n):
    n = 252533 * n
    return n % 33554393


def part1():
    n = array_number(3010, 3019)
    print(n)
    a = 20151125
    print(a)
    for _ in range(n - 1):
        a = next_code(a)
    print(a)


def main():
    part1()



if __name__ == '__main__':
    main()
