
from functools import cmp_to_key
from itertools import zip_longest

from help import get_input

'''
Part 1
------
6118: too high
'''

TEST1 = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''


def parse(s):
    for pair in s.split('\n\n'):
        left, right = pair.split('\n')
        left = eval(left)
        right = eval(right)
        yield left, right


def check_order(left, right, depth=0):
    for l, r in zip_longest(left, right):
        if r is None:
            return False
        if l is None:
            return True
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            elif l > r:
                return False
            else:
                continue
        if isinstance(l, int) and isinstance(r, list):
            c = check_order([l], r, depth + 1)
            if c is None:
                continue
            else:
                return c
        elif isinstance(l, list) and isinstance(r, int):
            c = check_order(l, [r], depth + 1)
            if c is None:
                continue
            else:
                return c
        elif isinstance(l, list) and isinstance(r, list):
            c = check_order(l, r, depth + 1)
            if c is None:
                continue
            else:
                return c
        else:
            raise ValueError
    if depth == 0:
        return True
    else:
        return None


def sorter(left, right):
    c = check_order(left, right)
    assert isinstance(c, bool)
    return -1 if c else 1


def part1(pairs):
    s = 0
    for i, (left, right) in enumerate(pairs, start=1):
        if check_order(left, right):
            s += i
    return s


def part2(pairs):
    start = [[2]]
    end = [[6]]
    flat = [start, end]
    for l, r in pairs:
        flat.append(l)
        flat.append(r)
    s = sorted(flat, key=cmp_to_key(sorter))
    indices = []
    for i, x in enumerate(s, start=1):
        if x == start or x == end:
            indices.append(i)
    a, b = indices
    return a * b


def main():
    s = get_input('13')
    # s = TEST1
    pairs = list(parse(s))

    p1 = part1(pairs)
    p2 = part2(pairs)

    print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()
