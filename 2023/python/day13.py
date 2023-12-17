
from itertools import combinations

from help import get_input

TEST = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''


def find_diff_1(l1, l2):
    '''
    For part 2. Find the number of places where two lines differ. Return True if only
    one difference.
    '''
    d = 0
    for c1, c2 in zip(l1, l2):
        if c1 != c2:
            d += 1
    return d == 1


def find_reflection_line(lines, fn):
    ii = []
    for i, (l1, l2) in enumerate(zip(lines, lines[1:])):
        if fn(l1, l2):
            ii.append(i)
    for i in ii:
        ls1 = reversed(lines[:i])
        ls2 = lines[i + 2:]
        a = all(l1 == l2 for l1, l2 in zip(ls1, ls2))
        if a:
            return 'H', i + 1

    columns = list(zip(*lines))
    jj = []
    for j, (c1, c2) in enumerate(zip(columns, columns[1:])):
        if fn(c1, c2):
            jj.append(j)
    for j in jj:
        cs1 = reversed(columns[:j])
        cs2 = columns[j + 2:]
        a = all(c1 == c2 for c1, c2 in zip(cs1, cs2))
        if a:
            return 'V', j + 1

    raise ValueError


def find_reflection_line_2(lines, fn):
    '''
    Algorithm for part 2. Find the reflection line for part 1. If the line is
    horizontal, then part two reflection line may be, in this order,

    1. A horizontal line between the first two or last two lines.
    2. A vertical line
    '''
    d, n = find_reflection_line(lines, fn)
    print('old reflection line', d, n)

    if d == 'H':
        if find_diff_1(lines[0], lines[1]):
            return 'H', 1
        if find_diff_1(lines[-2], lines[-1]):
            return 'H', len(lines) - 1

        # now check columns
        columns = list(zip(*lines))
        # jj = []
        col_indices = range(len(columns))
        for ci1, ci2 in combinations(col_indices, 2):
            c1 = columns[ci1]
            c2 = columns[ci2]
            if find_diff_1(c1, c2):
                di = ci2 - ci2
                middle = di // 2
                return 'V', ci1 + middle + 1
                # jj.append(j)
        # for j in jj:
        #     cs1 = reversed(columns[:j])
        #     cs2 = columns[j + 2:]
        #     a = all(c1 == c2 for c1, c2 in zip(cs1, cs2))
        #     if a:
        #         return j + 1

        raise ValueError

    else:
        # print('checking V edge cases')
        columns = list(zip(*lines))

        # print(columns[0], columns[1])
        if find_diff_1(columns[0], columns[1]):
            return 'V', 1

        # print(columns[-2], columns[-1])
        if find_diff_1(columns[-2], columns[-1]):
            return 'V', len(columns) - 1

        # work with lines
        # ii = []
        row_indices = range(len(lines))
        for li1, li2 in combinations(row_indices, 2):
            l1 = lines[li1]
            l2 = lines[li2]

            print(li1, li2)
            print(l1)
            print(l2)
            print(find_diff_1(l1, l2))
            print()

            if find_diff_1(l1, l2):
                # print('found H diff', li1, l1, li2, l2)
                di = li2 - li1
                middle = di // 2
                return 'H', li1 + middle + 1
                # ii.append(i)
        # for i in ii:
        #     ls1 = reversed(lines[:i])
        #     ls2 = lines[i + 2:]
        #     a = all(l1 == l2 for l1, l2 in zip(ls1, ls2))
        #     if a:
        #         return i + 1

    raise ValueError

d = get_input('13').strip()
# d = TEST.strip()

p1 = 0
p2 = 0
for i, pattern in enumerate(d.split('\n\n')):
    print(i)
    lines = pattern.split('\n')

    # print('\n'.join(lines))

    fn = lambda l1, l2: l1 == l2
    d, n = find_reflection_line(lines, fn)
    d2, n2 = find_reflection_line_2(lines, fn)
    # print('new reflection line', d2, n2)

    if d == 'H':
        p1 += 100 * n
    else:
        p1 += n


    if d2 == 'H':
        p2 += 100 * n2
    elif d2 == 'V':
        p2 += n2
    else:
        raise ValueError

print(p1)
print(p2)