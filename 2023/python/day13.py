
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


d = get_input('13').strip()
# d = TEST.strip()

def find_reflection_line(lines):
    ii = []
    for i, (l1, l2) in enumerate(zip(lines, lines[1:])):
        if l1 == l2:
            ii.append(i)
    for i in ii:
        ls1 = reversed(lines[:i + 1])
        ls2 = lines[i + 1:]
        a = all(l1 == l2 for l1, l2 in zip(ls1, ls2))
        if a:
            return 'H', i + 1

    columns = list(zip(*lines))
    jj = []
    for j, (c1, c2) in enumerate(zip(columns, columns[1:])):
        if c1 == c2:
            jj.append(j)
    for j in jj:
        cs1 = reversed(columns[:j + 1])
        cs2 = columns[j + 1:]
        a = all(c1 == c2 for c1, c2 in zip(cs1, cs2))
        if a:
            return 'V', j + 1

    raise ValueError


p1 = 0
for pattern in d.split('\n\n'):
    lines = pattern.split('\n')
    d, n = find_reflection_line(lines)
    if d == 'H':
        p1 += 100 * n
    else:
        p1 += n

print(p1)