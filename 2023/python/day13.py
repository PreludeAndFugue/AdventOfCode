
from itertools import combinations

from help import get_input

TEST = '''
#.##..##.
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
#....#..#
'''


def find_smudge(l1, l2):
    '''
    For part 2. Find the number of places where two lines differ. Return True if only
    one difference.
    '''
    d = 0
    i = 0
    for j, (c1, c2) in enumerate(zip(l1, l2)):
        if c1 != c2:
            i = j
            d += 1
    if d == 1:
        return True, i
    else:
        return False, 0


def find_all_smudges(lines):
    for i1, i2 in combinations(range(len(lines)), 2):
        l1, l2 = lines[i1], lines[i2]
        result, i = find_smudge(l1, l2)
        if result:
            yield i1, i


def fix_smudge(lines, li, i):
    '''
    Updates lines to fix a smudge.
    '''
    lines = lines.copy()
    l = lines[li]
    s = l[i]
    s_new = '#' if s == '.' else '.'
    l = l[:i] + s_new + l[i + 1:]
    lines[li] = l
    return lines


def find_reflection_lines(lines, direction):
    '''
    Finds all reflection lines.
    direction: the direction being checked - 'H' or 'V'
    '''
    ii = []
    for i, (l1, l2) in enumerate(zip(lines, lines[1:])):
        if l1 == l2:
            ii.append(i)
    for i in ii:
        ls1 = reversed(lines[:i])
        ls2 = lines[i + 2:]
        a = all(l1 == l2 for l1, l2 in zip(ls1, ls2))
        if a:
            yield direction, i + 1
    return None


def part1(d):
    p1 = 0
    for _, pattern in enumerate(d.split('\n\n')):
        lines = pattern.split('\n')
        result = list(find_reflection_lines(lines, 'H'))
        if result:
            assert len(result) == 1
            d, n = result[0]
            if d == 'H':
                p1 += 100 * n
            else:
                p1 += n
        lines = list(zip(*lines))
        result = list(find_reflection_lines(lines, 'V'))
        if result:
            assert len(result) == 1
            d, n = result[0]
            if d == 'H':
                p1 += 100 * n
            else:
                p1 += n
    return p1


def part2(d):
    p2 = 0
    for pattern in d.split('\n\n'):
        lines = pattern.split('\n')

        old_h = list(find_reflection_lines(lines, 'H'))
        new_reflections = set()

        for li, j in find_all_smudges(lines):
            lines_unsmudged = fix_smudge(lines, li, j)
            for x in list(find_reflection_lines(lines_unsmudged, 'H')):
                new_reflections.add(x)


        lines = [''.join(l) for l in list(zip(*lines))]
        old_v = list(find_reflection_lines(lines, 'V'))

        for li, j in find_all_smudges(lines):
            lines_unsmudged = fix_smudge(lines, li, j)
            for x in list(find_reflection_lines(lines_unsmudged, 'V')):
                new_reflections.add(x)

        new_reflections -= set(old_h)
        new_reflections -= set(old_v)
        assert len(new_reflections) == 1, new_reflections
        d, n = new_reflections.pop()

        if d == 'H':
            p2 += 100 * n
        else:
            p2 += n

    return p2


def main():
    d = get_input('13').strip()
    # d = TEST.strip()

    p1 = part1(d)
    print(p1)

    p2 = part2(d)
    print(p2)


if __name__ == '__main__':
    main()
