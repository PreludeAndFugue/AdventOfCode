#!python3

INPUT = '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^'

TEST_INPUT1 = '..^^.'
TEST_OUTPUT1 = '''..^^.
.^^^^
^^..^'''

TEST_INPUT2 = '.^^.^.^^^^'
TEST_OUTPUT2 = '''.^^.^.^^^^
^^^...^..^
^.^^.^.^^.
..^^...^^^
.^^^^.^^.^
^^..^.^^..
^^^^..^^^.
^..^^^^.^^
.^^^..^.^^
^^.^^^..^^'''


TRAPS = set([
    '^^.',
    '.^^',
    '^..',
    '..^'
])


def update(row):
    l = len(row)
    row = '.' + row + '.'
    new_row = []
    for i in range(l):
        t = row[i:i + 3]
        if t in TRAPS:
            new_row.append('^')
        else:
            new_row.append('.')
    return ''.join(new_row)


def create_rows(row, n):
    rows = [row]
    for _ in range(n):
        row = update(row)
        rows.append(row)
    return rows


def count_safe(rows):
    t = 0
    for row in rows:
        t += row.count('.')
    return t


def test1(row, n):
    rows = [row]
    for _ in range(n):
        row = update(row)
        rows.append(row)
    x = '\n'.join(rows)
    return x


def part1():
    assert '\n'.join(create_rows(TEST_INPUT1, 2)) == TEST_OUTPUT1
    assert '\n'.join(create_rows(TEST_INPUT2, 9)) == TEST_OUTPUT2
    assert count_safe(create_rows(TEST_INPUT2, 9)) == 38

    rows = create_rows(INPUT, 39)
    t = count_safe(rows)
    print(t)


def part2():
    row = INPUT
    t = row.count('.')
    for _ in range(399_999):
        row = update(row)
        t += row.count('.')
    print(t)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
